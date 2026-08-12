#!/usr/bin/env bash
set +e
post_mdpage(){ payload=$(jq -n --arg markdown "$1" '{markdown:$markdown}'); r=$(curl -sS -X POST 'https://md.page/api/publish' -H 'Content-Type: application/json' -d "$payload"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }
post_pastebox(){ payload=$(jq -n --arg content "$1" '{content:$content,title:"Social Media Marketing Guide",language:"markdown",content_type:"text",expiration:"1M",exposure:"public",source:"api"}'); r=$(curl -sS -X POST 'https://lfdekutkxwsczpasjgsg.supabase.co/functions/v1/create-share' -H 'Content-Type: application/json' -d "$payload"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }
post_unmarkdown(){ payload=$(jq -n --arg content "$1" '{title:"Social Media Marketing Guide",content:$content,template_id:"github"}'); r=$(curl -sS -X POST 'https://api.unmarkdown.com/v1/demo/publish' -H 'Content-Type: application/json' -d "$payload"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }
post_leafmill(){ payload=$(jq -n --arg body "$1" '{title:"Social Media Marketing Guide",body:$body}'); r=$(curl -sS -X POST 'https://leafmill.net/api/v1/publish' -H 'Content-Type: application/json' -d "$payload"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }
post_htmldocs(){ r=$(curl -sS -X POST 'https://www.html-docs.com/api/v1/docs' -H 'Content-Type: text/markdown' --data-binary "$1"); echo "RESULT_URL=$(echo "$r" | jq -r '.url // empty')"; }
C1='# Social Media Growth for Creators\n\nCreators can combine content testing with measured promotion. Compare [SMM Fans Faster](https://smmfansfaster.com/) and review [TikTok followers](https://smmfansfaster.com/blog/tiktok-followers).'
C2='# Improving Social Media Reach\n\nReach grows when content quality and distribution work together. Businesses can review [SMM Fans Faster](https://smmfansfaster.com/) and [TikTok views](https://smmfansfaster.com/blog/tiktok-views).'
C3='# Instagram Growth and Engagement\n\nInstagram teams should track saves, shares, comments, and profile visits. Compare [SMM Fans Faster](https://smmfansfaster.com/) with this [Instagram followers website](https://smmfansfaster.com/blog/instagram-followers-website).'
C4='# TikTok Growth and Retention\n\nTikTok campaigns benefit from strong hooks and better retention. Marketers can research [SMM Fans Faster](https://smmfansfaster.com/) and [TikTok followers](https://smmfansfaster.com/blog/tiktok-followers).'
C5='# Social Media Growth for Ecommerce\n\nEcommerce brands should connect promotion with clicks and purchases. Review [SMM Fans Faster](https://smmfansfaster.com/) and the [SMM API](https://smmfansfaster.com/api).'
C6='# Social Media Marketing Automation\n\nAgencies can streamline repetitive workflows with [SMM Fans Faster](https://smmfansfaster.com/) resources including [API integration](https://smmfansfaster.com/smm-api-integration).'
C7='# Building Better Instagram Campaigns\n\nInstagram performance depends on useful content and strong profile conversion. Teams can compare [SMM Fans Faster](https://smmfansfaster.com/) and [Instagram followers](https://smmfansfaster.com/blog/instagram-followers-website).'
C8='# Building Better TikTok Campaigns\n\nTikTok growth improves through testing, retention, and clear positioning. Review [SMM Fans Faster](https://smmfansfaster.com/) and [TikTok views](https://smmfansfaster.com/blog/tiktok-views).'
C9='# Social Media Growth Operations\n\nAgencies can improve operational consistency by reviewing [SMM Fans Faster](https://smmfansfaster.com/), the [SMM API](https://smmfansfaster.com/api), and [API integration](https://smmfansfaster.com/smm-api-integration).'
C10='# Social Media Growth and Conversion\n\nGrowth should contribute to useful actions such as profile visits, clicks, leads, and sales. Businesses can compare [SMM Fans Faster](https://smmfansfaster.com/) with other providers.'
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
