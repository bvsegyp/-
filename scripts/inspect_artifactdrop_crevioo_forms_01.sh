#!/usr/bin/env bash
set +e
python3 - <<'PY'
import requests,re
from html.parser import HTMLParser
for url in ['https://drops.0xhome.dev/','https://crevioo.com/']:
 print('\n===',url,'===')
 h=requests.get(url,timeout=20).text
 class P(HTMLParser):
  def handle_starttag(self,tag,attrs):
   d=dict(attrs)
   if tag in ('form','input','textarea','button','select'): print(tag,d)
 P().feed(h)
 for pat in [r'/api/[A-Za-z0-9_./?=&-]+',r'/v1/[A-Za-z0-9_./?=&-]+',r'https?://[^"\'<> ]+']:
  vals=[]
  for x in re.findall(pat,h):
   if any(k in x.lower() for k in ['api','upload','publish','drop','create','artifact']): vals.append(x)
  for x in list(dict.fromkeys(vals))[:30]: print('HIT',x)
 print('SNIPPETS')
 for key in ['curl','POST','multipart','application/json','formData','upload','publish']:
  i=h.lower().find(key.lower())
  if i>=0: print(key,h[max(0,i-400):i+1000].replace('\n',' ')[:1400])
PY
