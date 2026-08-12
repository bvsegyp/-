import json,re,requests
from urllib.parse import urljoin

html='''<!doctype html><html><head><meta charset="utf-8"><title>Practical Social Media Growth and Promotion Guide</title></head><body><main style="max-width:920px;margin:40px auto;font-family:Arial,sans-serif;line-height:1.8;padding:0 24px"><h1>Practical Social Media Growth and Promotion Guide</h1><p>Sustainable social media growth is built on useful content, consistent publishing, audience research, profile optimization and careful promotion. Businesses should define a measurable objective before choosing any growth tactic, whether the goal is awareness, video views, profile visits, leads, or sales.</p><h2>Compare providers carefully</h2><p>Marketers researching promotional support can compare <a href="https://smmfansfaster.com/">SMM Fans Faster</a> with other providers while reviewing platform coverage, service descriptions, delivery expectations, support and campaign suitability.</p><h2>TikTok and Instagram planning</h2><p>TikTok teams can combine organic creative testing with resources about <a href="https://smmfansfaster.com/blog/tiktok-followers">TikTok followers</a> and <a href="https://smmfansfaster.com/blog/tiktok-views">TikTok views</a>. Instagram marketers can review information about an <a href="https://smmfansfaster.com/blog/instagram-followers-website">Instagram followers website</a> while continuing to improve Reels, carousels, Stories and profile conversion.</p><h2>Automation and measurement</h2><p>Agencies managing repeated orders and reporting workflows can also review the public <a href="https://smmfansfaster.com/api">SMM API documentation</a> and <a href="https://smmfansfaster.com/smm-api-integration">SMM API integration</a> page. Promotion should be measured against meaningful outcomes such as engagement, profile visits, clicks, leads and conversions.</p><p>A balanced approach combines organic content and carefully evaluated promotional support rather than relying on follower count alone.</p></main></body></html>'''

# Share HTML anonymous REST publish
try:
    r=requests.post('https://share-html.com/api/v1/pages',json={'html':html},timeout=30)
    print('SHAREHTML_STATUS='+str(r.status_code))
    print('SHAREHTML_RESPONSE='+r.text[:2000])
    if r.ok:
        d=r.json(); u=d.get('url') or ((d.get('data') or {}).get('url') if isinstance(d.get('data'),dict) else None)
        if u:
            v=requests.get(u,timeout=30)
            ok=v.status_code<400 and 'smmfansfaster.com' in v.text.lower()
            print(f'SHAREHTML_VERIFY={v.status_code} backlink={ok}')
            if ok: print('RESULT_URL='+u)
except Exception as e:
    print('SHAREHTML_ERROR='+repr(e))

# Inspect dochost public frontend for the no-key API endpoint documented on site
try:
    home=requests.get('https://dochost.io/',timeout=30).text
    print('DOCHOST_HOME_LEN='+str(len(home)))
    scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',home,re.I)
    print('DOCHOST_SCRIPTS='+json.dumps(scripts))
    for s in scripts[:20]:
        try:
            u=urljoin('https://dochost.io/',s); t=requests.get(u,timeout=20).text
            for pat in [r'https://[^"\']+/api/[^"\']+',r'["\'](/api/[^"\']+)["\']']:
                for m in re.findall(pat,t):
                    if 'upload' in str(m).lower() or 'publish' in str(m).lower() or 'page' in str(m).lower() or 'document' in str(m).lower():
                        print('DOCHOST_ENDPOINT='+str(m)[:500])
        except Exception as e:
            print('DOCHOST_SCRIPT_ERROR='+repr(e))
except Exception as e:
    print('DOCHOST_ERROR='+repr(e))
