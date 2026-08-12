#!/usr/bin/env bash
set +e
for host in 'https://paste.page/free-html-hosting' 'https://htmldrop.app/' 'https://publishto.us/'; do
  echo "=== HOST $host ==="
  curl -sS -L "$host" > /tmp/site.html
  python3 - <<'PY'
from html.parser import HTMLParser
import re, os
s=open('/tmp/site.html',encoding='utf-8',errors='ignore').read()
class P(HTMLParser):
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='form': print('FORM',d)
        if tag in ('input','textarea','button','select'): print('FIELD',tag,d)
        if tag=='script' and d.get('src'): print('SCRIPT',d['src'])
P().feed(s)
for pat in [r'fetch\(([^\n]{0,400})',r'axios\.[a-z]+\(([^\n]{0,400})',r'/(?:api|v1)/[A-Za-z0-9_./?=&-]+',r'https://[^"\' ]+/(?:api|v1)/[^"\' ]+']:
    vals=re.findall(pat,s,re.I)
    for v in vals[:30]: print('HIT',pat,v[:500])
PY
  grep -Eo 'src="[^"]+\.js[^" ]*"' /tmp/site.html | sed 's/^src="//;s/"$//' | head -20 >/tmp/jslist
  while read -r src; do
    [ -z "$src" ] && continue
    case "$src" in
      http*) u="$src" ;;
      //*) u="https:$src" ;;
      /*)
        base=$(echo "$host" | sed -E 's#(https?://[^/]+).*#\1#')
        u="$base$src" ;;
      *)
        base=$(echo "$host" | sed -E 's#(https?://[^/]+).*#\1#')
        u="$base/$src" ;;
    esac
    echo "JSURL=$u"
    curl -sS -L "$u" | grep -Eo '.{0,180}(fetch\(|/api/|/v1/|publish|upload).{0,300}' | head -20 || true
  done </tmp/jslist
done
