import requests,re,json,html,secrets
from urllib.parse import urlparse

HOME='https://bvsegypt.com/'
TITLES=[
 'دليل اختيار ماكينة عد النقود المناسبة للشركات والمحلات',
 'كيف تختار ماكينة عد فلوس تناسب حجم العمل اليومي',
 'أهمية كشف العملات المزورة أثناء عمليات التحصيل النقدي',
 'نصائح للحفاظ على دقة وكفاءة ماكينة عد النقود',
 'متى تحتاج الشركات إلى ماكينة فرز وعد نقود احترافية',
 'دليل مبسط لمقارنة ماكينات عد النقود قبل الشراء',
 'كيف تقلل أخطاء العد اليدوي داخل النشاط التجاري',
 'ما الذي يجب فحصه قبل شراء ماكينة عد نقود جديدة',
 'إدارة النقد بكفاءة في المتاجر والشركات',
 'دور ماكينات عد النقود في تسريع إغلاق الخزينة',
 'أهم معايير اختيار جهاز كشف تزوير العملات',
 'الصيانة الدورية لماكينات عد النقود ولماذا تهم',
 'كيف تختار ماكينة عد نقود للاستخدام المكثف',
 'حلول عملية لعد وفرز النقد داخل الشركات',
 'لماذا تحتاج نقاط البيع إلى معدات عد نقد موثوقة',
 'كيفية تحسين دورة التعامل مع النقد في النشاط التجاري',
 'اختيار ماكينة عد النقود للمكاتب والمحلات',
 'مقارنة عملية بين العد اليدوي واستخدام ماكينة عد النقود',
 'نصائح قبل الاستثمار في ماكينة عد أو كشف عملات',
 'كيف تدير النقد اليومي بسرعة ودقة أكبر'
]
ANCHORS=[
 'BVS Egypt','ماكينات عد النقود من BVS Egypt','حلول عد وكشف النقود','BVS لماكينات عد النقود',
 'بيزنس فاليو سوليوشن','معدات عد النقود في مصر','حلول إدارة النقد من BVS','BVS Egypt لماكينات عد الفلوس',
 'متجر BVS Egypt','ماكينات كشف وفرز النقود','حلول BVS Egypt','معدات التعامل مع النقد',
 'BVS Egypt','ماكينات عد وفرز النقد','حلول عد النقود','BVS لماكينات عد النقود','بيزنس فاليو سوليوشن',
 'معدات عد النقود','حلول إدارة النقد','BVS Egypt'
]

def article(i):
 t=TITLES[i%len(TITLES)]; a=ANCHORS[i%len(ANCHORS)]
 return f'''# {t}

التعامل اليومي مع النقد يحتاج إلى دقة وسرعة، خصوصًا في الشركات والمحلات والصيدليات والمخازن والأنشطة التي تستقبل عددًا كبيرًا من المدفوعات النقدية. الاعتماد الكامل على العد اليدوي قد يستهلك وقتًا طويلًا ويزيد احتمال حدوث اختلافات في إجمالي الخزينة، لذلك تساعد معدات عد وفرز النقد على تنظيم العملية وتقليل الأعمال المتكررة.

## حدد حجم الاستخدام قبل اختيار الجهاز

أول خطوة هي تحديد متوسط حجم النقد الذي يتم التعامل معه يوميًا. النشاط الصغير قد يحتاج إلى ماكينة بسيطة وسريعة للعد، بينما تحتاج الشركات التي تتعامل مع كميات كبيرة من الأوراق النقدية إلى جهاز يتحمل التشغيل لفترات أطول ويقدم وظائف إضافية مثل التجميع والفرز والتنبيه عند وجود ورقة مشتبه بها.

كما يجب الاهتمام بسهولة التشغيل ووضوح لوحة التحكم وسرعة الوصول إلى الصيانة وقطع الغيار. الجهاز المناسب ليس بالضرورة صاحب أكبر عدد من الوظائف، بل الجهاز الذي يلائم طبيعة الاستخدام الفعلي ويقلل الوقت الضائع داخل دورة العمل.

## الدقة أهم من السرعة وحدها

سرعة العد عامل مهم، لكن القرار لا يجب أن يعتمد عليها بمفردها. من الأفضل تقييم ثبات النتائج عند تشغيل الجهاز أكثر من مرة، وقدرته على التعامل مع الأوراق المستخدمة يوميًا، وسهولة تنظيف الحساسات وأجزاء السحب. وجود نظام واضح للصيانة يساعد كذلك على الحفاظ على الأداء وتقليل الأعطال المفاجئة.

للتعرف على خيارات متخصصة في هذا المجال يمكن مراجعة [{a}]({HOME}) ومقارنة الحلول المتاحة وفق احتياجات النشاط وحجم التعامل النقدي.

## كشف التزوير جزء من إدارة المخاطر

في البيئات التي تستقبل النقد من عدد كبير من العملاء، يصبح فحص الأوراق خطوة مهمة إلى جانب العد. وجود تقنيات مساعدة على اكتشاف الأوراق المشتبه بها يقلل الاعتماد على الفحص البصري وحده، لكن يظل من المهم تدريب الموظفين على التعامل الصحيح مع الجهاز ومراجعة التنبيهات بدل تجاهلها أثناء أوقات الضغط.

## الصيانة المنتظمة تحافظ على الأداء

تراكم الأتربة وبقايا الأوراق داخل مسار السحب يمكن أن يؤثر على دقة العد بمرور الوقت. لذلك يفيد وضع جدول دوري للتنظيف والفحص، مع التوقف عن استخدام الجهاز عند ظهور أخطاء متكررة بدل الاستمرار في التشغيل حتى تتفاقم المشكلة. كما أن استخدام قطع غيار مناسبة عند الحاجة يساهم في إطالة العمر التشغيلي للمعدة.

## اختيار الحل المناسب يوفر وقت الفريق

عند اختيار ماكينة مناسبة لطبيعة العمل تصبح عملية إقفال الخزينة أسرع، ويمكن للموظفين التركيز على المراجعة بدل قضاء وقت طويل في العد المتكرر. أفضل نتيجة تأتي من الجمع بين جهاز مناسب، وإجراءات تشغيل واضحة، ومراجعة دورية للأداء، وصيانة يمكن الوصول إليها عند الحاجة.

في النهاية، قرار الشراء الجيد يبدأ من فهم حجم الاستخدام والمشكلات التي تريد حلها، ثم مقارنة السرعة والدقة ووظائف الكشف وخدمة ما بعد البيع والتكلفة الإجمالية للتشغيل قبل الاعتماد على أي جهاز.'''

def md_to_html(md):
 out=[]
 for p in re.split(r'\n\s*\n',md):
  p=p.strip()
  if not p: continue
  if p.startswith('# '): out.append('<h1>'+html.escape(p[2:])+'</h1>'); continue
  if p.startswith('## '): out.append('<h2>'+html.escape(p[3:])+'</h2>'); continue
  parts=[]; pos=0
  for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',p):
   parts.append(html.escape(p[pos:m.start()]))
   parts.append('<a href="'+html.escape(m.group(2),quote=True)+'">'+html.escape(m.group(1))+'</a>')
   pos=m.end()
  parts.append(html.escape(p[pos:]))
  out.append('<p>'+''.join(parts).replace('\n',' ')+'</p>')
 return '<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body><main>'+''.join(out)+'</main></body></html>'

def extract_url(d):
 if isinstance(d,dict):
  for k in ('url','link','shareUrl','share_url','viewerUrl','viewer_url','pageUrl','page_url','siteUrl','site_url','previewUrl','publicUrl','public_url'):
   v=d.get(k)
   if isinstance(v,str) and v.startswith('http'): return v
  for v in d.values():
   u=extract_url(v)
   if u:return u
 elif isinstance(d,list):
  for v in d:
   u=extract_url(v)
   if u:return u
 return ''

def verify(name,u):
 if not u:return None
 try:
  r=requests.get(u,timeout=18,allow_redirects=True,headers={'User-Agent':'Mozilla/5.0 BVSVerifier/1.0'})
  ok=r.status_code<400 and 'bvsegypt.com' in r.text.lower()
  print('VERIFY',name,r.status_code,ok,r.url)
  return r.url if ok else None
 except Exception as e:
  print('VERIFY_ERR',name,repr(e)); return None

def pub_telegra(i):
 s=requests.Session(); a=article(i)
 acc=s.post('https://api.telegra.ph/createAccount',data={'short_name':'BVSEgypt','author_name':'BVS Editorial'},timeout=15).json(); tok=(acc.get('result') or {}).get('access_token','')
 nodes=[]
 for p in re.split(r'\n\s*\n',a):
  p=p.strip()
  if not p:continue
  tag='p'; txt=p
  if p.startswith('# '):tag='h3';txt=p[2:]
  elif p.startswith('## '):tag='h4';txt=p[3:]
  ch=[];pos=0
  for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',txt):
   if m.start()>pos:ch.append(txt[pos:m.start()])
   ch.append({'tag':'a','attrs':{'href':m.group(2)},'children':[m.group(1)]});pos=m.end()
  if pos<len(txt):ch.append(txt[pos:])
  nodes.append({'tag':tag,'children':ch})
 d=s.post('https://api.telegra.ph/createPage',data={'access_token':tok,'title':TITLES[i],'content':json.dumps(nodes,ensure_ascii=False)},timeout=15).json(); p=(d.get('result') or {}).get('path','')
 return 'https://telegra.ph/'+p if p else ''

def simple_json(url,payload):
 r=requests.post(url,json=payload,timeout=18,headers={'User-Agent':'Mozilla/5.0 BVS/1.0'}); print('POST',url,r.status_code,r.text[:180])
 try:return extract_url(r.json()) if r.ok else ''
 except:return ''

def publish(name,i):
 md=article(i); hh=md_to_html(md); title=TITLES[i]
 try:
  if name=='telegra.ph': return pub_telegra(i)
  if name=='pagedrop.dev': return simple_json('https://pagedrop.dev/api/v1/sites',{'html':hh,'title':title})
  if name=='freekit.dev': return simple_json('https://freekit.dev/api/v1/sites',{'html':hh,'title':title})
  if name=='shareyourhtml.com': return simple_json('https://shareyourhtml.com/pages',{'slug':'bvs-'+secrets.token_hex(5),'html':hh,'expiry':'never'})
  if name=='shippage.ai': return simple_json('https://shippage.ai/v1/publish',{'html':hh,'title':title,'public':True})
  if name=='md.page': return simple_json('https://md.page/api/publish',{'markdown':md})
  if name=='yeet.md': return simple_json('https://yeet.md/api/share',{'content':md})
  if name=='mdview.io': return simple_json('https://mdview.io/api/public/publish',{'title':title,'content':md,'expiresInDays':30})
  if name=='output.pub': return simple_json('https://output.pub/api/publish',{'content':md,'format':'markdown'})
  if name=='quicky.page': return simple_json('https://quicky.page/api/v1/publish',{'title':title,'content':md})
  if name=='thethings.ai': return simple_json('https://thethings.ai/api/scratch/publish',{'content':hh,'content_type':'text/html','title':title,'summary':'BVS Egypt cash handling guide'})
  if name=='unmarkdown.com': return simple_json('https://api.unmarkdown.com/v1/demo/publish',{'title':title,'content':md,'template_id':'github'})
  if name=='leafmill.net': return simple_json('https://leafmill.net/api/v1/publish',{'title':title,'body':md})
  if name=='htmldrop.link': return simple_json('https://htmldrop.link/publish',{'html':hh,'title':title})
  if name=='brewpage.app': return simple_json('https://brewpage.app/api/html?ns=public&ttl=30',{'content':hh,'ttl':30})
  if name=='mdshare.live':
   r=requests.post('https://mdshare.live/api/documents',data=md.encode('utf-8'),headers={'Content-Type':'text/markdown','User-Agent':'Mozilla/5.0'},timeout=18); print('POST mdshare',r.status_code,r.text[:180])
   try:return extract_url(r.json()) if r.ok else ''
   except:return ''
  if name=='markdown.page':
   r=requests.post('https://markdown.page/api/publish',data=md.encode('utf-8'),headers={'Accept':'text/plain','Content-Type':'text/markdown','User-Agent':'Mozilla/5.0'},timeout=18); print('POST markdown.page',r.status_code,r.text[:180])
   if r.ok:
    for x in r.text.splitlines():
     if x.strip().startswith('http'):return x.strip()
   return ''
  if name=='public.dsp.so':
   files={'file':('bvs.html',hh.encode('utf-8'),'text/html')}; data={'name':title}
   r=requests.post('https://api.display.dev/v1/public/artifacts',files=files,data=data,timeout=20); print('POST display',r.status_code,r.text[:180])
   try:return extract_url(r.json()) if r.ok else ''
   except:return ''
  if name=='shipsite.co':
   b=hh.encode('utf-8'); rr=requests.post('https://shipsite.co/api/v1/publish',json={'files':[{'path':'index.html','size':len(b),'contentType':'text/html'}],'viewer':{'title':title,'description':'BVS Egypt cash handling guide'}},timeout=18); print('POST shipsite',rr.status_code,rr.text[:180]); c=rr.json()
   ups=((c.get('upload') or {}).get('uploads') or []); up=next((x for x in ups if x.get('path')=='index.html'),None)
   if not up:return ''
   requests.put(up['url'],data=b,headers={'Content-Type':'text/html'},timeout=20)
   f=requests.post((c.get('upload') or {}).get('finalizeUrl'),json={'versionId':(c.get('upload') or {}).get('versionId'),'claimToken':c.get('claimToken')},timeout=18)
   try:return extract_url(f.json()) or c.get('siteUrl','')
   except:return c.get('siteUrl','')
 except Exception as e:
  print('PUBLISH_ERR',name,repr(e)); return ''
 return ''

sites=['telegra.ph','pagedrop.dev','freekit.dev','shareyourhtml.com','shippage.ai','md.page','markdown.page','yeet.md','mdview.io','output.pub','quicky.page','thethings.ai','mdshare.live','unmarkdown.com','leafmill.net','htmldrop.link','brewpage.app','public.dsp.so','shipsite.co']
results=[]; seen=set()
for i,name in enumerate(sites):
 u=publish(name,i)
 v=verify(name,u)
 if v:
  host=urlparse(v).netloc.lower().removeprefix('www.')
  if host not in seen:
   seen.add(host); results.append({'source':name,'domain':host,'url':v,'title':TITLES[i]})
print('BVS_RESULTS_BEGIN')
for x in results: print(x['domain']+'\t'+x['url'])
print('BVS_RESULTS_END')
print('BVS_VALID_COUNT='+str(len(results)))
print('BVS_RESULTS_JSON='+json.dumps(results,ensure_ascii=False))
