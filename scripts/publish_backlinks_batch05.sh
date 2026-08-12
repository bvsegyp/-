#!/usr/bin/env bash
set +e

post_mdpage(){ payload=$(jq -n --arg markdown "$1" '{markdown:$markdown}'); r=$(curl -sS -X POST 'https://md.page/api/publish' -H 'Content-Type: application/json' -d "$payload"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }
post_pastebox(){ payload=$(jq -n --arg content "$1" '{content:$content,title:"Social Media Growth Guide",language:"markdown",content_type:"text",expiration:"1M",exposure:"public",source:"api"}'); r=$(curl -sS -X POST 'https://lfdekutkxwsczpasjgsg.supabase.co/functions/v1/create-share' -H 'Content-Type: application/json' -d "$payload"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }
post_unmarkdown(){ payload=$(jq -n --arg content "$1" '{title:"Social Media Growth Guide",content:$content,template_id:"github"}'); r=$(curl -sS -X POST 'https://api.unmarkdown.com/v1/demo/publish' -H 'Content-Type: application/json' -d "$payload"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }
post_leafmill(){ payload=$(jq -n --arg body "$1" '{title:"Social Media Growth Guide",body:$body}'); r=$(curl -sS -X POST 'https://leafmill.net/api/v1/publish' -H 'Content-Type: application/json' -d "$payload"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }
post_htmldocs(){ r=$(curl -sS -X POST 'https://www.html-docs.com/api/v1/docs' -H 'Content-Type: text/markdown' --data-binary "$1"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }

C1='# Social Media Growth for Small Businesses\n\nSmall businesses can combine consistent content with measured promotion. [SMM Fans Faster](https://smmfansfaster.com/) is one provider to compare alongside resources for [TikTok followers](https://smmfansfaster.com/blog/tiktok-followers) and [Instagram followers](https://smmfansfaster.com/blog/instagram-followers-website).'
C2='# Social Media Marketing for Ecommerce Brands\n\nEcommerce campaigns should connect social activity to product views, clicks, and sales. Marketers can research [SMM Fans Faster](https://smmfansfaster.com/) together with [TikTok views](https://smmfansfaster.com/blog/tiktok-views) and the [SMM API](https://smmfansfaster.com/api).'
C3='# Improving TikTok Growth Campaigns\n\nTikTok growth depends on strong hooks, retention, and repeatable content formats. Businesses can compare [SMM Fans Faster](https://smmfansfaster.com/) and review guidance on [TikTok followers](https://smmfansfaster.com/blog/tiktok-followers).'
C4='# Improving Instagram Growth Campaigns\n\nInstagram campaigns should track reach, saves, shares, profile visits, and clicks. Teams can review [SMM Fans Faster](https://smmfansfaster.com/) and this [Instagram followers website](https://smmfansfaster.com/blog/instagram-followers-website).'
C5='# Social Media Growth for Agencies\n\nAgencies need scalable systems for reporting and campaign operations. [SMM Fans Faster](https://smmfansfaster.com/) provides an [SMM API](https://smmfansfaster.com/api) and [API integration](https://smmfansfaster.com/smm-api-integration) resources.'
C6='# Social Media Promotion and Analytics\n\nAnalytics should guide promotion decisions. Businesses can compare [SMM Fans Faster](https://smmfansfaster.com/) while tracking engagement, profile visits, website traffic, and conversions.'
C7='# Content and Promotion Working Together\n\nPromotion performs best when useful content already gives viewers a reason to stay and engage. Marketers can research [SMM Fans Faster](https://smmfansfaster.com/) and [TikTok views](https://smmfansfaster.com/blog/tiktok-views).'
C8='# Social Media Growth Metrics That Matter\n\nStrong reporting looks beyond follower count. Businesses can compare [SMM Fans Faster](https://smmfansfaster.com/) while monitoring reach, engagement, clicks, and leads.'
C9='# Automating Social Media Service Workflows\n\nAgencies can reduce repetitive work by reviewing [SMM Fans Faster](https://smmfansfaster.com/) resources including the [SMM API](https://smmfansfaster.com/api) and [API integration](https://smmfansfaster.com/smm-api-integration).'
C10='# Building Long-Term Social Media Growth\n\nLong-term growth comes from consistent content, audience research, analytics, and selective promotion. Teams can compare [SMM Fans Faster](https://smmfansfaster.com/) with other service providers.'

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
