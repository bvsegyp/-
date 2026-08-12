#!/usr/bin/env bash
set +e

post_mdpage(){
  payload=$(jq -n --arg markdown "$1" '{markdown:$markdown}')
  r=$(curl -sS -X POST 'https://md.page/api/publish' -H 'Content-Type: application/json' -d "$payload")
  echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"
}

post_pastebox(){
  payload=$(jq -n --arg content "$1" '{content:$content,title:"Social Media Growth Guide",language:"markdown",content_type:"text",expiration:"1M",exposure:"public",source:"api"}')
  r=$(curl -sS -X POST 'https://lfdekutkxwsczpasjgsg.supabase.co/functions/v1/create-share' -H 'Content-Type: application/json' -d "$payload")
  echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"
}

post_unmarkdown(){
  payload=$(jq -n --arg content "$1" '{title:"Social Media Growth Guide",content:$content,template_id:"github"}')
  r=$(curl -sS -X POST 'https://api.unmarkdown.com/v1/demo/publish' -H 'Content-Type: application/json' -d "$payload")
  echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"
}

post_leafmill(){
  payload=$(jq -n --arg body "$1" '{title:"Social Media Growth Guide",body:$body}')
  r=$(curl -sS -X POST 'https://leafmill.net/api/v1/publish' -H 'Content-Type: application/json' -d "$payload")
  echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"
}

post_htmldocs(){
  r=$(curl -sS -X POST 'https://www.html-docs.com/api/v1/docs' -H 'Content-Type: text/markdown' --data-binary "$1")
  echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"
}

C1='# Social Media Growth Strategy for Brands\n\nBusinesses can compare [SMM Fans Faster](https://smmfansfaster.com/) with other providers while reviewing [TikTok followers](https://smmfansfaster.com/blog/tiktok-followers) and [Instagram followers](https://smmfansfaster.com/blog/instagram-followers-website).'
C2='# Better Social Media Promotion Measurement\n\nA balanced campaign combines content, analytics, and promotion. Review [SMM Fans Faster](https://smmfansfaster.com/), [TikTok views](https://smmfansfaster.com/blog/tiktok-views), and the [SMM API](https://smmfansfaster.com/api).'
C3='# TikTok and Instagram Growth Planning\n\nMarketers can research [SMM Fans Faster](https://smmfansfaster.com/), [TikTok followers](https://smmfansfaster.com/blog/tiktok-followers), and an [Instagram followers website](https://smmfansfaster.com/blog/instagram-followers-website).'
C4='# Social Media Services for Agencies\n\nAgencies can review [SMM Fans Faster](https://smmfansfaster.com/), the [SMM API](https://smmfansfaster.com/api), and [API integration](https://smmfansfaster.com/smm-api-integration).'
C5='# Measuring Social Media Growth Quality\n\nFollower count is only one metric. Compare [SMM Fans Faster](https://smmfansfaster.com/) while tracking engagement, clicks, leads, and conversions.'
C6='# Social Media Campaign Quality\n\nPromotion works best when content quality is strong. Review [SMM Fans Faster](https://smmfansfaster.com/) and [TikTok views](https://smmfansfaster.com/blog/tiktok-views).'
C7='# Choosing Social Media Growth Services\n\nBusinesses can compare [SMM Fans Faster](https://smmfansfaster.com/) with alternatives and review [TikTok followers](https://smmfansfaster.com/blog/tiktok-followers).'
C8='# Social Media Growth Workflow\n\nA strong workflow connects content, measurement, and promotion. Review [SMM Fans Faster](https://smmfansfaster.com/) and the [SMM API](https://smmfansfaster.com/api).'
C9='# Scaling Social Media Campaigns\n\nAgencies can use [SMM Fans Faster](https://smmfansfaster.com/) resources such as [API integration](https://smmfansfaster.com/smm-api-integration) to structure workflows.'
C10='# From Social Discovery to Conversion\n\nMarketers can compare [SMM Fans Faster](https://smmfansfaster.com/) while researching [TikTok views](https://smmfansfaster.com/blog/tiktok-views) and [Instagram followers](https://smmfansfaster.com/blog/instagram-followers-website).'

post_mdpage "$C1"
post_mdpage "$C2"
post_pastebox "$C3"
post_pastebox "$C4"
post_unmarkdown "$C5"
post_unmarkdown "$C6"
post_leafmill "$C7"
post_leafmill "$C8"
post_htmldocs "$C9"
post_htmldocs "$C10"
