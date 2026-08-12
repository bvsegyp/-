import requests,re
base='https://pagepaste.com/'
html='''<!doctype html><html><head><meta charset="utf-8"><title>Social Media Growth Strategy Across TikTok and Instagram</title></head><body><main style="max-width:900px;margin:40px auto;font-family:Arial,sans-serif;line-height:1.8;padding:0 22px"><h1>Social Media Growth Strategy Across TikTok and Instagram</h1><p>Effective social media growth usually combines strong content, clear audience targeting, consistent publishing, analytics, and carefully selected promotional support. The most useful campaigns define their goal first, then match every tactic to that goal.</p><p>Businesses comparing external support can review <a href="https://smmfansfaster.com/">SMM Fans Faster</a> alongside other providers and compare platform coverage, service details, support, order conditions, and campaign fit.</p><h2>TikTok growth</h2><p>TikTok growth depends heavily on hooks, retention, repeatable creative formats, and audience relevance. Teams can also review resources about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a> while tracking watch time, shares, profile visits, and conversions.</p><h2>Instagram growth</h2><p>For Instagram, marketers should balance Reels, carousels, and Stories while keeping the profile clear and conversion-focused. This guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> can be considered as one part of a wider growth plan.</p><h2>Automation for agencies</h2><p>Agencies managing larger campaign volumes can study the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> resources. Automation works best when orders are still checked for the correct target, quantity, and service before submission.</p><p>Long-term results come from combining useful content, measurement, promotion, and conversion optimization instead of focusing on a single visible metric.</p></main></body></html>'''
s=requests.Session()
r=s.post(base,data={'html':html,'title':'Social Media Growth Strategy Across TikTok and Instagram'},timeout=30,allow_redirects=True)
print('POST_STATUS',r.status_code)
print('FINAL_URL',r.url)
print('BODY_LEN',len(r.text))
# Prefer explicit published URL embedded by the PHP response.
patterns=[r'PUBLISHED_URL\s*=\s*["\']([^"\']+)',r'https://[A-Za-z0-9.-]*pagepaste\.com/[A-Za-z0-9_./?=-]+']
urls=[]
for p in patterns:
    urls += re.findall(p,r.text,re.I)
if r.url.rstrip('/') != base.rstrip('/'):
    urls.insert(0,r.url)
seen=[]
for u in urls:
    if u not in seen: seen.append(u)
print('CANDIDATES',seen[:20])
for u in seen:
    try:
        v=s.get(u,timeout=30)
        ok=v.status_code<400 and 'smmfansfaster.com' in v.text.lower()
        print('VERIFY',u,v.status_code,ok)
        if ok:
            print('RESULT_URL='+u)
            break
    except Exception as e:
        print('VERIFY_ERR',u,repr(e))
