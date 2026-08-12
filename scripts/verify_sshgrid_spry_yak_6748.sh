#!/usr/bin/env bash
set +e
STATUS='https://sshgrid.com/api/v1/sites/spry-yak-6748'
for i in $(seq 1 15); do
 resp=$(curl -sS --max-time 15 "$STATUS")
 echo "SSHGRID_STATUS_$i=$resp"
 live=$(printf '%s' "$resp" | python3 -c 'import sys,json; d=json.load(sys.stdin); print(d.get("url_live") or (d.get("url") if d.get("overall") in ("ready","live","done") else "") or "")' 2>/dev/null)
 if [[ "$live" == https://* ]]; then
  code=$(curl -sS -L --max-time 20 -o /tmp/live.html -w '%{http_code}' "$live")
  if [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/live.html; then echo "RESULT_URL=$live"; exit 0; fi
 fi
 sleep 4
done
exit 0
