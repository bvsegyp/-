#!/usr/bin/env bash
set +e
python3 - <<'PY'
import re,requests
from urllib.parse import urljoin
for base,path in [('https://pagelive.io','/tools/publish-html'),('https://fylo.host','/html-viewer-online')]:
 print('===',base,'===')
 try:
  h=requests.get(base+path,timeout=20).text
  print('HOME_LEN',len(h))
  scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',h,re.I)
  for s in scripts[:30]:
   try:
    u=urljoin(base+'/',s); t=requests.get(u,timeout=12).text
    for m in re.finditer(r'(?:fetch|axios\.(?:post|request))\((.{0,1200})',t):
     z=m.group(0)
     if any(x in z.lower() for x in ['post','/api/','publish','upload']): print('CALL',z[:1200].replace('\n',' '))
    for ep in sorted(set(re.findall(r'["\'](/(?:api|v1)/[^"\' ]+)["\']',t))): print('EP',ep)
   except Exception: pass
 except Exception as e: print('ERR',e)
PY
