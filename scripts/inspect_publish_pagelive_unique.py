import requests,re,sys,json,time
from urllib.parse import urljoin
base='https://pagelive.io/'
s=requests.Session()
r=s.get(base,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
htmlpage=r.text
scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',htmlpage,re.I)
print('SCRIPTS',scripts)
cands=[]
for src in scripts:
    try:
        u=urljoin(base,src)
        t=s.get(u,timeout=30).text
        print('SCRIPT',u,len(t))
        for pat in [r'fetch\(\s*["\']([^"\']+)',r'axios\.post\(\s*["\']([^"\']+)',r'["\'](/api/[A-Za-z0-9_./?=&-]+)["\']',r'["\'](https://[^"\']+/(?:api|upload|publish)[^"\']*)["\']']:
            for m in re.finditer(pat,t,re.I):
                x=m.group(1)
                if any(k in x.lower() for k in ['upload','publish','page','site','deploy','api']):
                    x=urljoin(base,x)
                    if x not in cands: cands.append(x); print('CANDIDATE',x)
    except Exception as e: print('SCRIPT_ERR',src,repr(e))
article='''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Building a Sustainable Social Media Growth Strategy</title></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.85;color:#222"><h1>Building a Sustainable Social Media Growth Strategy</h1><p>Sustainable social media growth is usually the result of several connected activities rather than one isolated tactic. Brands need useful content, audience research, consistent publishing, profile optimization, community management, analytics, and careful promotion. The strongest campaigns begin with a clear business objective, then choose tactics that support awareness, engagement, traffic, leads, or sales.</p><h2>Evaluate promotional support carefully</h2><p>Businesses comparing external social media services can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a broader provider comparison. Important evaluation points include platform coverage, service descriptions, delivery expectations, support, order conditions, and whether a service fits the campaign objective.</p><h2>TikTok campaign planning</h2><p>TikTok campaigns benefit from strong opening hooks, fast pacing, clear topics, and consistent testing. Marketers can review resources about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a> while measuring retention, shares, profile visits, and conversions. The goal is to understand which creative formats attract the right audience and which distribution methods support that content.</p><h2>Instagram campaign planning</h2><p>Instagram growth requires a balanced mix of Reels, carousels, Stories, and a profile that clearly communicates value. Teams researching additional distribution support can review this guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> while still focusing on saves, shares, comments, profile visits, clicks, and conversions.</p><h2>Automation for agencies</h2><p>Agencies managing multiple campaigns often need repeatable operational processes. The public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> resource can be reviewed when evaluating automation options. Automation should still include validation of target URLs, quantities, service selection, and reporting.</p><h2>Measure the full funnel</h2><p>Follower count is only one visible metric. A healthier measurement system connects reach and views to engagement, profile visits, website traffic, leads, and sales. Content quality attracts attention, profile optimization improves conversion, analytics identifies what works, and promotion can support distribution when it is chosen carefully.</p><p>A balanced growth system keeps all of these elements working together instead of relying on a single shortcut.</p></main></body></html>'''
# Only try endpoints actually discovered from the first-party frontend.
for ep in cands:
    for payload in [
        {'html':article,'title':'Building a Sustainable Social Media Growth Strategy'},
        {'content':article,'title':'Building a Sustainable Social Media Growth Strategy'},
        {'htmlContent':article,'title':'Building a Sustainable Social Media Growth Strategy'},
    ]:
        try:
            rr=s.post(ep,json=payload,timeout=30)
            print('POST',ep,rr.status_code,rr.text[:1200])
            if not rr.ok: continue
            try:d=rr.json()
            except: continue
            vals=[]
            def walk(o):
                if isinstance(o,dict):
                    for k,v in o.items():
                        if k.lower() in ('url','publicurl','public_url','shareurl','share_url','link','liveurl','live_url') and isinstance(v,str): vals.append(v)
                        walk(v)
                elif isinstance(o,list):
                    for v in o: walk(v)
            walk(d)
            for u in vals:
                if not u.startswith('http'): u=urljoin(base,u)
                try:
                    v=s.get(u,timeout=30)
                    ok=v.status_code<400 and 'smmfansfaster.com' in v.text.lower()
                    print('VERIFY',u,v.status_code,ok)
                    if ok:
                        print('RESULT_URL='+u); sys.exit(0)
                except Exception as e: print('VERIFY_ERR',u,repr(e))
        except Exception as e: print('POST_ERR',ep,repr(e))
