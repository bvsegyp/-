import requests

html='''<!doctype html><html><head><meta charset="utf-8"><title>How to Build a Sustainable Social Media Growth System</title></head><body><main style="max-width:900px;margin:40px auto;font-family:Arial,sans-serif;line-height:1.8;padding:0 22px"><h1>How to Build a Sustainable Social Media Growth System</h1><p>Long-term social media growth works best when content, audience research, publishing consistency, analytics, and promotion support one another. Teams should start with a clear objective such as awareness, profile visits, leads, or sales, then choose the right mix of tactics for that objective.</p><p>Businesses comparing promotional providers can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in their research and review service coverage, delivery expectations, support, order conditions, and campaign fit.</p><h2>TikTok campaign planning</h2><p>For TikTok, stronger hooks and repeatable formats are essential. Marketers can also review resources about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a> while tracking watch time, shares, profile visits, and conversions.</p><h2>Instagram campaign planning</h2><p>Instagram campaigns benefit from a balanced mix of Reels, carousels, and Stories. This guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> can be considered alongside organic content improvements and profile optimization.</p><h2>Automation and measurement</h2><p>Agencies managing larger volumes can study the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> resources. Any automation process should still include checks for target URLs, quantities, and campaign suitability.</p><p>The strongest growth system measures meaningful outcomes rather than relying on follower count alone.</p></main></body></html>'''

for name,url in [('FREEKIT','https://freekit.dev/api/v1/sites'),('PAGEDROP','https://pagedrop.dev/api/v1/sites')]:
    try:
        r=requests.post(url,json={'html':html},timeout=30)
        print(f'{name}_STATUS={r.status_code}')
        print(f'{name}_RESPONSE={r.text[:1500]}')
        if r.ok:
            d=r.json()
            u=(d.get('data') or {}).get('url') or d.get('url')
            if u and u.startswith('https://'):
                v=requests.get(u,timeout=30)
                ok=('smmfansfaster.com' in v.text.lower()) and v.status_code < 400
                print(f'{name}_VERIFY={v.status_code} backlink={ok}')
                if ok:
                    print('RESULT_URL='+u)
    except Exception as e:
        print(f'{name}_ERROR={e!r}')
