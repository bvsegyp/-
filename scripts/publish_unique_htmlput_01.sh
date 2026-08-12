#!/usr/bin/env bash
set +e
cat >/tmp/article.html <<'EOF'
<!doctype html><html><head><meta charset="utf-8"><title>Social Media Growth Services and Campaign Measurement</title></head><body><main style="max-width:900px;margin:40px auto;font-family:Arial,sans-serif;line-height:1.8;padding:0 22px"><h1>Social Media Growth Services and Campaign Measurement</h1><p>A successful social media growth plan connects content quality, audience research, publishing consistency, analytics, profile optimization, and promotional support. Businesses should define a measurable objective before increasing activity.</p><p>Teams comparing providers can review <a href="https://smmfansfaster.com/">SMM Fans Faster</a> alongside other services and compare platform coverage, delivery expectations, support, and campaign fit.</p><h2>TikTok growth</h2><p>Marketers can review resources covering <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a> while testing stronger hooks, pacing, formats, and topics. Retention, saves, shares, comments, and profile visits provide useful context beyond headline metrics.</p><h2>Instagram growth</h2><p>Instagram campaigns can combine Reels, carousels, Stories, and profile optimization while researching an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a>. Engagement and website actions should remain part of the evaluation.</p><h2>Agency workflows</h2><p>Agencies can also review the <a href="https://smmfansfaster.com/api">SMM API</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> resources when considering automation. A balanced workflow keeps content, promotion, analytics, and conversion aligned.</p></main></body></html>
EOF
curl -LsS --max-time 25 https://www.htmlput.com/ -o /tmp/home.html
python3 - <<'PY'
import re,requests
from urllib.parse import urljoin
h=open('/tmp/home.html',errors='ignore').read()
print('HTMLPUT_HOME',len(h))
for s in re.findall(r'<script[^>]+src=["\']([^"\']+)',h,re.I):
 try:
  u=urljoin('https://www.htmlput.com/',s); t=requests.get(u,timeout=12).text
  for m in re.finditer(r'(?:fetch|axios\.(?:post|request))\((.{0,1200})',t):
   z=m.group(0)
   if 'POST' in z or '/api/' in z or 'upload' in z.lower() or 'host' in z.lower(): print('HTMLPUT_CALL='+z[:1200].replace('\n',' '))
 except Exception as e: pass
PY
