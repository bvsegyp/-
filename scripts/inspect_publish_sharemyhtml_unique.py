import requests,re,sys,os,tempfile
from urllib.parse import urljoin
base='https://sharemyhtml.com/'
s=requests.Session(); r=s.get(base,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
assets=[]
for pat in [r'<script[^>]+src=["\']([^"\']+)',r'<link[^>]+href=["\']([^"\']+\.js[^"\']*)']:
 for m in re.finditer(pat,r.text,re.I):
  u=urljoin(base,m.group(1))
  if u not in assets: assets.append(u)
print('ASSETS',assets)
cands=[]
for u in assets:
 try:t=s.get(u,timeout=30).text
 except Exception as e: print('ERR',u,repr(e)); continue
 print('ASSET',u,len(t))
 for pat in [r'fetch\(\s*[`"\']([^`"\']+)',r'axios\.post\(\s*[`"\']([^`"\']+)',r'["\'](/api/[A-Za-z0-9_./?=&${}-]+)["\']',r'["\'](https://[^"\']+/(?:api|upload|publish)[^"\']*)["\']']:
  for m in re.finditer(pat,t,re.I):
   x=m.group(1)
   if any(k in x.lower() for k in ['upload','publish','html','page','api']):
    x=urljoin(base,x)
    if x not in cands: cands.append(x); print('CANDIDATE',x)
article='''<!doctype html><html><head><meta charset="utf-8"><title>Social Media Growth Strategy: Content, Promotion and Measurement</title></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.85"><h1>Social Media Growth Strategy: Content, Promotion and Measurement</h1><p>A sustainable social media strategy connects content quality, audience research, consistent publishing, profile optimization, analytics, and carefully selected promotion. Businesses should define a measurable objective first and then choose tactics that support awareness, engagement, traffic, leads, or sales.</p><h2>Evaluating promotional support</h2><p>Teams researching external services can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a broader comparison. Platform coverage, delivery conditions, support, service descriptions, and campaign fit are all more useful evaluation points than price alone.</p><h2>TikTok growth</h2><p>TikTok rewards fast creative testing. Strong hooks, editing pace, topic relevance, and repeatable formats can influence watch time and discovery. Marketers can review resources about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a> while tracking completion rate, shares, profile visits, and conversions.</p><h2>Instagram growth</h2><p>Instagram teams can combine Reels, carousels, Stories, and profile optimization. This guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> can be reviewed alongside organic engagement metrics such as saves, shares, comments, profile visits, and clicks.</p><h2>Agency automation</h2><p>Agencies managing repeated workflows may also review the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> page. Automation should still include validation and reporting checks.</p><p>The strongest growth systems measure the full funnel from discovery to engagement and conversion instead of relying on one visible metric.</p></main></body></html>'''
open('/tmp/sharemyhtml.html','w').write(article)
# only try first-party endpoints discovered from frontend
for ep in cands:
 if 'sharemyhtml.com' not in ep: continue
 tries=[
   ('multipart',None),
   ('json',{'html':article,'title':'Social Media Growth Strategy: Content, Promotion and Measurement'}),
   ('raw',article)
 ]
 for typ,payload in tries:
  try:
   if typ=='multipart': rr=s.post(ep,files={'file':('social-media-growth.html',article,'text/html')},timeout=30)
   elif typ=='json': rr=s.post(ep,json=payload,timeout=30)
   else: rr=s.post(ep,data=payload,headers={'Content-Type':'text/html'},timeout=30)
   print('POST',typ,ep,rr.status_code,rr.text[:1400])
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
  except Exception as e: print('POST_ERR',typ,ep,repr(e))
