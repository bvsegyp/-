#!/usr/bin/env bash
set +e
cat >/tmp/draftlet.html <<'EOF'
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>How to Build a Better Social Media Growth System</title></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.8;color:#171717"><h1>How to Build a Better Social Media Growth System</h1><p>A strong social media growth system connects useful content, audience research, consistent publishing, analytics, profile optimization, conversion planning, and carefully selected promotional support.</p><p>Businesses comparing external providers can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a wider review of social media marketing services. Useful comparison factors include platform coverage, delivery expectations, order minimums, support, refill conditions, cancellation options, and campaign fit.</p><h2>Use clear goals</h2><p>Awareness campaigns may focus on reach and views. Engagement campaigns can track watch time, saves, shares, and comments. Conversion campaigns should connect social activity to profile visits, website clicks, inquiries, leads, purchases, and revenue.</p><h2>TikTok growth</h2><p>Marketers can review guides about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a>, <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views, followers, and likes</a>, and the <a href="https://smmfansfaster.com/blog/numberoftiktokfollowers">number of TikTok followers</a>. Visible growth is most useful when evaluated alongside retention and interaction quality.</p><h2>Instagram growth</h2><p>Instagram teams can review this guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a>, along with discussions about whether <a href="https://smmfansfaster.com/ar/blog/doesincreasingyourfollowersaffecttheinstagramalgorithmfindoutnow">increasing followers affects the Instagram algorithm</a> and whether <a href="https://smmfansfaster.com/ar/blog/doesbuyinginstagramfollowersaffectengagement">buying Instagram followers affects engagement</a>.</p><h2>Automation and measurement</h2><p>Agencies can review the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and the <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> page while designing workflows. Automation should support careful campaign management rather than replace human review.</p><p>The strongest long-term approach improves the full path from discovery to action rather than maximizing a single visible metric.</p></main></body></html>
EOF
SIZE=$(wc -c </tmp/draftlet.html | tr -d ' ')
CREATE=$(python3 -c 'import json,os; print(json.dumps({"files":[{"path":"index.html","contentType":"text/html","size":int(os.environ["SIZE"])}]}))' SIZE="$SIZE" 2>/dev/null)
# construct JSON reliably
CREATE=$(SIZE="$SIZE" python3 -c 'import json,os; print(json.dumps({"files":[{"path":"index.html","contentType":"text/html","size":int(os.environ["SIZE"])}]}))')
RESP=$(curl -sS -X POST 'https://api.draftlet.io/api/v1/publish' -H 'content-type: application/json' --data-binary "$CREATE")
echo "DRAFTLET_CREATE=$RESP"
UPLOAD=$(python3 -c 'import json,sys; d=json.load(sys.stdin); u=d.get("uploads") or []; print(u[0].get("uploadUrl","") if u else "")' <<< "$RESP" 2>/dev/null)
FINAL=$(python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("finalizeUrl", ""))' <<< "$RESP" 2>/dev/null)
LIVE=$(python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("url", ""))' <<< "$RESP" 2>/dev/null)
if [ -n "$UPLOAD" ]; then
  curl -sS -X PUT "$UPLOAD" -H 'Content-Type: text/html' -H "Content-Length: $SIZE" --data-binary @/tmp/draftlet.html >/tmp/draftlet-upload.out
  echo "DRAFTLET_UPLOAD_DONE=1"
fi
if [[ "$FINAL" == /* ]]; then FINAL="https://api.draftlet.io$FINAL"; fi
if [ -n "$FINAL" ]; then
  FRESP=$(curl -sS -X POST "$FINAL" -H 'Content-Type: application/json' -d '{}')
  echo "DRAFTLET_FINALIZE=$FRESP"
  FURL=$(python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("url", ""))' <<< "$FRESP" 2>/dev/null)
  [ -n "$FURL" ] && LIVE="$FURL"
fi
if [[ "$LIVE" == https://*.draftlet.io* ]]; then
  code=$(curl -sS -L -o /tmp/draftlet-live.html -w '%{http_code}' "$LIVE")
  if [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/draftlet-live.html; then echo "RESULT_URL=$LIVE"; else echo "DRAFTLET_VERIFY_FAILED=$code $LIVE"; fi
fi
