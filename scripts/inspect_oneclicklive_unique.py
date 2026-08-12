import requests,re,json
from urllib.parse import urljoin
base='https://oneclicklive.app/en'
s=requests.Session(); r=s.get(base,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
assets=[]
for pat in [r'<script[^>]+src=["\']([^"\']+)',r'<link[^>]+href=["\']([^"\']+\.js[^"\']*)']:
 for m in re.finditer(pat,r.text,re.I):
  u=urljoin(r.url,m.group(1))
  if u not in assets: assets.append(u)
print('ASSET_COUNT',len(assets))
for u in assets:
 try:t=s.get(u,timeout=30).text
 except Exception as e: print('ERR',u,repr(e)); continue
 print('ASSET',u,len(t))
 for pat in [r'fetch\([^\n]{0,1500}',r'axios\.post\([^\n]{0,1500}',r'["\'](/api/[A-Za-z0-9_./?=&${}-]+)["\']',r'https://[^"\'\s`]+']:
  seen=set()
  for m in re.finditer(pat,t,re.I):
   z=m.group(0)
   if any(k in z.lower() for k in ['deploy','publish','project','site','upload','api']):
    if z not in seen: seen.add(z); print('MATCH',z[:1600])
