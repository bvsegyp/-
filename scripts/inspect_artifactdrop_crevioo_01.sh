#!/usr/bin/env bash
set +e
python3 - <<'PY'
import re,requests
from urllib.parse import urljoin
sites=[('https://drops.0xhome.dev/','ArtifactDrop'),('https://crevioo.com/','Crevioo')]
for base,name in sites:
 print('===',name,base,'===')
 try:
  h=requests.get(base,timeout=20,allow_redirects=True).text
  print('HOME_LEN',len(h))
  for ep in sorted(set(re.findall(r'["\'](/(?:api|v1|v2)/[^"\'<> ]+)["\']',h))): print('HOME_EP',ep)
  scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',h,re.I)
  print('SCRIPT_COUNT',len(scripts))
  for s in scripts[:40]:
   try:
    u=urljoin(base,s); t=requests.get(u,timeout=12).text
    for ep in sorted(set(re.findall(r'["\'](/(?:api|v1|v2)/[^"\'<> ]+)["\']',t))): print('JS_EP',ep)
    for m in re.finditer(r'(?:fetch|axios\.(?:post|request))\((.{0,1400})',t):
     z=m.group(0)
     if any(x in z.lower() for x in ['post','publish','upload','artifact','page']): print('CALL',z[:1400].replace('\n',' '))
   except Exception: pass
 except Exception as e: print('ERR',repr(e))
PY
