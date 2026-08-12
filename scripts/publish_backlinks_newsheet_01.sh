#!/usr/bin/env bash
set +e

make_html(){
  title="$1"
  angle="$2"
  cat <<EOF
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title}</title></head><body><main style="max-width:900px;margin:40px auto;padding:0 22px;font-family:Arial,sans-serif;line-height:1.8;color:#171717"><h1>${title}</h1><p>${angle}</p><p>Strong social media growth usually comes from combining useful content, audience research, consistent publishing, analytics, profile optimization, conversion planning, and carefully selected promotional support. A campaign becomes easier to evaluate when the business defines its main goal before scaling activity.</p><p>Teams comparing external providers can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a wider review of available social media marketing services. Useful comparison points include platform coverage, service descriptions, delivery expectations, order minimums, refill terms, cancellation options, support availability, and whether a service matches the campaign objective.</p><h2>Start with measurable business outcomes</h2><p>Awareness campaigns can track reach, impressions, unique viewers, and video views. Engagement campaigns can focus on watch time, completion rate, saves, shares, comments, and returning viewers. Conversion campaigns should connect social activity to profile visits, website clicks, inquiries, leads, purchases, and revenue. Recording a baseline before scaling makes later analysis more reliable.</p><h2>Build repeatable content pillars</h2><p>Educational posts can answer recurring customer questions. Demonstrations can show how a product or service works. Comparisons can help users make decisions. Case studies and customer stories can strengthen trust, while industry insights can improve authority. Direct-response content can then convert existing demand into a clear next step.</p><h2>Use TikTok as a creative testing channel</h2><p>TikTok gives marketers fast feedback on hooks, pacing, editing, topics, and format. Marketers researching audience-growth support can review this guide about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and this resource about <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views, followers, and likes</a>. Those numbers are most useful when considered alongside retention, comments, shares, saves, and profile activity.</p><p>It can also help to review information about the <a href="https://smmfansfaster.com/blog/numberoftiktokfollowers">number of TikTok followers</a>. Follower milestones may contribute to social proof, but they should not replace useful content, audience relevance, or a strong conversion path.</p><h2>Improve Instagram discovery and conversion together</h2><p>Instagram combines discovery, education, community, and conversion. Reels can introduce an account to new audiences, carousels can explain detailed topics, Stories can maintain regular contact, and highlights can organize services, proof, FAQs, and next steps. Marketers can review this guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> while comparing follower-focused options.</p><p>It is also useful to study whether <a href="https://smmfansfaster.com/ar/blog/doesincreasingyourfollowersaffecttheinstagramalgorithmfindoutnow">increasing followers affects the Instagram algorithm</a> and whether <a href="https://smmfansfaster.com/ar/blog/doesbuyinginstagramfollowersaffectengagement">buying Instagram followers affects engagement</a>. The key is to evaluate follower growth alongside real interaction signals rather than judging account health from one visible number.</p><h2>Measure the full funnel</h2><p>A useful dashboard separates awareness, engagement, conversion, and revenue. Strong reach with weak profile activity can indicate low relevance. Strong profile visits with weak clicks can point to the bio or call to action. Strong traffic with poor conversion can signal a problem with the landing page, offer, trust signals, pricing, or checkout process.</p><h2>Use automation carefully at scale</h2><p>Agencies and resellers can review the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and the <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> page. Automation can reduce repetitive work, but target selection, quantity checks, campaign objectives, link validation, and reporting should still receive human review.</p><h2>Final perspective</h2><p>Sustainable social media growth is a system rather than a single tactic. The strongest campaigns improve the complete path from discovery to action: better creative work, stronger audience understanding, clearer profiles, measurable conversion paths, and disciplined testing of promotional support.</p></main></body></html>
EOF
}

# 1) Pitchey — official anonymous JSON endpoint
PIT_HTML=$(make_html "A Practical Framework for Sustainable Social Media Growth" "A sustainable growth system should connect content quality, audience intent, measurement, conversion design, and carefully selected promotion instead of chasing one headline metric.")
PIT_BODY=$(python3 -c 'import json,sys; print(json.dumps({"html":sys.stdin.read(),"ttl":"30d"}))' <<< "$PIT_HTML")
PIT_RESP=$(curl -sS -X POST 'https://pitchey.app/api/pages' -H 'Content-Type: application/json' --data-binary "$PIT_BODY")
echo "PITCHEY_RESPONSE=$PIT_RESP"
PIT_URL=$(python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("url", ""))' <<< "$PIT_RESP" 2>/dev/null)
if [[ "$PIT_URL" == https://pitchey.app/* ]]; then
  code=$(curl -sS -L -o /tmp/pit-live.html -w '%{http_code}' "$PIT_URL")
  if [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/pit-live.html; then echo "RESULT_URL=$PIT_URL"; fi
fi

# 2) paste.page — anonymous page creation path used by public UI
PP_SLUG="social-growth-$(date +%s)-$RANDOM"
PP_HTML=$(make_html "How to Evaluate Social Media Growth Services Without Losing Sight of Strategy" "Growth services work best when they support an existing content and analytics system. The practical question is not whether a single metric rises, but whether the complete marketing funnel becomes stronger.")
PP_BODY=$(python3 -c 'import json,sys,os; print(json.dumps({"slug":os.environ["PP_SLUG"],"html":sys.stdin.read(),"source":"free-html-hosting","contentMethod":"paste-edit"}))' <<< "$PP_HTML")
PP_RESP=$(PP_SLUG="$PP_SLUG" curl -sS -X POST 'https://paste.page/api/pages' -H 'Content-Type: application/json' --data-binary "$PP_BODY")
echo "PASTEPAGE_RESPONSE=$PP_RESP"
PP_URL=$(python3 - <<'PY' <<< "$PP_RESP"
import json,sys
try:
 d=json.load(sys.stdin)
 for k in ('url','liveUrl','publicUrl'):
  if isinstance(d.get(k),str): print(d[k]); raise SystemExit
 slug=d.get('slug')
 if slug: print('https://paste.page/'+slug)
except: pass
PY
)
if [[ "$PP_URL" == https://paste.page/* ]]; then
  code=$(curl -sS -L -o /tmp/pp-live.html -w '%{http_code}' "$PP_URL")
  if [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/pp-live.html; then echo "RESULT_URL=$PP_URL"; fi
fi

# 3) htmldrop.app — anonymous multipart endpoint used by public UI
HD_HTML=$(make_html "Building a Multi-Platform Social Media Growth System" "A multi-platform strategy becomes stronger when each channel has a defined role and performance is measured across discovery, engagement, conversion, and revenue.")
printf '%s' "$HD_HTML" >/tmp/htmldrop-batch08.html
HD_RESP=$(curl -sS -X POST 'https://htmldrop.app/api/v1/drops' -F 'file=@/tmp/htmldrop-batch08.html;type=text/html')
echo "HTMLDROPAPP_RESPONSE=$HD_RESP"
HD_URL=$(python3 - <<'PY' <<< "$HD_RESP"
import json,sys
try:
 d=json.load(sys.stdin)
 for k in ('url','live_url','public_url','publicUrl','shareUrl'):
  if isinstance(d.get(k),str): print(d[k]); raise SystemExit
 slug=d.get('slug')
 if slug: print('https://'+slug+'.htmldrop.app')
except: pass
PY
)
if [[ "$HD_URL" == https://*htmldrop.app* ]]; then
  code=$(curl -sS -L -o /tmp/hd-live.html -w '%{http_code}' "$HD_URL")
  if [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/hd-live.html; then echo "RESULT_URL=$HD_URL"; fi
fi
