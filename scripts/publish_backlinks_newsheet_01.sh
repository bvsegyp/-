#!/usr/bin/env bash
set +e
curl -sS 'https://yourtext.host/' > /tmp/yourtext.html
python3 - <<'PY'
import re
s=open('/tmp/yourtext.html',encoding='utf-8',errors='ignore').read()
for pat in [r'function\s+formSubmit\s*\([^)]*\)\s*\{.*?\}',r'check[^;\n]{0,300}',r'publish[^;\n]{0,300}']:
    print('PATTERN',pat)
    for m in re.findall(pat,s,re.S|re.I)[:20]: print(m[:2000])
for src in re.findall(r'<script[^>]+src=["\']([^"\']+)',s,re.I): print('SCRIPT_SRC',src)
PY
