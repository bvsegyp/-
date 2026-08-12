#!/usr/bin/env bash
set +e
curl -sS 'https://yourtext.host/' > /tmp/yourtext.html
python3 - <<'PY'
from html.parser import HTMLParser
class P(HTMLParser):
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if tag=='form': print('FORM',d)
        if tag in ('input','textarea','button','select'):
            print('FIELD',tag,d)
P().feed(open('/tmp/yourtext.html',encoding='utf-8',errors='ignore').read())
PY
