import requests
base='https://www.showyourcode.app'
html='''<!doctype html><html><head><meta charset="utf-8"><title>A Practical Framework for Multi-Platform Social Media Growth</title></head><body><main style="max-width:900px;margin:40px auto;font-family:Arial,sans-serif;line-height:1.8;padding:0 22px"><h1>A Practical Framework for Multi-Platform Social Media Growth</h1><p>A sustainable social media strategy combines useful content, audience research, consistent publishing, analytics, and carefully selected promotional support. The first step is defining the business outcome: awareness, profile activity, leads, conversions, or sales.</p><p>Teams researching promotional services can compare providers such as <a href="https://smmfansfaster.com/">SMM Fans Faster</a> based on platform coverage, service descriptions, delivery expectations, support, and campaign fit rather than choosing only by price.</p><h2>TikTok growth strategy</h2><p>On TikTok, creative quality and retention remain central. Strong hooks, short editing cycles, and repeatable formats should be tested alongside resources about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a>. Marketers should compare follower growth with watch time, shares, profile visits, and conversion activity.</p><h2>Instagram growth strategy</h2><p>Instagram campaigns benefit from a balanced mix of Reels, carousels, Stories, profile optimization, and clear calls to action. Teams can review this guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> while continuing to improve organic creative quality.</p><h2>Agency automation</h2><p>For agencies managing multiple accounts, the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> resources describe options for connecting ordering and status workflows. Automation should be paired with manual checks for targets, quantities, and campaign suitability.</p><p>The strongest long-term approach combines content, promotion, analytics, and conversion optimization instead of depending on a single visible metric.</p></main></body></html>'''
s=requests.Session()
payload={'htmlContent':html,'title':'A Practical Framework for Multi-Platform Social Media Growth','topicIds':[],'type':'html','templateId':None}
r=s.post(base+'/api/works',json=payload,timeout=30)
print('POST_STATUS',r.status_code)
print('POST_BODY',r.text[:2000])
if r.ok:
    d=r.json(); uuid=d.get('uuid')
    if uuid:
        u=base+'/share/'+uuid
        v=s.get(u,timeout=30)
        ok=v.status_code<400 and 'smmfansfaster.com' in v.text.lower()
        print('VERIFY',v.status_code,'BACKLINK',ok,'LEN',len(v.text))
        if ok: print('RESULT_URL='+u)
