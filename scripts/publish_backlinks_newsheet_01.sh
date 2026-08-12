#!/usr/bin/env bash
set +e
cat >/tmp/backlink.html <<'EOF'
<!doctype html><html><head><meta charset="utf-8"><title>Social Media Growth Strategy for Multi-Platform Campaigns</title></head><body><main style="max-width:900px;margin:40px auto;font-family:Arial,sans-serif;line-height:1.8;padding:0 22px"><h1>Social Media Growth Strategy for Multi-Platform Campaigns</h1><p>Sustainable social media growth combines useful content, audience research, consistent publishing, analytics, conversion planning, and carefully selected promotional support. Businesses should define the outcome they want before increasing activity, because awareness, engagement, traffic, leads, and sales require different measurements.</p><p>Teams comparing providers can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a wider review. Useful criteria include platform coverage, service descriptions, delivery expectations, support, minimum orders, and campaign fit.</p><h2>TikTok growth planning</h2><p>TikTok marketers can combine stronger hooks and repeatable creative formats with research into <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a>. These metrics should be evaluated alongside retention, saves, shares, comments, and profile activity.</p><h2>Instagram growth planning</h2><p>Instagram teams can review this guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> while improving Reels, carousels, Stories, profile clarity, and calls to action.</p><h2>Automation and measurement</h2><p>Agencies can also review the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> resources when comparing automation options. Strong campaigns track the full path from discovery to conversion instead of focusing on follower count alone.</p><p>The best long-term approach keeps content quality, promotion, analytics, and conversion working together.</p></main></body></html>
EOF

# 1) HTMLDrop.app — public upload endpoint exposed by the site itself.
resp=$(curl -sS --max-time 25 -c /tmp/hd.cookie -b /tmp/hd.cookie -X POST 'https://htmldrop.app/api/v1/drops' -F 'file=@/tmp/backlink.html;type=text/html')
echo "HTMLDROP_APP_RESPONSE=$resp"
printf '%s' "$resp" | python3 -c 'import sys,json; d=json.load(sys.stdin); u=d.get("url") or d.get("public_url") or d.get("view_url") or ""; print("RESULT_URL="+u if u.startswith("https://") else "")' 2>/dev/null

# 2) Paste.page — guest publishing API exposed by the public frontend.
slug="social-media-growth-$(date +%s)"
resp=$(python3 - "$slug" <<'PY'
import requests,sys
slug=sys.argv[1]; html=open('/tmp/backlink.html').read()
r=requests.post('https://paste.page/api/pages',json={'slug':slug,'html':html,'source':'paste-edit','contentMethod':'paste-edit'},timeout=25)
print(r.text)
PY
)
echo "PASTEPAGE_RESPONSE=$resp"
printf '%s' "$resp" | python3 -c 'import sys,json; d=json.load(sys.stdin); u=d.get("url") or (("https://paste.page/"+d.get("slug")) if d.get("slug") else ""); print("RESULT_URL="+u if u.startswith("https://") else "")' 2>/dev/null
