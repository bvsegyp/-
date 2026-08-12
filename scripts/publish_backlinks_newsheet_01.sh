#!/usr/bin/env bash
set +e
YT='https://yourtext.host/2026/08/How-to-Build-a-Sustainable-Social-Media-Growth-Strategy'
code=$(curl -sS -o /tmp/yt-live.html -w '%{http_code}' "$YT")
if [ "$code" = "200" ] && grep -q 'smmfansfaster.com' /tmp/yt-live.html; then echo "RESULT_URL=$YT"; else echo "YOURTEXT_VERIFY_FAILED=$code"; fi

curl -sSI 'https://mira.cagdas.io/' > /tmp/mira.headers
cat /tmp/mira.headers | grep -i 'x-llm-spec\|content-type\|location' || true
spec=$(awk -F': ' 'tolower($1)=="x-llm-spec"{gsub("\r","");print $2}' /tmp/mira.headers | tail -1)
echo "MIRA_SPEC_URL=$spec"
if [ -n "$spec" ]; then
  case "$spec" in
    http*) url="$spec" ;;
    /*) url="https://mira.cagdas.io$spec" ;;
    *) url="https://mira.cagdas.io/$spec" ;;
  esac
  curl -sS "$url" | head -c 30000
  echo
fi
