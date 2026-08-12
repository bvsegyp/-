import requests,re,sys
from urllib.parse import urljoin
base='https://fylo.host/html-viewer-online'
s=requests.Session()
r=s.get(base,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',r.text,re.I)
print('SCRIPTS',scripts)
cands=[]
for src in scripts:
 try:
  u=urljoin(r.url,src); t=s.get(u,timeout=30).text; print('SCRIPT',u,len(t))
  for pat in [r'fetch\(\s*[`"\']([^`"\']+)',r'axios\.post\(\s*[`"\']([^`"\']+)',r'["\'](/api/[A-Za-z0-9_./?=&${}-]+)["\']',r'["\'](https://[^"\']+/(?:api|publish|upload|deploy)[^"\']*)["\']']:
   for m in re.finditer(pat,t,re.I):
    x=m.group(1)
    if any(k in x.lower() for k in ['publish','upload','deploy','site','html','api']):
     x=urljoin('https://fylo.host/',x)
     if x not in cands: cands.append(x); print('CANDIDATE',x)
 except Exception as e: print('SCRIPT_ERR',src,repr(e))
article='''<!doctype html><html><head><meta charset="utf-8"><title>How to Plan Multi-Platform Social Media Growth</title></head><body><main style="max-width:900px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.85"><h1>How to Plan Multi-Platform Social Media Growth</h1><p>Social media growth becomes more reliable when brands connect content strategy, audience research, analytics, profile optimization, and carefully selected promotion. The first step is to define a measurable objective such as awareness, engagement, traffic, leads, or sales.</p><h2>Compare providers by campaign fit</h2><p>Businesses researching promotional support can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a broader provider comparison and evaluate platform coverage, service information, delivery expectations, support, and suitability for the campaign.</p><h2>TikTok strategy</h2><p>TikTok teams can improve performance by testing stronger hooks, pacing, formats, and posting consistency. Supporting research can include guides about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a>. Important metrics include watch time, completion rate, shares, profile visits, and conversions.</p><h2>Instagram strategy</h2><p>Instagram marketers can combine Reels, carousels, Stories, and profile optimization. This resource about an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> can be reviewed alongside organic engagement and conversion data.</p><h2>Agency automation</h2><p>For agencies managing repeated workflows, the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> resource can help with technical evaluation. Automation should still include campaign checks and reporting.</p><p>The strongest long-term approach keeps content quality, promotion, analytics, and conversion working together instead of relying on a single visible metric.</p></main></body></html>'''
for ep in cands:
 # only first-party endpoint discovered from frontend
 if 'fylo.host' not in ep and 'fylo.live' not in ep: continue
 payloads=[{'html':article,'subdomain':'social-growth-guide'}, {'content':article,'slug':'social-growth-guide'}, {'htmlContent':article,'name':'social-growth-guide'}]
 for payload in payloads:
  try:
   rr=s.post(ep,json=payload,timeout=30); print('POST',ep,rr.status_code,rr.text[:1500])
   if not rr.ok: continue
   try:d=rr.json()
   except: continue
   vals=[]
   def walk(o):
    if isinstance(o,dict):
     for k,v in o.items():
      if k.lower() in ('url','publicurl','public_url','shareurl','share_url','liveurl','live_url','link') and isinstance(v,str): vals.append(v)
      walk(v)
    elif isinstance(o,list):
     for v in o: walk(v)
   walk(d)
   for u in vals:
    if not u.startswith('http'): u=urljoin('https://fylo.host/',u)
    try:
     v=s.get(u,timeout=30); ok=v.status_code<400 and 'smmfansfaster.com' in v.text.lower(); print('VERIFY',u,v.status_code,ok)
     if ok: print('RESULT_URL='+u); sys.exit(0)
    except Exception as e: print('VERIFY_ERR',u,repr(e))
  except Exception as e: print('POST_ERR',ep,repr(e))
