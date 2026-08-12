#!/usr/bin/env bash
set +e
curl -sS -L 'https://www.showyourcode.app/playground' > /tmp/syc.html
JS=$(grep -Eo 'src="[^"]+\.js[^"]*"' /tmp/syc.html | sed 's/^src="//;s/"$//' | grep '/assets/' | head -1)
case "$JS" in http*) URL="$JS";; /*) URL="https://www.showyourcode.app$JS";; *) URL="https://www.showyourcode.app/$JS";; esac
echo "SYC_JS=$URL"
curl -sS -L "$URL" > /tmp/syc.js
python3 - <<'PY'
import re
s=open('/tmp/syc.js',encoding='utf-8',errors='ignore').read()
for pat in [r'fetch\([^)]{0,800}\)',r'axios\.[a-zA-Z]+\([^)]{0,800}\)',r'["\'`](/api/[^"\'`]+)["\'`]',r'["\'`]([^"\'`]*(?:share|publish|snippet|playground)[^"\'`]*)["\'`]']:
    print('PATTERN',pat)
    vals=re.findall(pat,s,re.I|re.S)
    for v in vals[:80]:
        if isinstance(v,tuple): v=' '.join(v)
        print(str(v)[:1200].replace('\n',' '))
PY
