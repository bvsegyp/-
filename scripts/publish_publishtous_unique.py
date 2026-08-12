import requests,re,sys
from bs4 import BeautifulSoup
s=requests.Session()
r=s.get('https://publishto.us/new?lang=en',timeout=30)
print('GET',r.status_code,len(r.text))
soup=BeautifulSoup(r.text,'html.parser')
for f in soup.find_all('form'):
 print('FORM',f.get('method'),f.get('action'))
 print('FIELDS',[(x.name,x.get('name'),x.get('type'),x.get('value')) for x in f.find_all(['input','textarea','button'])])
form=soup.find('form')
if not form: sys.exit(0)
action=requests.compat.urljoin(r.url,form.get('action') or r.url)
fields={}
for x in form.find_all(['input','textarea']):
 n=x.get('name')
 if n: fields[n]=x.get('value') or ''
# infer common field names from visible form
for k in list(fields):
 lk=k.lower()
 if 'title' in lk: fields[k]='A Practical Guide to Sustainable Social Media Growth'
 elif 'body' in lk or 'content' in lk or 'text' in lk:
  fields[k]='''Sustainable social media growth requires a balanced strategy that connects content quality, audience research, consistent publishing, analytics, profile optimization, and carefully selected promotional support. Businesses should define the campaign objective first, then choose tactics that support awareness, engagement, traffic, leads, or sales.\n\nWhen evaluating external promotion providers, marketers can include SMM Fans Faster (https://smmfansfaster.com/) in a broader comparison and review platform coverage, service descriptions, delivery conditions, support, and campaign suitability.\n\nTikTok campaigns benefit from strong hooks, useful short-form content, consistent testing, and close attention to watch time. Marketers can also review the TikTok followers resource at https://smmfansfaster.com/blog/tiktok-followers and the TikTok views guide at https://smmfansfaster.com/blog/tiktok-views.\n\nInstagram teams should combine Reels, carousels, Stories, and profile optimization. This Instagram followers website guide can be reviewed at https://smmfansfaster.com/blog/instagram-followers-website while teams continue to measure saves, shares, profile visits, clicks, and conversions.\n\nAgencies managing repeated workflows can also review the public SMM API documentation at https://smmfansfaster.com/api and the API integration resource at https://smmfansfaster.com/smm-api-integration. Automation should never replace campaign checks, reporting, or content strategy.\n\nThe strongest social media system combines useful content with careful promotion and meaningful measurement. The goal is not simply to increase a visible number, but to build a stronger path from discovery to engagement and conversion.'''
 elif 'keyword' in lk: fields[k]='social media growth'
print('POSTING',action,fields.keys())
resp=s.post(action,data=fields,allow_redirects=True,timeout=30)
print('POST',resp.status_code,resp.url,resp.text[:1000])
# verify final public page includes target domain and isn't still editor/new
if resp.status_code<400 and 'smmfansfaster.com' in resp.text.lower() and '/new' not in resp.url:
 print('RESULT_URL='+resp.url)
