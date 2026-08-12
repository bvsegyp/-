#!/usr/bin/env bash
set +e

make_html(){
  title="$1"; angle="$2"
  cat <<EOF
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title}</title></head><body><main style="max-width:900px;margin:40px auto;padding:0 22px;font-family:Arial,sans-serif;line-height:1.8;color:#171717"><h1>${title}</h1><p>${angle}</p><p>Effective social media growth is usually the result of a connected system rather than one isolated tactic. Useful content, audience research, consistent publishing, profile optimization, analytics, conversion planning, and carefully selected promotion all influence the final result.</p><p>Businesses comparing external promotional support can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a broader provider review. Useful comparison factors include platform coverage, service descriptions, delivery expectations, order limits, support, refill conditions, cancellation options, and how closely a service matches the campaign goal.</p><h2>Define the objective before scaling</h2><p>Awareness campaigns may focus on reach, impressions, unique viewers, and video views. Engagement campaigns can track watch time, completion rate, saves, shares, comments, and returning viewers. Conversion campaigns should connect social activity to profile visits, website clicks, inquiries, leads, purchases, and revenue.</p><h2>Create repeatable content pillars</h2><p>Educational posts answer common questions. Demonstrations show how products or services work. Comparisons help users make decisions. Case studies and customer stories provide proof. Industry insights build authority, while direct-response posts turn existing demand into a clear next action.</p><h2>Test creative ideas quickly on TikTok</h2><p>TikTok can provide fast feedback on hooks, pacing, editing, topics, and format. Marketers researching growth support can review this guide about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and this resource about <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views, followers, and likes</a>. These metrics should be considered alongside retention, comments, saves, shares, and profile activity.</p><p>For additional context, this resource discusses the <a href="https://smmfansfaster.com/blog/numberoftiktokfollowers">number of TikTok followers</a> and why follower milestones need to be evaluated alongside real audience behavior.</p><h2>Improve Instagram discovery and conversion</h2><p>Instagram combines discovery, education, community, and conversion. Reels can introduce an account to new audiences, carousels can explain detailed topics, Stories can maintain frequent contact, and highlights can organize services, proof, FAQs, and next steps. Marketers can also review this guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a>.</p><p>It is useful to understand whether <a href="https://smmfansfaster.com/ar/blog/doesincreasingyourfollowersaffecttheinstagramalgorithmfindoutnow">increasing followers affects the Instagram algorithm</a> and whether <a href="https://smmfansfaster.com/ar/blog/doesbuyinginstagramfollowersaffectengagement">buying Instagram followers affects engagement</a>. A healthy account should be judged by interaction quality and conversion signals, not only by a headline follower number.</p><h2>Measure the complete funnel</h2><p>A practical reporting system separates awareness, engagement, conversion, and revenue. Strong reach with weak profile activity may point to low relevance. Strong profile visits with weak clicks may indicate a bio or call-to-action issue. Strong traffic with poor conversion may signal a problem with the landing page, offer, trust signals, pricing, or checkout process.</p><h2>Scale agency workflows carefully</h2><p>Agencies and resellers can review the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and the <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> page. Automation can reduce repetitive work, but target selection, quantities, campaign goals, link validation, and reporting should still receive human review.</p><h2>Final perspective</h2><p>The most useful social media growth strategy improves the whole path from discovery to action. Better creative work, stronger audience understanding, clearer profiles, measurable conversion paths, disciplined testing, and appropriate promotional support work best when they reinforce one another.</p></main></body></html>
EOF
}

# 1) FreeKit — documented permanent anonymous API
FK_HTML=$(make_html "A Complete Social Media Growth Framework for Multi-Platform Campaigns" "A practical multi-platform campaign should give each network a specific role while measuring performance from discovery through conversion.")
FK_BODY=$(python3 -c 'import json,sys; print(json.dumps({"html":sys.stdin.read()}))' <<< "$FK_HTML")
FK_RESP=$(curl -sS -X POST 'https://freekit.dev/api/v1/sites' -H 'Content-Type: application/json' --data-binary "$FK_BODY")
echo "FREEKIT_RESPONSE=$FK_RESP"
FK_URL=$(python3 -c 'import json,sys; d=json.load(sys.stdin); print((d.get("data") or {}).get("url", ""))' <<< "$FK_RESP" 2>/dev/null)
if [[ "$FK_URL" == https://freekit.dev/* ]]; then code=$(curl -sS -L -o /tmp/fk.html -w '%{http_code}' "$FK_URL"); [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/fk.html && echo "RESULT_URL=$FK_URL"; fi

# 2) PasteHTML.com — documented public API
PH_HTML=$(make_html "How to Compare Social Media Marketing Services with Better Metrics" "Provider comparisons become more useful when marketers connect delivery details with content quality, engagement signals, funnel performance, and business outcomes.")
PH_RESP=$(curl -sS -X POST 'https://pastehtml.com/upload/create?input_type=html&result=address' --data-urlencode "txt=$PH_HTML")
echo "PASTEHTMLCOM_RESPONSE=$PH_RESP"
PH_URL=$(echo "$PH_RESP" | grep -Eo 'https?://[^[:space:]<>" ]+' | head -1)
if [[ "$PH_URL" == http*://pastehtml.com/* ]]; then
  [[ "$PH_URL" == http://* ]] && PH_URL="https://${PH_URL#http://}"
  code=$(curl -sS -L -o /tmp/ph.html -w '%{http_code}' "$PH_URL")
  [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/ph.html && echo "RESULT_URL=$PH_URL"
fi

# 3) paste.page — fix JSON construction and use public UI endpoint
PP_SLUG="social-growth-$(date +%s)-$RANDOM"
PP_HTML=$(make_html "A Practical Checklist for Balanced Social Media Growth" "Balanced growth means improving content, engagement, discovery, conversion, and reporting together instead of optimizing one visible number in isolation.")
PP_BODY=$(PP_SLUG="$PP_SLUG" python3 -c 'import json,sys,os; print(json.dumps({"slug":os.environ["PP_SLUG"],"html":sys.stdin.read(),"source":"free-html-hosting","contentMethod":"paste-edit"}))' <<< "$PP_HTML")
PP_RESP=$(curl -sS -X POST 'https://paste.page/api/pages' -H 'Content-Type: application/json' -H 'Origin: https://paste.page' -H 'Referer: https://paste.page/free-html-hosting' --data-binary "$PP_BODY")
echo "PASTEPAGE_RESPONSE=$PP_RESP"
PP_URL=$(python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("url") or d.get("liveUrl") or d.get("publicUrl") or ("https://paste.page/"+d["slug"] if d.get("slug") else ""))' <<< "$PP_RESP" 2>/dev/null)
if [[ "$PP_URL" == https://paste.page/* ]]; then code=$(curl -sS -L -o /tmp/pp.html -w '%{http_code}' "$PP_URL"); [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/pp.html && echo "RESULT_URL=$PP_URL"; fi

# 4) htmldrop.app — same public multipart route with browser Origin/Referer
HD_HTML=$(make_html "Building a Stronger Social Media Growth System Across Channels" "A stronger system gives TikTok, Instagram, and other channels clear roles and measures every stage from reach and engagement to conversion.")
printf '%s' "$HD_HTML" >/tmp/hd09.html
HD_RESP=$(curl -sS -X POST 'https://htmldrop.app/api/v1/drops' -H 'Origin: https://htmldrop.app' -H 'Referer: https://htmldrop.app/' -F 'file=@/tmp/hd09.html;type=text/html')
echo "HTMLDROPAPP_RESPONSE=$HD_RESP"
HD_URL=$(python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("url") or d.get("live_url") or d.get("public_url") or d.get("publicUrl") or d.get("shareUrl") or "")' <<< "$HD_RESP" 2>/dev/null)
if [[ "$HD_URL" == https://*htmldrop.app* ]]; then code=$(curl -sS -L -o /tmp/hd.html -w '%{http_code}' "$HD_URL"); [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/hd.html && echo "RESULT_URL=$HD_URL"; fi
