#!/usr/bin/env bash
set +e
python3 - <<'PY'
import requests,re
from urllib.parse import urljoin
base='https://crevioo.com/'
h=requests.get(base,timeout=20).text
scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',h,re.I)
print('SCRIPTS',scripts)
for s in scripts:
 u=urljoin(base,s)
 t=requests.get(u,timeout=20).text
 print('BUNDLE',u,'LEN',len(t))
 for needle in ['supabase','functions/v1','from("pages")','from(\'pages\')','insert(','generate','createPage','published_pages','pages']:
  p=t.lower().find(needle.lower())
  if p>=0: print('NEEDLE',needle,t[max(0,p-1200):p+2600].replace('\n',' ')[:3800])
 for x in sorted(set(re.findall(r'https://[a-z0-9.-]+\.supabase\.co[^"\' ]*',t,re.I))): print('SUPABASE_URL',x)
 for x in sorted(set(re.findall(r'["\'](/(?:api|functions|v1)/[^"\' ]+)["\']',t))): print('EP',x)
PY
