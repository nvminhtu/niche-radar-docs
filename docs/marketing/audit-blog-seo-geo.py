"""Audit SEO + GEO cho bài blog shotmatic (đã đăng = không draft).
Rubric gộp từ: AgriciDaniel/claude-seo (seo-content, seo-page), zubair-trabzada/geo-seo-claude (geo-citability),
coreyhaines31/marketingskills (seo-audit, ai-seo). Chỉ đo cái check_post.mjs chưa đo.
usage: python3 -I audit_posts.py <repo> <out.json>
"""
import sys, re, json, os, collections, yaml

repo, out = sys.argv[1], sys.argv[2]
d = os.path.join(repo, 'content/blog')
posts = {}
for f in sorted(os.listdir(d)):
    if not f.endswith('.md'):
        continue
    raw = open(os.path.join(d, f), encoding='utf8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.S)
    fm, body = yaml.safe_load(m.group(1)), m.group(2)
    if fm.get('draft'):
        continue
    posts[f[:-3]] = (fm, body)

W = lambda s: len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.%$-]*", s or ''))
PRONOUN = re.compile(r'^(it|this|that|these|those|they|he|she|so|but|and|also|here)\b', re.I)
NUM = re.compile(r'(\$?\d[\d,.]*\s?(%|★|k|m|x)?)')
FIRSTHAND = re.compile(r"\b(I|we) (measured|tested|ran|checked|counted|built|tried|found|pulled|looked)\b|\bon (\d{1,2} )?(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]* \d{4}|\bas of \w+ \d{4}|\b(checked|measured|pulled) (in |on )?\w+ \d{4}", re.I)
AIPHRASE = re.compile(r"\b(crucial|robust|comprehensive|navigat(e|ing) the|landscape|realm|tapestry|it'?s worth noting|in the world of|ever-evolving|harness|empower|streamline|cutting-edge|dive into|deep dive|whether you'?re)\b", re.I)

inbound = collections.Counter()
for s, (fm, body) in posts.items():
    for l in set(re.findall(r'\]\(/blog/([^)#\s/]+)', body)):
        inbound[l] += 1

kwmap = collections.defaultdict(list)
rows = []
for s, (fm, body) in posts.items():
    kw = (fm.get('keyword') or '').lower().strip()
    kwmap[kw].append(s)
    title, desc = fm.get('title', ''), fm.get('description', '')
    words = W(body)
    first100 = ' '.join(re.findall(r'\S+', re.sub(r'^#.*$', '', body, flags=re.M))[:100]).lower()
    kwtoks = [t for t in re.findall(r'[a-z0-9]+', kw) if len(t) > 2]
    has = lambda txt: all(t in txt.lower() for t in kwtoks) if kwtoks else False
    h2s = re.findall(r'^## (.+)$', body, re.M)
    # tách section theo H2
    secs = re.split(r'^## .+$', body, flags=re.M)[1:]
    openers, pron, lens, ans_first = [], 0, [], 0
    for sec in secs:
        paras = [p.strip() for p in sec.strip().split('\n\n') if p.strip() and not p.strip().startswith(('#', '|', '!', '<', '```'))]
        if not paras:
            continue
        p0 = re.sub(r'[*_`]', '', paras[0])
        if PRONOUN.match(p0):
            pron += 1
        if not re.match(r'^(\d+\.|-|\*)', p0) and 15 <= W(p0) <= 80:
            ans_first += 1
        lens.append(W(sec))
    n = max(len(secs), 1)
    nums = len(NUM.findall(body))
    il = re.findall(r'\]\((/[^)\s]*)\)', body)
    el = re.findall(r'\]\((https?://[^)\s]+)\)', body)
    imgs = re.findall(r'!\[([^\]]*)\]\(', body)
    tables = len(re.findall(r'^\|.*\|\s*$\n^\|[\s:|-]+\|', body, re.M))
    upd = str(fm.get('updated') or fm.get('date'))
    issues = []
    if len(title) > 60: issues.append(f'title {len(title)} ký tự (>60, Google cắt)')
    if not has(title): issues.append('keyword không có trong title')
    if not has(desc): issues.append('keyword không có trong description')
    if len(desc) < 120: issues.append(f'description ngắn {len(desc)} ký tự')
    if not has(first100 + ' ' + (fm.get('answer') or '')): issues.append('keyword không ở 100 từ đầu/answer')
    if kwtoks and not any(has(h) for h in h2s): issues.append('keyword không có trong H2 nào')
    if kwtoks and not all(t in s for t in kwtoks[:2]): issues.append('slug không chứa keyword')
    if words + 0 < 1500: issues.append(f'thân bài {words} từ (<1.500 sàn blog của claude-seo)')
    ilr = len(il) / max(words, 1) * 1000
    if ilr < 3: issues.append(f'link nội bộ {ilr:.1f}/1000 từ (<3)')
    if inbound[s] == 0: issues.append('bài mồ côi: không bài nào link tới')
    if not el: issues.append('không có link nguồn ngoài trong thân bài')
    if not imgs: issues.append('không có ảnh/screenshot trong bài')
    elif any(not a.strip() for a in imgs): issues.append('ảnh thiếu alt')
    if not tables: issues.append('không có bảng (khối AI dễ trích nhất)')
    if pron / n > 0.25: issues.append(f'{pron}/{n} section mở bằng đại từ (không tự đứng được)')
    if ans_first / n < 0.7: issues.append(f'chỉ {ans_first}/{n} section mở bằng đoạn trả lời 15–80 từ')
    if nums / max(words, 1) * 1000 < 8: issues.append(f'mật độ số {nums / max(words,1)*1000:.1f}/1000 từ (thấp)')
    if not FIRSTHAND.search(body + ' ' + str(fm.get('evidence', ''))): issues.append('không thấy dấu hiệu tự đo/tự thử (Experience)')
    ai = AIPHRASE.findall(body)
    if len(ai) >= 3: issues.append(f'{len(ai)} cụm văn AI ({", ".join(sorted(set(x[0] if isinstance(x, tuple) else x for x in ai))[:4])})')
    if upd < '2026-08-01': issues.append(f'cập nhật lần cuối {upd}')
    q = sum(h.strip().endswith('?') for h in h2s)
    rows.append(dict(slug=s, keyword=kw, topic=fm.get('topic'), words=words, title_len=len(title), h2=len(h2s), h2_q=q,
                     int_links=len(il), inbound=inbound[s], ext_links=len(el), images=len(imgs), tables=tables,
                     nums_per_k=round(nums / max(words, 1) * 1000, 1), sec_pronoun=pron, sec_answer_first=ans_first,
                     sections=n, avg_sec_words=round(sum(lens) / max(len(lens), 1)), updated=upd, issues=issues))

cannibal = {k: v for k, v in kwmap.items() if len(v) > 1}
cnt = collections.Counter(i.split(' (')[0].split(' {')[0] for r in rows for i in [re.sub(r'\d+(\.\d+)?', 'N', x) for x in r['issues']])
json.dump(dict(n=len(rows), rows=rows, cannibal=cannibal, issue_counts=cnt.most_common()), open(out, 'w'), ensure_ascii=False, indent=1)
print('posts', len(rows))
for k, v in cnt.most_common():
    print(f'{v:3d}  {k}')
print('\ncannibal:', json.dumps(cannibal, indent=0))
