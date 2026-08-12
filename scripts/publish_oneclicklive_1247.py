import requests
base='https://oneclicklive.app'
html='''<!doctype html><html><head><meta charset="utf-8"><title>Social Media Growth: Content, Promotion and Measurement</title></head><body><main style="max-width:900px;margin:40px auto;font-family:Arial,sans-serif;line-height:1.8;padding:0 22px"><h1>Social Media Growth: Content, Promotion and Measurement</h1><p>Successful social media growth is usually built from several connected activities: useful content, audience research, consistent publishing, analytics, conversion planning, and selective promotional support. Brands should define the business goal before increasing activity so they can judge whether a tactic is actually producing value.</p><p>When comparing promotional providers, marketers can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in their research and evaluate platform coverage, service details, delivery expectations, support, and campaign suitability.</p><h2>TikTok planning</h2><p>TikTok teams should test hooks, retention, editing pace, and creative formats. Resources covering <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a> can be reviewed alongside organic performance metrics such as watch time, shares, comments, and profile visits.</p><h2>Instagram planning</h2><p>Instagram growth often requires a mix of Reels, carousels, Stories, and profile optimization. Teams can also examine this guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> while improving content quality and conversion paths.</p><h2>Agency operations</h2><p>For agencies, the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> resources provide information about connecting service and order workflows. Automated processes should still include checks for the correct target URL, service, and quantity.</p><p>A balanced growth system tracks meaningful outcomes instead of relying on a single headline number.</p></main></body></html>'''
s=requests.Session()
r=s.post(base+'/api/deploy',json={'code':html,'title':'Social Media Growth: Content, Promotion and Measurement'},timeout=40)
print('POST_STATUS',r.status_code)
print('POST_BODY',r.text[:3000])
if r.ok:
    try:
        d=r.json()
    except Exception:
        d={}
    urls=[]
    def walk(x):
        if isinstance(x,dict):
            for k,v in x.items():
                if isinstance(v,str) and v.startswith('http'): urls.append(v)
                else: walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
    walk(d)
    print('CANDIDATES',urls)
    for u in urls:
        try:
            v=s.get(u,timeout=40)
            ok=v.status_code<400 and 'smmfansfaster.com' in v.text.lower()
            print('VERIFY',u,v.status_code,ok,len(v.text))
            if ok:
                print('RESULT_URL='+u)
                break
        except Exception as e: print('VERIFY_ERR',u,repr(e))
