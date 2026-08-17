import requests,re,json,html,secrets
from urllib.parse import urlparse
from bs4 import BeautifulSoup
TARGET='https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'
ANCHOR='أفضل شركة تنظيف في الرياض'
TITLE='أفضل شركة تنظيف في الرياض: دليل عملي لاختيار خدمة موثوقة'

def article():
 return f'''# {TITLE}

اختيار خدمة تنظيف مناسبة في الرياض يحتاج إلى تقييم الجودة والخبرة وطريقة التنفيذ، وليس الاعتماد على السعر أو الإعلان فقط. تختلف احتياجات الشقق والفلل والمكاتب، لذلك من الأفضل معرفة ما يشمله الحجز وطبيعة المعدات والمواد المستخدمة قبل اتخاذ القرار.

## معايير مهمة قبل الحجز

الشركة المحترفة توضح نطاق العمل، وقت الوصول، مدة التنفيذ، وعدد أفراد الفريق المتوقع. كما يجب أن يكون لديها خبرة في التعامل مع أنواع مختلفة من الأرضيات والأثاث والأسطح حتى يتم التنظيف بدون إتلاف الخامات أو ترك آثار مزعجة.

## تنظيف المنازل والفلل

التنظيف الجيد يبدأ بتحديد الأولويات مثل المطابخ والحمامات والمجالس وغرف النوم، ثم الانتقال إلى التفاصيل والزوايا والأسطح. في الفلل والمساحات الكبيرة يصبح تقسيم الفريق وتوزيع المهام عنصرًا مهمًا للحفاظ على الجودة وتقليل الوقت.

## المعدات والمواد المناسبة

المعدات الحديثة تساعد على إزالة الأتربة والبقع بشكل أكثر كفاءة، لكن اختيار مادة التنظيف المناسبة لكل سطح لا يقل أهمية. الرخام والخشب والأقمشة والسجاد تحتاج إلى أساليب مختلفة، والخبرة تقلل احتمالات التلف أو تغير اللون.

## قارن الخدمة وليس السعر فقط

من المفيد مقارنة وضوح الأسعار، سرعة التواصل، تنوع الخدمات، وخيارات التنظيف الإضافية مثل الكنب والسجاد والتعقيم وتنظيف المكاتب. هذه التفاصيل تكشف الفرق بين خدمة منظمة وخدمة تعتمد على التنفيذ السريع فقط.

## الخيار المناسب في الرياض

لمن يبحث عن [{ANCHOR}]({TARGET})، يمكن مراجعة خدمات غيمة ملونة ومقارنة ما تقدمه مع احتياج المنزل أو المكتب قبل الحجز. الاختيار الصحيح يعتمد على توافق الخدمة مع مساحة المكان ونوع التنظيف المطلوب ومستوى العناية بالتفاصيل.

## النتيجة الأفضل تبدأ بالتخطيط

تحديد المطلوب بوضوح قبل وصول الفريق، اختيار الخدمة المناسبة، ومراجعة التفاصيل بعد انتهاء العمل يساعد على الحصول على نتيجة أفضل. عندما تكون خطوات التنفيذ واضحة يصبح التنظيف أكثر كفاءة ويوفر على العميل الوقت والجهد.'''

def md_to_html(md):
 out=[]
 for p in re.split(r'\n\s*\n',md):
  p=p.strip()
  if not p: continue
  if p.startswith('# '): out.append('<h1>'+html.escape(p[2:])+'</h1>'); continue
  if p.startswith('## '): out.append('<h2>'+html.escape(p[3:])+'</h2>'); continue
  parts=[];pos=0
  for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',p):
   parts.append(html.escape(p[pos:m.start()]));parts.append('<a href="'+html.escape(m.group(2),quote=True)+'">'+html.escape(m.group(1))+'</a>');pos=m.end()
  parts.append(html.escape(p[pos:]));out.append('<p>'+''.join(parts)+'</p>')
 return '<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>'+html.escape(TITLE)+'</title></head><body>'+''.join(out)+'</body></html>'

def extract_url(d):
 if isinstance(d,dict):
  for k in ('url','link','shareUrl','share_url','viewerUrl','viewer_url','pageUrl','page_url','siteUrl','site_url','previewUrl','publicUrl','public_url'):
   v=d.get(k)
   if isinstance(v,str) and v.startswith('http'):return v
  for v in d.values():
   u=extract_url(v)
   if u:return u
 if isinstance(d,list):
  for v in d:
   u=extract_url(v)
   if u:return u
 return ''

def verify(name,u):
 if not u:return None
 try:
  r=requests.get(u,timeout=22,allow_redirects=True,headers={'User-Agent':'Mozilla/5.0 ColorfulVerifier/1.0'})
  soup=BeautifulSoup(r.text,'html.parser');hits=0
  for a in soup.find_all('a',href=True):
   if 'colorfulcloudco.com' in a['href'] and ANCHOR in a.get_text(' ',strip=True):hits+=1
  noindex='noindex' in r.headers.get('x-robots-tag','').lower() or bool(soup.find('meta',attrs={'name':re.compile('robots',re.I),'content':re.compile('noindex',re.I)}))
  print('VERIFY',name,r.status_code,r.url,'ANCHORS',hits,'NOINDEX',int(noindex))
  return r.url if r.status_code<400 and hits>0 and not noindex else None
 except Exception as e: print('VERIFY_ERR',name,repr(e));return None

def simple_json(url,payload):
 r=requests.post(url,json=payload,timeout=25,headers={'User-Agent':'Mozilla/5.0 ColorfulSEO/1.0'});print('POST',url,r.status_code,r.text[:200])
 try:return extract_url(r.json()) if r.ok else ''
 except:return ''

def telegraph(md):
 s=requests.Session();acc=s.post('https://api.telegra.ph/createAccount',data={'short_name':'ColorfulCloud','author_name':'Cleaning Guide'},timeout=20).json();tok=(acc.get('result') or {}).get('access_token','');nodes=[]
 for p in re.split(r'\n\s*\n',md):
  p=p.strip()
  if not p:continue
  tag='p';txt=p
  if p.startswith('# '):tag='h3';txt=p[2:]
  elif p.startswith('## '):tag='h4';txt=p[3:]
  ch=[];pos=0
  for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',txt):
   if m.start()>pos:ch.append(txt[pos:m.start()])
   ch.append({'tag':'a','attrs':{'href':m.group(2)},'children':[m.group(1)]});pos=m.end()
  if pos<len(txt):ch.append(txt[pos:])
  nodes.append({'tag':tag,'children':ch})
 d=s.post('https://api.telegra.ph/createPage',data={'access_token':tok,'title':TITLE,'content':json.dumps(nodes,ensure_ascii=False)},timeout=20).json();p=(d.get('result') or {}).get('path','');return 'https://telegra.ph/'+p if p else ''

md=article();hh=md_to_html(md);results=[]
def add(name,u):
 v=verify(name,u)
 if v:results.append({'source':name,'url':v})

try:add('telegra.ph',telegraph(md))
except Exception as e:print('TELE_ERR',repr(e))
try:add('shareyourhtml.com',simple_json('https://shareyourhtml.com/pages',{'slug':'cleaning-riyadh-'+secrets.token_hex(4),'html':hh,'expiry':'never'}))
except Exception as e:print('SHAREHTML_ERR',repr(e))
try:add('md.page',simple_json('https://md.page/api/publish',{'markdown':md}))
except Exception as e:print('MDPAGE_ERR',repr(e))
try:
 r=requests.post('https://markdown.page/api/publish',data=md.encode('utf-8'),headers={'Accept':'text/plain','Content-Type':'text/markdown','User-Agent':'Mozilla/5.0'},timeout=25);print('MARKDOWNPAGE',r.status_code,r.text[:250]);u=next((x.strip() for x in r.text.splitlines() if x.strip().startswith('http')),'');add('markdown.page',u)
except Exception as e:print('MARKDOWNPAGE_ERR',repr(e))
for name,url,payload in [
 ('yeet.md','https://yeet.md/api/share',{'content':md}),
 ('mdview.io','https://mdview.io/api/public/publish',{'title':TITLE,'content':md,'expiresInDays':30}),
 ('output.pub','https://output.pub/api/publish',{'content':md,'format':'markdown'}),
 ('quicky.page','https://quicky.page/api/v1/publish',{'title':TITLE,'content':md}),
 ('thethings.ai','https://thethings.ai/api/scratch/publish',{'content':hh,'content_type':'text/html','title':TITLE,'summary':'دليل اختيار شركة تنظيف في الرياض'}),
 ('unmarkdown.com','https://api.unmarkdown.com/v1/demo/publish',{'title':TITLE,'content':md,'template_id':'github'}),
 ('leafmill.net','https://leafmill.net/api/v1/publish',{'title':TITLE,'body':md}),
 ('htmldrop.link','https://htmldrop.link/publish',{'html':hh,'title':TITLE}),
]:
 try:add(name,simple_json(url,payload))
 except Exception as e:print(name,'ERR',repr(e))
# shipsite
try:
 b=hh.encode();rr=requests.post('https://shipsite.co/api/v1/publish',json={'files':[{'path':'index.html','size':len(b),'contentType':'text/html'}],'viewer':{'title':TITLE,'description':'دليل تنظيف في الرياض'}},timeout=25);print('SHIPSITE',rr.status_code,rr.text[:300]);c=rr.json();ups=((c.get('upload') or {}).get('uploads') or []);up=next((x for x in ups if x.get('path')=='index.html'),None)
 if up:
  requests.put(up['url'],data=b,headers={'Content-Type':'text/html'},timeout=25);f=requests.post((c.get('upload') or {}).get('finalizeUrl'),json={'versionId':(c.get('upload') or {}).get('versionId'),'claimToken':c.get('claimToken')},timeout=25);u=extract_url(f.json()) or c.get('siteUrl','');add('shipsite.co',u)
except Exception as e:print('SHIPSITE_ERR',repr(e))
print('COLORFUL_EXTRA_RESULTS_BEGIN')
for x in results:print(x['source']+'\t'+x['url'])
print('COLORFUL_EXTRA_RESULTS_END')
print('COLORFUL_EXTRA_VALID_COUNT='+str(len(results)))
print('COLORFUL_EXTRA_RESULTS_JSON='+json.dumps(results,ensure_ascii=False))
