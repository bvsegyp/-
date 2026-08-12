#!/usr/bin/env bash
set +e
URL='https://www.showyourcode.app/assets/playground-CCuKPIoD.js'
curl -sS -L "$URL" > /tmp/syc.js
echo "SYC_JS_SIZE=$(wc -c </tmp/syc.js)"
python3 - <<'PY'
import re
s=open('/tmp/syc.js',encoding='utf-8',errors='ignore').read()
for pat in [r'fetch\((.{0,1000}?)\)',r'axios\.[a-zA-Z]+\((.{0,1000}?)\)',r'(/api/[A-Za-z0-9_./?=&${}-]+)',r'([A-Za-z0-9_./-]*(?:snippet|share|publish)[A-Za-z0-9_./?=&${}-]*)']:
 print('PATTERN',pat)
 seen=[]
 for m in re.findall(pat,s,re.I|re.S):
  v=m if isinstance(m,str) else ' '.join(m)
  v=v.replace('\n',' ')
  if v not in seen:
   seen.append(v); print(v[:1600])
  if len(seen)>=100: break
PY
