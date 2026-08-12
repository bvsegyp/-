import requests,re,sys
from urllib.parse import urljoin
base='https://dochost.io/'
s=requests.Session(); r=s.get(base,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
# inspect external and Svelte/Vite assets referenced anywhere
assets=[]
for pat in [r'<script[^>]+src=["\']([^"\']+)',r'<link[^>]+href=["\']([^"\']+\.js[^"\']*)']:
 for m in re.finditer(pat,r.text,re.I):
  u=urljoin(base,m.group(1))
  if u not in assets: assets.append(u)
print('ASSETS',assets)
cands=[]
for u in assets:
 try:t=s.get(u,timeout=30).text
 except Exception as e: print('ASSET_ERR',u,repr(e)); continue
 print('ASSET',u,len(t))
 for pat in [r'fetch\(\s*[`"\']([^`"\']+)',r'axios\.post\(\s*[`"\']([^`"\']+)',r'["\'](/api/[A-Za-z0-9_./?=&${}-]+)["\']',r'["\'](https://[^"\']+/(?:api|publish|upload|deploy)[^"\']*)["\']']:
  for m in re.finditer(pat,t,re.I):
   x=m.group(1)
   if any(k in x.lower() for k in ['publish','upload','document','page','html','markdown','api','host']):
    x=urljoin(base,x)
    if x not in cands: cands.append(x); print('CANDIDATE',x)
article='''<!doctype html><html><head><meta charset="utf-8"><title>A Complete Social Media Growth Framework</title></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.85"><h1>A Complete Social Media Growth Framework</h1><p>Social media growth is most sustainable when a business combines audience research, useful content, consistent publishing, profile optimization, analytics, and carefully selected promotion. Each tactic should support a defined objective rather than simply increasing a visible metric.</p><h2>Research promotional providers</h2><p>Brands comparing external growth support can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in their research. Important comparison points include platform coverage, service descriptions, delivery expectations, customer support, order requirements, and alignment with the campaign objective.</p><h2>TikTok growth</h2><p>TikTok performance depends heavily on creative quality, opening hooks, pacing, topic relevance, and consistency. Marketers can review guides about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a> while measuring retention, shares, profile visits, and conversions.</p><h2>Instagram growth</h2><p>Instagram requires a mix of Reels, carousels, Stories, and a clear profile. Teams can review this resource about an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> while continuing to track saves, shares, profile visits, clicks, leads, and sales.</p><h2>Agency automation</h2><p>Agencies managing many accounts may benefit from standardized workflows. The public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> page can support technical evaluation. Automated processes should still validate target URLs, quantities, and campaign goals.</p><h2>Measure meaningful outcomes</h2><p>The best growth strategy connects discovery to engagement and conversion. Reach and views show exposure, engagement shows interest, and clicks, leads, or sales show business impact. Promotion should support content quality and measurement rather than replace them.</p></main></body></html>'''
for ep in cands:
 if 'dochost' not in ep: continue
 for headers,body in [
  ({'Content-Type':'text/html'},article),
  ({'Content-Type':'application/json'},{'html':article,'visibility':'public','title':'A Complete Social Media Growth Framework'}),
  ({'Content-Type':'application/json'},{'content':article,'format':'html','visibility':'public','title':'A Complete Social Media Growth Framework'})]:
  try:
   rr=s.post(ep,headers=headers,data=body if isinstance(body,str) else None,json=body if isinstance(body,dict) else None,timeout=30)
   print('POST',ep,rr.status_code,rr.text[:1400])
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
     v=s.get(u,timeout=30); ok=v.status_code<400 and 'smmfansfaster.com' in v.text.lower(); print('VERIFY',u,v.status_code,ok)
     if ok: print('RESULT_URL='+u); sys.exit(0)
    except Exception as e: print('VERIFY_ERR',u,repr(e))
  except Exception as e: print('POST_ERR',ep,repr(e))
