import asyncio,re,html,json,requests
from playwright.async_api import async_playwright

LINKS=[
 ('أفضل شركة تنظيف في الرياض','https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'),
 ('أفضل شركة تنظيف شقق بالرياض','https://colorfulcloudco.com/افضل-شركة-تنظيف-شقق-بالرياض/'),
 ('تنظيف منازل بالساعة بالرياض','https://colorfulcloudco.com/تنظيف-منازل-بالساعة-بالرياض/'),
 ('شركات تنظيف في الرياض','https://colorfulcloudco.com/شركات-تنظيف-في-الرياض/'),
 ('شركة غيمة ملونة للتنظيف','https://colorfulcloudco.com/'),
]

def md(title):
 return f'''# {title}

اختيار خدمة تنظيف مناسبة في الرياض يحتاج إلى مقارنة عملية بين جودة التنفيذ وخبرة الفريق وطريقة التعامل مع تفاصيل المنزل، وليس الاعتماد على السعر وحده. كل منزل له احتياجات مختلفة بحسب المساحة وعدد الغرف ونوعية الأرضيات والأثاث، لذلك تبدأ النتيجة الجيدة من تحديد المطلوب قبل الحجز.

## حدد احتياج المنزل أولًا

قبل التواصل مع أي شركة، اكتب قائمة بالمناطق التي تحتاج عناية أكبر مثل المطبخ والحمامات والمجالس وغرف النوم. إذا كان هناك كنب أو سجاد أو بقع صعبة فمن الأفضل ذكر ذلك من البداية حتى يتم تجهيز الأدوات والمواد المناسبة. يساعد هذا التنظيم على توزيع الوقت وتقليل إعادة العمل.

يمكنك مراجعة دليل [{LINKS[0][0]}]({LINKS[0][1]}) للتعرف على أهم معايير المقارنة قبل اتخاذ قرار الحجز.

## تنظيف الشقق يحتاج تنظيمًا مناسبًا للمساحة

الشقق تختلف عن الفلل في توزيع المساحات وسهولة الحركة، لذلك من المهم اختيار خطة تبدأ بإزالة الغبار ثم تنظيف الأسطح والأرضيات وتنتهي بالمطبخ والحمامات والتعقيم عند الحاجة. ترتيب الخطوات يقلل انتقال الأتربة إلى الأماكن التي تم تنظيفها بالفعل.

ولمعرفة تفاصيل الخدمة المناسبة للوحدات السكنية يمكن الاطلاع على [{LINKS[1][0]}]({LINKS[1][1]}).

## المرونة في الوقت مهمة لبعض العملاء

ليس كل عميل يحتاج يوم تنظيف كامل. أحيانًا تكون الأولوية لعدة غرف أو لمطبخ وحمامات فقط، وهنا تكون الخدمة بالساعة خيارًا عمليًا إذا كان نطاق المهام واضحًا. تحديد عدد الساعات مع الأولويات يساعد على استغلال الوقت بأفضل شكل ممكن.

يمكن مراجعة خيار [{LINKS[2][0]}]({LINKS[2][1]}) لفهم طريقة الخدمة المرنة ومتى تكون مناسبة.

## قارن الشركات من خلال نطاق الخدمة

عند مقارنة أكثر من مزود، لا تكتفِ بالسعر. راجع عدد أفراد الفريق، مدة العمل، المواد والمعدات المستخدمة، الخدمات الإضافية، سرعة التواصل، وطريقة التعامل مع الملاحظات بعد انتهاء الزيارة. هذه العناصر تعطي صورة أكثر دقة عن مستوى الخدمة المتوقع.

يساعدك دليل [{LINKS[3][0]}]({LINKS[3][1]}) على معرفة الفروق التي يجب مراجعتها عند المقارنة.

## المواد والمعدات تؤثر في النتيجة

استخدام مادة واحدة لكل الأسطح قد يسبب تلفًا أو تغيرًا في اللون. الخشب والرخام والزجاج والأقمشة تحتاج إلى طرق مختلفة، كما أن معالجة البقع يجب أن تتم بصورة تدريجية. المعدات المناسبة تساعد على الوصول إلى الزوايا وإزالة الأتربة الدقيقة وتوفير وقت التنفيذ بدون التأثير على الخامات.

وللتعرف على نطاق الخدمات المنزلية والمنشآت يمكن زيارة [{LINKS[4][0]}]({LINKS[4][1]}).

## التجهيز قبل وصول الفريق يوفر الوقت

إخلاء الأسطح من الأغراض الشخصية وترتيب الأشياء الصغيرة قبل موعد التنظيف يساعد الفريق على بدء العمل مباشرة. في المنازل الكبيرة يمكن تقسيم العقار إلى مناطق ومراجعة كل منطقة بعد الانتهاء منها. هذه الطريقة تجعل متابعة التنفيذ أكثر سهولة وتقلل احتمالات نسيان التفاصيل.

## المراجعة النهائية خطوة أساسية

بعد انتهاء العمل، راجع الأرضيات والزوايا والمطبخ والحمامات والأسطح الأكثر استخدامًا. إذا ظهرت ملاحظة بسيطة فمن الأفضل معالجتها قبل مغادرة الفريق. المراجعة النهائية لا تعني البحث عن أخطاء فقط، بل التأكد من أن نطاق العمل المتفق عليه تم تنفيذه بالكامل.

## حافظ على النتيجة بين الزيارات

بعد التنظيف الاحترافي يمكن الحفاظ على المنزل لفترة أطول بروتين بسيط يشمل إزالة الانسكابات سريعًا، مسح الأسطح التي تتعرض للغبار، تهوية المكان، وترتيب الأغراض المستخدمة يوميًا. بهذه الخطوات تقل الحاجة إلى تنظيف عميق متكرر ويصبح وقت الزيارة التالية أقل.

## الخلاصة

أفضل تجربة تنظيف تبدأ بتحديد الاحتياج بوضوح ثم اختيار شركة تشرح الخدمة والسعر وطريقة التنفيذ دون غموض. عندما تكون المهام منظمة والمواد مناسبة ويتم إجراء مراجعة نهائية، تصبح النتيجة أكثر استقرارًا ويوفر العميل وقتًا وجهدًا على المدى الطويل.'''

def to_html(text,title):
 blocks=[]
 for b in re.split(r'\n\s*\n',text):
  b=b.strip()
  if not b: continue
  if b.startswith('# '): blocks.append('<h1>'+html.escape(b[2:])+'</h1>');continue
  if b.startswith('## '): blocks.append('<h2>'+html.escape(b[3:])+'</h2>');continue
  pos=0;p=[]
  for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',b):
   p.append(html.escape(b[pos:m.start()]));p.append('<a href="'+html.escape(m.group(2),quote=True)+'">'+html.escape(m.group(1))+'</a>');pos=m.end()
  p.append(html.escape(b[pos:]));blocks.append('<p>'+''.join(p)+'</p>')
 return '<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,Tahoma,sans-serif;line-height:2">'+''.join(blocks)+'</main></body></html>'

async def verify(browser,url):
 p=await browser.new_page();resp=None
 try:
  resp=await p.goto(url,wait_until='domcontentloaded',timeout=35000);await p.wait_for_timeout(1800)
  n=0
  try:n+=await p.locator('a[href*="colorfulcloudco.com"]').count()
  except:pass
  for fr in p.frames:
   if fr==p.main_frame:continue
   try:n+=await fr.locator('a[href*="colorfulcloudco.com"]').count()
   except:pass
  robots=''
  try:robots=(await p.locator('meta[name="robots"],meta[name="googlebot"]').evaluate_all("e=>e.map(x=>x.content||'').join(' ')")).lower()
  except:pass
  xrob=''
  try:xrob=(await resp.all_headers()).get('x-robots-tag','').lower() if resp else ''
  except:pass
  noindex='noindex' in robots or 'noindex' in xrob
  final=p.url;print('VERIFY',url,'FINAL',final,'HREFS',n,'NOINDEX',int(noindex));await p.close();return final,n,noindex
 except Exception as e:
  print('VERIFY_ERR',url,repr(e));
  try:await p.close()
  except:pass
  return url,0,True

async def generic(browser,domain,url,mode,idx):
 title=['دليل تنظيف المنازل في الرياض','اختيار شركة تنظيف محترفة بالرياض','خدمات تنظيف الشقق والفلل بالرياض','تنظيف المنزل باحتراف في الرياض'][idx%4]
 m=md(title);h=to_html(m,title);content=m if mode=='md' else h
 pg=await browser.new_page()
 try:
  await pg.goto(url,wait_until='domcontentloaded',timeout=40000);await pg.wait_for_timeout(900)
  for sel in ['input[name*=title i]','input[placeholder*=title i]','input[type=text]']:
   loc=pg.locator(sel)
   if await loc.count():
    try:await loc.first.fill(title);break
    except:pass
  filled=False
  ta=pg.locator('textarea:visible')
  if await ta.count():
   try:await ta.first.fill(content);filled=True
   except:pass
  if not filled:
   ce=pg.locator('[contenteditable=true]:visible')
   if await ce.count():
    try:await ce.first.fill(content);filled=True
    except:pass
  if not filled:
   fi=pg.locator('input[type=file]')
   if await fi.count():
    path=f'/tmp/cc-{idx}.html';open(path,'w',encoding='utf-8').write(h)
    try:await fi.first.set_input_files(path);filled=True
    except:pass
  if not filled:print(domain,'NO_INPUT');await pg.close();return None
  for pat in ['Get my shareable link','Get shareable link','Generate link','Generate Live Page','Deploy Page','Deploy','Publish','Share Note','Share','Host','Upload','Generate','Create','Save']:
   btn=pg.get_by_role('button',name=re.compile(pat,re.I))
   if await btn.count():
    try:await btn.first.click(timeout=4000);break
    except:pass
  await pg.wait_for_timeout(2500)
  c=[]
  if pg.url.rstrip('/')!=url.rstrip('/'):c.append(pg.url)
  try:c += [x for x in await pg.locator('a[href]').evaluate_all('e=>e.map(x=>x.href)') if domain in x]
  except:pass
  seen=set()
  for u in c:
   if u in seen or any(x in u for x in ['/api/','manifest','favicon','login','signup']):continue
   seen.add(u);f,n,ni=await verify(browser,u)
   if n>=5 and not ni:print('VALID',domain,f);await pg.close();return (domain,f)
  print(domain,'NO_VALID',c[:8])
 except Exception as e:print(domain,'ERR',repr(e))
 try:await pg.close()
 except:pass
 return None

async def direct(browser):
 s=requests.Session();out=[]
 title='أفضل شركة تنظيف في الرياض: دليل عملي قبل الحجز';m=md(title);h=to_html(m,title)
 try:
  r=s.post('https://draftmark.app/api/v1/docs',json={'content':m,'visibility':'public'},timeout=35);print('DRAFTMARK',r.status_code,r.text[:400]);d=r.json() if r.ok else {};u=d.get('url','');
  if u and not u.startswith('http'):u='https://'+u.lstrip('/')
  if u:
   f,n,ni=await verify(browser,u)
   if n>=5 and not ni:out.append(('draftmark.app',f));print('VALID draftmark.app',f)
 except Exception as e:print('DRAFTMARK_ERR',repr(e))
 try:
  r=s.post('https://share-html.com/api/v1/pages',json={'html':h},timeout=35);print('SHAREHTML',r.status_code,r.text[:400]);d=r.json() if r.ok else {};vals=[]
  def walk(x):
   if isinstance(x,str) and x.startswith('http'):vals.append(x)
   elif isinstance(x,dict):
    for v in x.values():walk(v)
   elif isinstance(x,list):
    for v in x:walk(v)
  walk(d)
  for u in vals:
   if 'share-html.com' in u and '/api/' not in u:
    f,n,ni=await verify(browser,u)
    if n>=5 and not ni:out.append(('share-html.com',f));print('VALID share-html.com',f);break
 except Exception as e:print('SHAREHTML_ERR',repr(e))
 return out

async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True)
  out=await direct(browser)
  tasks=[generic(browser,*x,i) for i,x in enumerate([
   ('notesh.ink','https://notesh.ink/','md'),
   ('yapp.page','https://yapp.page/','html'),
   ('publishmarkdown.com','https://publishmarkdown.com/','md'),
   ('markdshare.com','https://markdshare.com/','md'),
  ])]
  res=await asyncio.gather(*tasks)
  out += [x for x in res if x]
  print('FAST7_RESULTS_BEGIN')
  for d,u in out:print(d+'\t'+u)
  print('FAST7_RESULTS_END')
  print('FAST7_VALID_COUNT='+str(len(out)))
  print('FAST7_RESULTS_JSON='+json.dumps([{'source':d,'url':u} for d,u in out],ensure_ascii=False))
  await browser.close()

asyncio.run(main())
