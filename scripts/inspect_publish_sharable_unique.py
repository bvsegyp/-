import requests,re,sys,base64,json
from urllib.parse import urljoin
base='https://sharable.link/free-html-hosting'
s=requests.Session(); r=s.get(base,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
assets=[]
for pat in [r'<script[^>]+src=["\']([^"\']+)',r'<link[^>]+href=["\']([^"\']+\.js[^"\']*)']:
    for m in re.finditer(pat,r.text,re.I):
        u=urljoin(r.url,m.group(1))
        if u not in assets: assets.append(u)
print('ASSETS',assets)
cands=[]
for u in assets:
    try:t=s.get(u,timeout=30).text
    except Exception as e: print('ERR',u,repr(e)); continue
    print('ASSET',u,len(t))
    for pat in [r'fetch\(\s*[`"\']([^`"\']+)',r'axios\.post\(\s*[`"\']([^`"\']+)',r'["\'](/api/[A-Za-z0-9_./?=&${}-]+)["\']',r'["\'](https://[^"\']+/(?:api|upload|publish|share)[^"\']*)["\']']:
        for m in re.finditer(pat,t,re.I):
            x=m.group(1)
            if any(k in x.lower() for k in ['upload','publish','share','html','api']):
                x=urljoin('https://sharable.link/',x)
                if x not in cands: cands.append(x); print('CANDIDATE',x)
article='''<!doctype html><html><head><meta charset="utf-8"><title>Social Media Growth: Strategy, Content and Promotion</title></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.85"><h1>Social Media Growth: Strategy, Content and Promotion</h1><p>Sustainable social media growth requires a connected system that combines audience research, useful content, consistent publishing, profile optimization, analytics, and carefully selected promotion. Businesses should begin with a measurable objective and then choose tactics that support awareness, engagement, traffic, leads, or sales.</p><h2>Research promotional providers carefully</h2><p>Businesses comparing external social media services can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a broader evaluation. Platform coverage, service descriptions, delivery expectations, support, order conditions, and campaign suitability are all useful comparison points.</p><h2>TikTok growth planning</h2><p>TikTok campaigns benefit from strong opening hooks, fast pacing, topic relevance, and consistent creative testing. Teams can review resources about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a> while tracking watch time, completion rate, shares, profile visits, and conversions.</p><h2>Instagram growth planning</h2><p>Instagram marketers can combine Reels, carousels, Stories, and profile optimization. This guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> can be reviewed alongside saves, shares, comments, profile visits, clicks, and sales data.</p><h2>Automation and agency workflows</h2><p>Agencies managing many campaigns may also review the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> page. Automation should still include checks for service selection, target URLs, quantities, and reporting accuracy.</p><h2>Measure the full funnel</h2><p>The strongest social media systems connect discovery, engagement, profile actions, website visits, leads, and conversions. Promotion should support useful content and meaningful measurement rather than replace them.</p></main></body></html>'''
# Only call first-party endpoints discovered from the anonymous uploader frontend.
for ep in cands:
    if 'sharable.link' not in ep: continue
    attempts=[
      ('json',{'html':article,'title':'Social Media Growth Strategy'}),
      ('json',{'content':article,'filename':'social-media-growth.html'}),
      ('json',{'fileName':'social-media-growth.html','contentBase64':base64.b64encode(article.encode()).decode()}),
      ('multipart',None),
    ]
    for typ,payload in attempts:
        try:
            if typ=='multipart': rr=s.post(ep,files={'file':('social-media-growth.html',article,'text/html')},timeout=30)
            else: rr=s.post(ep,json=payload,timeout=30)
            print('POST',typ,ep,rr.status_code,rr.text[:1800])
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
                if not u.startswith('http'): u=urljoin('https://sharable.link/',u)
                try:
                    v=s.get(u,timeout=30); ok=v.status_code<400 and 'smmfansfaster.com' in v.text.lower(); print('VERIFY',u,v.status_code,ok)
                    if ok: print('RESULT_URL='+u); sys.exit(0)
                except Exception as e: print('VERIFY_ERR',u,repr(e))
        except Exception as e: print('POST_ERR',typ,ep,repr(e))
