import requests,re,json,html
from urllib.parse import urlparse
TARGET='https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'
ANCHOR='أفضل شركة تنظيف في الرياض'
TITLE='كيف تختار خدمة تنظيف منازل موثوقة في الرياض'
PAGE=f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{TITLE}</title><meta name="description" content="دليل عملي لاختيار خدمات تنظيف المنازل والشقق والفلل في الرياض"></head><body><main style="max-width:900px;margin:40px auto;padding:0 24px;font-family:Arial,Tahoma,sans-serif;line-height:1.95;color:#222"><h1>{TITLE}</h1><p>تحتاج المنازل في الرياض إلى خطط تنظيف تختلف باختلاف المساحة وعدد الغرف وطبيعة الاستخدام اليومي. لذلك من الأفضل تحديد المطلوب بوضوح قبل الحجز، سواء كان تنظيفًا دوريًا أو تنظيفًا عميقًا بعد انتقال أو مناسبة أو أعمال صيانة.</p><h2>حدد نطاق الخدمة أولًا</h2><p>ابدأ بتحديد الغرف والمناطق التي تحتاج إلى عناية أكبر مثل المطبخ والحمامات والنوافذ والأرضيات والمجالس. وضوح نطاق العمل يقلل الاختلافات بعد التنفيذ ويجعل مقارنة عروض الشركات أكثر دقة.</p><h2>قارن الجودة وليس السعر فقط</h2><p>تظهر جودة التنظيف في التفاصيل مثل الزوايا والحواف ومناطق اللمس المتكرر والأسطح خلف الأثاث. وعند المقارنة يمكن مراجعة <a href="{TARGET}">{ANCHOR}</a> للتعرف على نطاق خدمات تنظيف المنازل في الرياض وما يناسب احتياجات المنزل.</p><h2>اختيار الأدوات المناسبة مهم</h2><p>كل سطح يحتاج إلى أداة ومنظف مناسبين، واستخدام المواد بصورة عشوائية قد يترك آثارًا أو يؤثر على بعض التشطيبات. التنظيم في توزيع الأدوات بين المطبخ والحمامات وبقية المنزل يساعد كذلك على الحفاظ على مستوى أفضل من النظافة.</p><h2>التنظيف العميق يختلف عن الدوري</h2><p>التنظيف الدوري يركز على الحفاظ على ترتيب المنزل، بينما يشمل التنظيف العميق مناطق لا يتم الوصول إليها يوميًا مثل الزوايا خلف الأثاث وحواف الأرضيات والنوافذ وبعض التفاصيل الدقيقة في المطابخ والحمامات.</p><h2>راجع النتيجة بعد انتهاء الخدمة</h2><p>بعد الانتهاء من المفيد المرور على المناطق الرئيسية والتأكد من تنفيذ النقاط المتفق عليها. الشركات المنظمة توضح نطاق الخدمة قبل البدء وتتعامل مع الملاحظات بصورة واضحة، ما يجعل تجربة العميل أكثر استقرارًا عند تكرار الحجز.</p><h2>الخلاصة</h2><p>اختيار شركة تنظيف مناسبة في الرياض يعتمد على جودة التنفيذ ووضوح الخدمة وسهولة التواصل واستخدام الأدوات المناسبة، وليس على السعر وحده. تحديد احتياجات المنزل مسبقًا يجعل قرار الاختيار أكثر دقة.</p></main></body></html>'''
s=requests.Session();s.headers.update({'User-Agent':'Mozilla/5.0 ColorfulCloudSEO/5.0'})
def deep_url(x):
 if isinstance(x,dict):
  for k in ('url','public_url','publicUrl','live_url','liveUrl','pageUrl','site_url','siteUrl'):
   v=x.get(k)
   if isinstance(v,str) and v.startswith('http'):return v
  for v in x.values():
   u=deep_url(v)
   if u:return u
 elif isinstance(x,list):
  for v in x:
   u=deep_url(v)
   if u:return u
 elif isinstance(x,str):
  m=re.search(r'https?://[^\s\"\'<>]+',x)
  if m:return m.group(0).rstrip('.,);}')
 return ''
def verify(name,u):
 if not u:return None
 try:
  r=s.get(u,timeout=35,allow_redirects=True)
  noindex=('noindex' in r.headers.get('x-robots-tag','').lower()) or bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex',r.text,re.I))
  anchor=len(re.findall(r'<a[^>]+href=["\'][^"\']*colorfulcloudco\.com[^"\']*["\'][^>]*>\s*أفضل شركة تنظيف في الرياض\s*</a>',r.text,re.I))
  print('VERIFY',name,r.status_code,r.url,'ANCHORS',anchor,'NOINDEX',int(noindex))
  return r.url if r.status_code<400 and anchor>=1 and not noindex else None
 except Exception as e:print('VERIFY_ERR',name,repr(e));return None
results=[]
def attempt(name,func):
 try:
  r=func();print(name+'_POST',r.status_code,r.text[:700].replace('\n',' '))
  try:d=r.json()
  except:d=r.text
  u=deep_url(d);v=verify(name,u)
  if v:results.append({'source':name,'url':v,'domain':urlparse(v).netloc.lower().removeprefix('www.')})
 except Exception as e:print(name+'_ERR',repr(e))
attempt('html-docs.com',lambda:s.post('https://www.html-docs.com/api/v1/docs',data=PAGE.encode(),headers={'Content-Type':'text/html','x-agent-name':'Colorful Cloud Editorial'},timeout=45))
attempt('ht-ml.app',lambda:s.post('https://api.ht-ml.app/v1/sites',json={'html_content':PAGE},timeout=45))
attempt('meethtml.com',lambda:s.post('https://api.meethtml.com/api/v1/publish',json={'html':PAGE},timeout=45))
attempt('pitchey.app',lambda:s.post('https://pitchey.app/api/pages',json={'html':PAGE,'ttl':'30d'},timeout=45))
print('COLORFUL4_RESULTS_BEGIN')
for x in results:print(x['source']+'\t'+x['url'])
print('COLORFUL4_RESULTS_END')
print('COLORFUL4_VALID_COUNT='+str(len(results)))
print('COLORFUL4_RESULTS_JSON='+json.dumps(results,ensure_ascii=False))
