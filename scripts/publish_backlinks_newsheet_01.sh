#!/usr/bin/env bash
set +e
for host in 'https://www.showyourcode.app/playground' 'https://pagepaste.com/' 'https://oneclicklive.app/en' 'https://www.shareduo.com/'; do
  echo "=== HOST $host ==="
  base=$(echo "$host" | sed -E 's#(https?://[^/]+).*#\1#')
  curl -sS -L "$host" > /tmp/site.html
  python3 - <<'PY'
from html.parser import HTMLParser
import re
s=open('/tmp/site.html',encoding='utf-8',errors='ignore').read()
class P(HTMLParser):
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='form': print('FORM',d)
        if tag in ('input','textarea','button','select'): print('FIELD',tag,d)
        if tag=='script' and d.get('src'): print('SCRIPT',d['src'])
P().feed(s)
for pat in [r'fetch\(([^\n]{0,500})',r'axios\.[a-z]+\(([^\n]{0,500})',r'/(?:api|v1)/[A-Za-z0-9_./?=&:-]+']:
  for v in re.findall(pat,s,re.I)[:50]: print('HIT',pat,v[:700])
PY
  grep -Eo 'src="[^"]+\.js[^" ]*"' /tmp/site.html | sed 's/^src="//;s/"$//' | head -30 >/tmp/jslist
  while read -r src; do
    [ -z "$src" ] && continue
    case "$src" in http*) u="$src";; //*) u="https:$src";; /*) u="$base$src";; *) u="$base/$src";; esac
    echo "JSURL=$u"
    curl -sS -L "$u" | grep -Eo '.{0,220}(fetch\(|axios\.|/api/|/v1/|share|publish|deploy|upload).{0,420}' | head -40 || true
  done </tmp/jslist
done
