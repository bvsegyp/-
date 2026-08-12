#!/usr/bin/env bash
set +e
FINAL='https://api.draftlet.io/api/v1/publish/azure-river-5084/finalize'
BODY='{"versionId":"ver_01KZTDPKN5R8DAPV04J84D8TB9","editToken":"-5WqsT0ko1_Kt1NfurmB6zbRbdYhfhd_"}'
RESP=$(curl -sS -X POST "$FINAL" -H 'Content-Type: application/json' --data-binary "$BODY")
echo "DRAFTLET_FINALIZE=$RESP"
URL=$(python3 -c 'import json,sys; d=json.load(sys.stdin); print(d.get("url", ""))' <<< "$RESP" 2>/dev/null)
[ -z "$URL" ] && URL='https://azure-river-5084.draftlet.io'
code=$(curl -sS -L -o /tmp/draftlet-live.html -w '%{http_code}' "$URL")
echo "DRAFTLET_VERIFY=$code $URL"
if [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/draftlet-live.html; then echo "RESULT_URL=$URL"; fi
