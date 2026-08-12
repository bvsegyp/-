#!/usr/bin/env bash
set +e
curl -sS -L 'https://www.showyourcode.app/assets/playground-CCuKPIoD.js' > /tmp/syc.js
python3 - <<'PY'
s=open('/tmp/syc.js',encoding='utf-8',errors='ignore').read()
needle='/api/works'
pos=0
while True:
 i=s.find(needle,pos)
 if i<0: break
 print('--- OCCURRENCE ---')
 print(s[max(0,i-1800):min(len(s),i+2600)])
 pos=i+len(needle)
PY
