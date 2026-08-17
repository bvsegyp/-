import requests,re,json,html,hashlib,subprocess,os
from urllib.parse import urlparse

TARGET='https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'
ANCHOR='أفضل شركة تنظيف في الرياض'
s=requests.Session(); s.headers.update({'User-Agent':'Mozilla/5.0 ColorfulCloudEditorial/3.0'})

TITLES=[
'تنظيف المنازل في الرياض وكيف تختار الخدمة المناسبة',
'دليل تنظيف الفلل والشقق في الرياض باحتراف',
'معايير اختيار شركة تنظيف للمنازل في الرياض',
'كيف تحصل على تنظيف عميق ومرتب لمنزلك في الرياض',
'تنظيف المطابخ والحمامات ضمن خدمة منزلية متكاملة',
'خطة عملية للحفاظ على نظافة المنزل في الرياض',
'الفرق بين التنظيف الدوري والتنظيف العميق للمنازل'
]

def article(title):
 return f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="دليل عملي لاختيار خدمات تنظيف المنازل والشقق والفلل في الرياض"></head><body><main style="max-width:900px;margin:40px auto;padding:0 24px;font-family:Arial,Tahoma,sans-serif;line-height:1.95;color:#222"><h1>{html.escape(title)}</h1><p>الحصول على منزل نظيف ومرتب لا يعتمد فقط على سرعة تنفيذ العمل، بل على طريقة تنظيم الخدمة واختيار الأدوات والمنظفات المناسبة لكل سطح. تختلف احتياجات الشقق عن الفلل، كما يختلف التنظيف الدوري عن التنظيف العميق الذي يشمل الزوايا والمناطق التي لا تصل إليها أعمال التنظيف اليومية بسهولة.</p><h2>حدد احتياجات المنزل قبل الحجز</h2><p>من الأفضل تحديد الغرف والمناطق التي تحتاج إلى اهتمام أكبر قبل بدء الخدمة. قد تكون الأولوية للمطبخ والحمامات والنوافذ والأرضيات، أو قد يحتاج المنزل بالكامل إلى تنظيف شامل بعد انتقال أو مناسبة أو أعمال صيانة. هذا التحديد يجعل نطاق الخدمة واضحًا ويساعد على تقييم النتيجة بعد الانتهاء.</p><h2>جودة التنظيف تظهر في التفاصيل</h2><p>التنظيف الجيد يشمل الأسطح الظاهرة والزوايا والحواف والمناطق خلف الأثاث ومقابض الأبواب وأماكن اللمس المتكرر. كما يجب استخدام مادة مناسبة لكل نوع من الأسطح لتجنب الخدش أو تغير اللون أو ترك آثار بعد التنظيف.</p><p>عند مقارنة الشركات والخدمات المتاحة، يمكن مراجعة <a href="{TARGET}">{ANCHOR}</a> والتعرف على نطاق خدمات تنظيف المنازل في الرياض قبل اتخاذ قرار الحجز.</p><h2>المطبخ والحمامات يحتاجان أسلوبًا مختلفًا</h2><p>تتراكم الدهون والرطوبة في المطبخ والحمامات بصورة أسرع من بقية المنزل. لذلك يفيد استخدام أدوات مخصصة لهذه المناطق مع الاهتمام بالأرضيات والجدران والأسطح ومناطق الالتقاء والزوايا، ثم التهوية الجيدة بعد الانتهاء للحفاظ على النتيجة.</p><h2>المعدات المناسبة توفر الوقت وتحسن النتيجة</h2><p>استخدام المكانس والأدوات والمواد الملائمة يساعد فريق التنظيف على إنجاز العمل بصورة أكثر انتظامًا. المهم ليس كثرة المعدات، بل اختيار الأداة الصحيحة لكل مهمة وتجنب استخدام نفس الأداة على أسطح مختلفة بطريقة قد تنقل الأوساخ بدل إزالتها.</p><h2>راجع النتيجة بعد الانتهاء</h2><p>من المفيد إجراء مراجعة سريعة للمناطق الرئيسية ومطابقة التنفيذ مع النقاط المتفق عليها قبل بدء الخدمة. الشركات المنظمة توضح ما هو مشمول في الباقة وما يحتاج إلى طلب منفصل، ما يجعل تجربة العميل أكثر وضوحًا ويساعد على تكرار الخدمة عند الحاجة.</p><h2>الخلاصة</h2><p>اختيار خدمة تنظيف مناسبة في الرياض يبدأ بفهم احتياجات المنزل ثم مقارنة نطاق العمل وجودة التنفيذ وسهولة التواصل والمواد المستخدمة. الاعتماد على هذه المعايير يعطي نتيجة أفضل من اختيار الخدمة بناءً على السعر وحده.</p></main></body></html>'''

def verify(name,u):
 if not u:return None
 try:
  r=s.get(u,timeout=40,allow_redirects=True)
  noindex=('noindex' in r.headers.get('x-robots-tag','').lower()) or bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex',r.text,re.I))
  anchors=len(re.findall(r'<a[^>]+href=["\'][^"\']*colorfulcloudco\.com[^"\']*["\'][^>]*>\s*أفضل شركة تنظيف في الرياض\s*</a>',r.text,re.I))
  print('VERIFY',name,r.status_code,r.url,'ANCHORS',anchors,'NOINDEX',int(noindex))
  return r.url if r.status_code<400 and anchors>=1 and not noindex else None
 except Exception as e:
  print('VERIFY_ERR',name,repr(e));return None

def urls(obj):
 out=[]
 def walk(x):
  if isinstance(x,str):out.extend(re.findall(r'https?://[^\s"\'<>]+',x))
  elif isinstance(x,dict):
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(obj);return [u.rstrip('.,);}') for u in out]

def choose(obj,domains=()):
 us=urls(obj)
 for d in domains:
  for u in us:
   if d in u:return u
 return us[0] if us else ''

def main():
 results=[]
 def add(name,u):
  v=verify(name,u)
  if v:results.append({'source':name,'url':v,'domain':urlparse(v).netloc.lower().removeprefix('www.')})

 # XDR exact three-step
 try:
  data=article(TITLES[0]).encode('utf-8'); sha=hashlib.sha256(data).hexdigest()
  r=s.post('https://api.xdr.no/api/v1/publish',json={'files':[{'path':'index.html','size':len(data),'contentType':'text/html','sha256':sha}]},timeout=50)
  print('XDR_CREATE',r.status_code,r.text[:600]); d=r.json(); ups=d.get('uploads') or []; live=d.get('url'); fin=d.get('finalize')
  if ups:
   up=ups[0]; requests.put(up.get('putUrl'),data=data,headers={'Content-Type':'text/html'},timeout=55)
   if fin:s.post(fin,timeout=50)
  add('xdr.no',live)
 except Exception as e:print('XDR_ERR',repr(e))

 # Draftlet exact three-step
 try:
  data=article(TITLES[1]).encode('utf-8')
  r=s.post('https://api.draftlet.io/api/v1/publish',json={'files':[{'path':'index.html','contentType':'text/html','size':len(data)}]},timeout=55)
  print('DRAFTLET_CREATE',r.status_code,r.text[:600]); d=r.json(); slug=d['slug']; ver=d['versionId']; tok=d['editToken']; up=d['uploads'][0]['uploadUrl']; live=d['url']
  requests.put(up,data=data,headers={'content-type':'text/html','content-length':str(len(data))},timeout=60)
  s.post(f'https://api.draftlet.io/api/v1/publish/{slug}/finalize',json={'versionId':ver,'editToken':tok},timeout=55)
  add('draftlet.io',live)
 except Exception as e:print('DRAFTLET_ERR',repr(e))

 # Draftmark
 try:
  r=s.post('https://draftmark.app/api/v1/docs',json={'content':article(TITLES[2]),'visibility':'public'},headers={'Content-Type':'application/json'},timeout=45)
  print('DRAFTMARK',r.status_code,r.text[:500]); d=r.json() if r.ok else {}; u=d.get('url','');
  if u and not u.startswith('http'):u='https://'+u
  add('draftmark.app',u)
 except Exception as e:print('DRAFTMARK_ERR',repr(e))

 # HTMLShare
 try:
  r=s.post('https://api.htmlshare.net/v1/publish',json={'html':article(TITLES[3])},timeout=45)
  print('HTMLSHARE',r.status_code,r.text[:500]); d=r.json() if r.ok else {}; add('htmlshare.net',d.get('url',''))
 except Exception as e:print('HTMLSHARE_ERR',repr(e))

 # ZeroDeploy - use live data.url, not API endpoint
 try:
  r=s.post('https://api.zerodeploy.dev/drop',files={'file':('index.html',article(TITLES[4]),'text/html')},timeout=60)
  print('ZERODEPLOY',r.status_code,r.text[:700]); d=r.json() if r.ok else {}; data=d.get('data') or {}; u=data.get('url','') or d.get('url',''); add('zerodeploy.app',u)
 except Exception as e:print('ZERODEPLOY_ERR',repr(e))

 # Sitebin - try all non-edit URLs from response
 try:
  r=s.post('https://app.sitebin.io/api/sites',files={'files':('index.html',article(TITLES[5]),'text/html')},timeout=60)
  print('SITEBIN',r.status_code,r.text[:900]); d=r.json() if r.ok else {}; candidates=[]
  for u in urls(d):
   if 'sitebin.io' in u and '/e/' not in u:candidates.append(u)
  for k in ('url','site_url','public_url','live_url'):
   if isinstance(d,dict) and d.get(k):candidates.insert(0,d[k])
  seen=set()
  for u in candidates:
   if u in seen:continue
   seen.add(u);v=verify('sitebin.io',u)
   if v:results.append({'source':'sitebin.io','url':v,'domain':urlparse(v).netloc.lower().removeprefix('www.')});break
 except Exception as e:print('SITEBIN_ERR',repr(e))

 # Based.page CLI
 try:
  fn='/tmp/colorfulcloud-based.html';open(fn,'w',encoding='utf-8').write(article(TITLES[6]))
  p=subprocess.run(['npx','-y','based-page@latest','deploy','--file',fn,'--slug','riyadh-home-cleaning-guide','--title',TITLES[6]],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=150)
  print('BASED_RC',p.returncode);print('BASED_OUT',p.stdout[:2000].replace('\n',' '));u=choose(p.stdout,('based.page',));add('based.page',u)
 except Exception as e:print('BASED_ERR',repr(e))

 print('COLORFUL3_RESULTS_BEGIN')
 for x in results:print(x['source']+'\t'+x['url'])
 print('COLORFUL3_RESULTS_END')
 print('COLORFUL3_VALID_COUNT='+str(len(results)))
 print('COLORFUL3_RESULTS_JSON='+json.dumps(results,ensure_ascii=False))

if __name__=='__main__':main()
