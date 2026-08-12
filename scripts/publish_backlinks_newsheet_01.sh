#!/usr/bin/env bash
set +e
cat >/tmp/backlink.html <<'EOF'
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Social Media Growth Strategy: Content, Analytics and Promotion</title></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.8;color:#171717"><h1>Social Media Growth Strategy: Content, Analytics and Promotion</h1><p>Reliable social media growth depends on the interaction between content quality, audience research, publishing consistency, analytics, conversion planning, and carefully selected promotional support.</p><p>Teams comparing external providers can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a broader review. Useful factors include platform coverage, delivery expectations, minimum orders, support, refill conditions, cancellation options, and campaign fit.</p><h2>TikTok growth</h2><p>Marketers can review resources about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a>, <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views, followers, and likes</a>, and the <a href="https://smmfansfaster.com/blog/numberoftiktokfollowers">number of TikTok followers</a>. These visible metrics should be compared with retention, saves, shares, comments, and profile activity.</p><h2>Instagram growth</h2><p>Instagram teams can review this guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a>, plus discussions about whether <a href="https://smmfansfaster.com/ar/blog/doesincreasingyourfollowersaffecttheinstagramalgorithmfindoutnow">increasing followers affects the Instagram algorithm</a> and whether <a href="https://smmfansfaster.com/ar/blog/doesbuyinginstagramfollowersaffectengagement">buying Instagram followers affects engagement</a>.</p><h2>Measurement and automation</h2><p>Campaign dashboards should separate awareness, engagement, conversion, and revenue. Agencies and resellers can also review the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and the <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> page when evaluating automation workflows.</p><p>The strongest long-term approach improves the complete path from discovery to action instead of maximizing one visible number in isolation.</p></main></body></html>
EOF

# Verify the already-created ShareDuo artifact using the public preview convention.
for SD_URL in 'https://preview.shareduo.com/xs9d9q6' 'https://preview.shareduo.com/xs9d9q6/' ; do
 code=$(curl -sS -L -o /tmp/sd-live.html -w '%{http_code}' "$SD_URL")
 echo "SHAREDUO_VERIFY=$code $SD_URL"
 if [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/sd-live.html; then echo "RESULT_URL=$SD_URL"; break; fi
done

# PagePaste — correct multipart field reading file contents.
PP_RESP=$(curl -sS -L -D /tmp/pp-headers.txt 'https://pagepaste.com/' -F 'html=</tmp/backlink.html' -F 'title=Social Media Growth Strategy')
printf '%s' "$PP_RESP" >/tmp/pp-response.html
echo 'PAGEPASTE_HEADERS_START'; grep -Ei '^(location|content-location):' /tmp/pp-headers.txt | tail -5; echo 'PAGEPASTE_HEADERS_END'
# Look for result/share URLs, excluding static assets.
PP_URL=$(grep -Eo 'https://pagepaste\.com/[A-Za-z0-9][A-Za-z0-9/_-]{2,}' /tmp/pp-response.html | grep -Ev '(assets|images|icons|manifest|cdn|blog|privacy|terms)' | sort -u | tail -1)
if [ -z "$PP_URL" ]; then
 loc=$(grep -Ei '^location:' /tmp/pp-headers.txt | tail -1 | sed -E 's/^[Ll]ocation:[[:space:]]*//;s/\r$//')
 [[ "$loc" == /* ]] && PP_URL="https://pagepaste.com$loc"
 [[ "$loc" == https://pagepaste.com/* ]] && PP_URL="$loc"
fi
echo "PAGEPASTE_CANDIDATE=$PP_URL"
if [[ "$PP_URL" == https://pagepaste.com/* ]]; then
 code=$(curl -sS -L -o /tmp/pp-live.html -w '%{http_code}' "$PP_URL")
 if [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/pp-live.html; then echo "RESULT_URL=$PP_URL"; else echo "PAGEPASTE_VERIFY_FAILED=$code"; fi
fi
