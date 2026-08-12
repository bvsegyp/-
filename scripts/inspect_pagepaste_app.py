import requests,re
u='https://pagepaste.com/app.js'
t=requests.get(u,timeout=30).text
print('LEN',len(t))
for pat in [r'fetch\([^\n]{0,1000}',r'XMLHttpRequest[^\n]{0,1000}',r'axios[^\n]{0,1000}',r'https?://[^"\'\s)]+',r'/api/[A-Za-z0-9_./?=&-]+']:
 print('PATTERN',pat)
 seen=set()
 for m in re.finditer(pat,t,re.I):
  s=m.group(0)
  if s not in seen:
   seen.add(s); print(s[:1200])
