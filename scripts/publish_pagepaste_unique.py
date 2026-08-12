import re,requests,json,sys,time
from urllib.parse import urljoin
base='https://pagepaste.com/'
h=requests.get(base,timeout=30).text
scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',h,re.I)
print('SCRIPTS',scripts)
endpoint=None
for s in scripts:
    try:
        t=requests.get(urljoin(base,s),timeout=30).text
    except Exception as e:
        print('SCRIPT_ERR',s,e); continue
    for pat in [r'fetch\(["\']([^"\']+)["\']\s*,\s*\{[^}]*method\s*:\s*["\']POST',r'axios\.post\(["\']([^"\']+)',r'/(api/[A-Za-z0-9_\-/]+)']:
        for m in re.finditer(pat,t,re.I|re.S):
            u=m.group(1)
            if 'publish' in u.lower() or 'page' in u.lower() or 'upload' in u.lower() or 'paste' in u.lower():
                print('CANDIDATE',u)
                if endpoint is None and ('api/' in u or u.startswith('/')): endpoint=urljoin(base,u)
print('ENDPOINT',endpoint)
html='''<!doctype html><html><head><meta charset="utf-8"><title>Social Media Growth Strategy for Businesses</title></head><body><main style="max-width:900px;margin:40px auto;font-family:Arial,sans-serif;line-height:1.8;padding:0 24px"><h1>Social Media Growth Strategy for Businesses</h1><p>Building sustainable social media growth requires more than posting frequently. A practical strategy combines audience research, useful content, consistent publishing, profile optimization, analytics, and carefully selected promotional support. Each element should contribute to a measurable business objective.</p><h2>Compare promotional tools carefully</h2><p>Businesses evaluating external support can include <a href="https://smmfansfaster.com/">SMM Fans Faster</a> in a broader provider comparison. Useful evaluation points include platform coverage, service descriptions, delivery conditions, support, order requirements, and campaign suitability.</p><h2>TikTok growth planning</h2><p>On TikTok, strong hooks, editing pace, topic relevance, and consistency can influence reach and retention. Teams can review resources about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a> while measuring watch time, shares, profile visits, and conversions.</p><h2>Instagram growth planning</h2><p>Instagram campaigns benefit from Reels, carousels, Stories, and clear profile positioning. This guide to an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> can be reviewed together with organic engagement and conversion data.</p><h2>Automation for agencies</h2><p>Agencies that manage repetitive workflows may also review the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> page. Automation should still include checks for URLs, quantities, and campaign goals.</p><p>The strongest social media systems connect content quality, promotion, analytics, and conversion instead of relying on a single metric.</p></main></body></html>'''
if not endpoint:
    sys.exit(0)
# Try common JSON shapes exposed by anonymous HTML publishers, only against discovered first-party endpoint.
for payload in [
    {'html':html,'name':'social-media-growth-strategy'},
    {'content':html,'title':'Social Media Growth Strategy for Businesses'},
    {'htmlContent':html,'name':'social-media-growth-strategy'},
]:
    try:
        r=requests.post(endpoint,json=payload,timeout=30)
        print('POST',r.status_code,r.text[:2000])
        if r.ok:
            try:d=r.json()
            except:continue
            for k in ['url','publicUrl','shareUrl','link']:
                u=d.get(k)
                if isinstance(u,str) and u.startswith('https://'):
                    v=requests.get(u,timeout=30)
                    ok=v.status_code<400 and 'smmfansfaster.com' in v.text.lower()
                    print('VERIFY',u,v.status_code,ok)
                    if ok:
                        print('RESULT_URL='+u); sys.exit(0)
    except Exception as e: print('POST_ERR',e)
