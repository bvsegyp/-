import requests,re,json,html,secrets,hashlib,time
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup

TARGET='https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'
ANCHOR='أفضل شركة تنظيف في الرياض'
s=requests.Session(); s.headers.update({'User-Agent':'Mozilla/5.0 ColorfulCloudEditorial/2.0'})

TITLES=[
'كيف تختار شركة تنظيف موثوقة لمنزلك في الرياض',
'تنظيف المنازل في الرياض ومعايير الجودة التي تستحق الاهتمام',
'دليل تنظيف الشقق والفلل في الرياض بطريقة احترافية',
'متى تحتاج إلى شركة تنظيف متخصصة في الرياض',
'كيف تقارن بين شركات التنظيف قبل حجز الخدمة في الرياض',
'خطة عملية لتنظيف المنزل بعمق في الرياض',
'تنظيف المطابخ والحمامات ضمن خدمات التنظيف الشامل',
'أهمية المعدات والمنظفات المناسبة في تنظيف المنازل',
'كيف تحافظ على نظافة المنزل بعد خدمة التنظيف العميق',
'اختيار خدمة تنظيف تناسب الشقق والفلل في الرياض',
'معايير تقييم جودة شركات تنظيف المنازل في الرياض',
'دليل عملي لخدمات التنظيف الدوري والعميق في الرياض'
]

def article(i):
 t=TITLES[i%len(TITLES)]
 return f'''# {t}

تختلف احتياجات التنظيف من منزل إلى آخر حسب المساحة وعدد الغرف وطبيعة الأثاث ومستوى الاستخدام اليومي. لذلك لا يعتمد اختيار خدمة التنظيف الجيدة على السعر فقط، بل على وضوح نطاق العمل، جودة المواد والمعدات المستخدمة، خبرة فريق العمل، والقدرة على تنفيذ الخدمة بطريقة منظمة تحافظ على الأثاث والأسطح.

## ابدأ بتحديد نطاق الخدمة

قبل الحجز من المفيد تحديد المناطق التي تحتاج إلى تنظيف فعلي، مثل غرف النوم والمجالس والمطابخ والحمامات والنوافذ والأرضيات. بعض المنازل تحتاج إلى تنظيف دوري خفيف، بينما تحتاج منازل أخرى إلى تنظيف عميق بعد مناسبة أو انتقال أو أعمال صيانة. تحديد النطاق يساعد على اختيار الباقة المناسبة وتجنب دفع تكلفة إضافية لخدمات لا تحتاج إليها.

## الجودة تظهر في التفاصيل

التنظيف الاحترافي لا يقتصر على إزالة الغبار الظاهر. من المهم الانتباه إلى الزوايا، حواف الأرضيات، الأسطح المرتفعة، الأماكن خلف الأثاث، مقابض الأبواب، والمناطق التي تتعرض للمس المتكرر. كما أن استخدام الأدوات المناسبة لكل سطح يقلل خطر الخدوش أو تغير اللون ويحافظ على شكل المنزل بعد انتهاء الخدمة.

عند مقارنة الخيارات المتاحة، يمكن مراجعة [{ANCHOR}]({TARGET}) للتعرف على خدمة متخصصة في تنظيف المنازل بالرياض ومقارنة نطاق العمل بما يناسب احتياجات المنزل.

## تنظيف المطبخ يحتاج عناية مختلفة

المطبخ يجمع بين الدهون وبقايا الطعام والرطوبة، لذلك يحتاج إلى مواد وأدوات مناسبة للأسطح المختلفة. تنظيف الخزائن من الخارج، أسطح التحضير، الحوض، الأرضيات والمناطق المحيطة بالأجهزة يساعد على تحسين مستوى النظافة العامة ويقلل تراكم الأوساخ مع الوقت.

## الحمامات تحتاج إلى معالجة دقيقة

الرطوبة المستمرة تجعل الحمامات من أكثر الأماكن التي تحتاج إلى متابعة. يجب الاهتمام بالأرضيات والجدران والزوايا والمغاسل والمرايا، مع استخدام مواد مناسبة لا تضر بالأسطح. التهوية بعد التنظيف تساعد كذلك على تقليل الرطوبة والحفاظ على النتيجة لفترة أطول.

## المعدات المناسبة ترفع كفاءة العمل

الفرق المجهزة بمكانس وأدوات تنظيف متعددة ومواد مخصصة لكل نوع من الأسطح تستطيع إنجاز العمل بصورة أكثر انتظامًا. المهم ليس عدد الأدوات فقط، بل اختيار الأداة الصحيحة واستخدامها بطريقة تقلل الوقت وتحافظ على جودة النتيجة.

## راجع ما بعد الخدمة

بعد انتهاء التنظيف، من المفيد المرور على المناطق الرئيسية والتأكد من تنفيذ النقاط المتفق عليها. الشركات المنظمة توضح نطاق الخدمة قبل البدء وتتعامل مع الملاحظات بطريقة واضحة، وهو ما يجعل تجربة العميل أكثر استقرارًا عند تكرار الحجز مستقبلًا.

## الخلاصة

اختيار شركة تنظيف مناسبة في الرياض يبدأ من فهم احتياجات المنزل ثم مقارنة نطاق الخدمات وجودة التنفيذ والمواد المستخدمة وسهولة التواصل. الاهتمام بهذه المعايير يساعد على الحصول على نتيجة أفضل بدل الاعتماد على السعر وحده.'''

def md_to_html(md):
 out=[]
 for b in re.split(r'\n\s*\n',md):
  b=b.strip()
  if not b: continue
  if b.startswith('# '): out.append('<h1>'+html.escape(b[2:])+'</h1>'); continue
  if b.startswith('## '): out.append('<h2>'+html.escape(b[3:])+'</h2>'); continue
  parts=[]; pos=0
  for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',b):
   parts.append(html.escape(b[pos:m.start()])); parts.append('<a href="'+html.escape(m.group(2),quote=True)+'">'+html.escape(m.group(1))+'</a>'); pos=m.end()
  parts.append(html.escape(b[pos:])); out.append('<p>'+''.join(parts).replace('\n',' ')+'</p>')
 return '<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(TITLES[0])+'</title></head><body><main style="max-width:900px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.9">'+''.join(out)+'</main></body></html>'

def extract(d):
 if isinstance(d,dict):
  for k in ['url','share_url','shareUrl','publicUrl','public_url','previewUrl','pageUrl','siteUrl','link','viewerUrl']:
   v=d.get(k)
   if isinstance(v,str) and v.startswith('http'): return v
  for v in d.values():
   u=extract(v)
   if u:return u
 elif isinstance(d,list):
  for v in d:
   u=extract(v)
   if u:return u
 return ''

def verify_http(name,u):
 if not u or not u.startswith('http'): return None
 try:
  r=s.get(u,timeout=35,allow_redirects=True)
  soup=BeautifulSoup(r.text,'html.parser')
  anchors=[a for a in soup.find_all('a',href=True) if 'colorfulcloudco.com' in a.get('href','').lower() and ANCHOR in a.get_text(' ',strip=True)]
  noindex=('noindex' in r.headers.get('x-robots-tag','').lower()) or bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex',r.text,re.I))
  print('VERIFY',name,r.status_code,r.url,'ANCHORS',len(anchors),'NOINDEX',int(noindex))
  return r.url if r.status_code<400 and anchors and not noindex else None
 except Exception as e:
  print('VERIFY_ERR',name,repr(e)); return None

def add(results,name,u):
 v=verify_http(name,u)
 if v: results.append({'source':name,'domain':urlparse(v).netloc.lower().removeprefix('www.'),'url':v})

def pjson(url,payload,**kwargs):
 r=s.post(url,json=payload,timeout=35,**kwargs); print('POST',url,r.status_code,r.text[:300].replace('\n',' '))
 if not r.ok:return ''
 try:return extract(r.json())
 except:return ''

def run():
 results=[]; pending=[]
 # Display / public.dsp.so
 try:
  h=md_to_html(article(0)); r=s.post('https://api.display.dev/v1/public/artifacts',files={'file':('riyadh-cleaning-guide.html',h.encode(),'text/html')},data={'name':'riyadh-cleaning-guide'},timeout=35); print('DISPLAY',r.status_code,r.text[:300]);
  try:u=extract(r.json())
  except:u=''
  add(results,'public.dsp.so',u)
 except Exception as e: print('DISPLAY_ERR',repr(e))
 # Pubmark
 try:
  r=s.post('https://pubmark.site/api/documents',json={'title':TITLES[1]},timeout=35); print('PUBMARK_CREATE',r.status_code,r.text[:250]); d=r.json(); sid=d.get('secretId'); u=''
  if sid:
   s.put('https://pubmark.site/api/documents/'+sid,json={'content':article(1),'title':TITLES[1],'theme':'clean','colorPreset':'blue'},timeout=35)
   p=s.post('https://pubmark.site/api/documents/'+sid+'/publish',json={},timeout=35); print('PUBMARK_PUB',p.status_code,p.text[:250]); slug=(p.json() if p.ok else {}).get('slug'); u='https://pubmark.site/p/'+slug if slug else ''
  add(results,'pubmark.site',u)
 except Exception as e: print('PUBMARK_ERR',repr(e))
 # MDLib
 try:
  u=pjson('https://mdlib.dev/v1/docs',{'markdown':article(2),'title':TITLES[2],'is_public':True}); add(results,'mdlib.dev',u)
 except Exception as e: print('MDLIB_ERR',repr(e))
 # Jotbird
 try:
  r=s.post('https://api.jotbird.com/trial/publish',json={'markdown':article(3),'title':TITLES[3]},headers={'User-Agent':'jotbird-vscode/1.0.0'},timeout=35); print('JOTBIRD',r.status_code,r.text[:250]);
  try:u=extract(r.json())
  except:u=''
  add(results,'jotbird.com',u)
 except Exception as e: print('JOTBIRD_ERR',repr(e))
 # Stacktree
 try:
  h=md_to_html(article(4)); r=s.post('https://api.stacktr.ee/sites',files={'file':('index.html',h.encode(),'text/html')},timeout=40); print('STACKTREE',r.status_code,r.text[:250]);
  try:u=extract(r.json())
  except:u=''
  add(results,'stacktr.ee',u)
 except Exception as e: print('STACKTREE_ERR',repr(e))
 # Here.now
 try:
  h=md_to_html(article(5)); b=h.encode(); sha=hashlib.sha256(b).hexdigest(); d=s.post('https://here.now/api/v1/publish',headers={'X-HereNow-Client':'chatgpt/direct-api','Content-Type':'application/json'},json={'files':[{'path':'index.html','size':len(b),'contentType':'text/html; charset=utf-8','hash':sha}],'viewer':{'title':TITLES[5]}},timeout=40).json(); site=d.get('siteUrl',''); up=d.get('upload') or {}; ups=up.get('uploads') or []
  if ups: requests.put(ups[0]['url'],data=b,headers=ups[0].get('headers') or {'Content-Type':'text/html; charset=utf-8'},timeout=40)
  if up.get('finalizeUrl') and up.get('versionId'): s.post(up['finalizeUrl'],json={'versionId':up['versionId']},timeout=35)
  add(results,'here.now',site)
 except Exception as e: print('HERENOW_ERR',repr(e))
 # Rentry
 try:
  rs=requests.Session(); rs.headers.update({'User-Agent':'Mozilla/5.0'}); rs.get('https://rentry.co/',timeout=35); csrf=rs.cookies.get('csrftoken',''); rr=rs.post('https://rentry.co/api/new',data={'csrfmiddlewaretoken':csrf,'text':article(6),'edit_code':secrets.token_urlsafe(12),'url':''},headers={'Referer':'https://rentry.co/'},timeout=35); print('RENTRY',rr.status_code,rr.text[:250]); d=rr.json() if rr.ok else {}; u=d.get('url',''); add(results,'rentry.co',u)
 except Exception as e: print('RENTRY_ERR',repr(e))
 # MDShare - leave for browser verifier if raw verification fails
 try:
  md=article(7); d=s.post('https://mdshare.live/api/documents',data=md.encode(),headers={'Content-Type':'text/markdown'},timeout=35).json(); doc=d.get('document_id',''); key=d.get('admin_key',''); u=''
  if doc and key:
   q=s.post(f'https://mdshare.live/api/d/{doc}/links?key={key}',json={'permission':'view','label':'public-view'},timeout=35); print('MDSHARE_LINK',q.status_code,q.text[:300]);
   try:u=extract(q.json())
   except:u=''
  v=verify_http('mdshare.live',u)
  if v: results.append({'source':'mdshare.live','domain':urlparse(v).netloc.lower().removeprefix('www.'),'url':v})
  elif u: pending.append({'source':'mdshare.live','url':u})
 except Exception as e: print('MDSHARE_ERR',repr(e))
 # Pastebox
 try:
  u=pjson('https://lfdekutkxwsczpasjgsg.supabase.co/functions/v1/create-share',{'content':article(8),'title':TITLES[8],'language':'markdown','content_type':'text','expiration':'1M','exposure':'public','source':'api'}); v=verify_http('pastebox.ai',u)
  if v: results.append({'source':'pastebox.ai','domain':urlparse(v).netloc.lower().removeprefix('www.'),'url':v})
  elif u: pending.append({'source':'pastebox.ai','url':u})
 except Exception as e: print('PASTEBOX_ERR',repr(e))
 # Pastepile
 try:
  u=pjson('https://www.pastepile.com/api/public/pastes',{'title':TITLES[9],'content':article(9),'language':'markdown','expiry':'1mo','visibility':'public'}); v=verify_http('pastepile.com',u)
  if v: results.append({'source':'pastepile.com','domain':urlparse(v).netloc.lower().removeprefix('www.'),'url':v})
  elif u: pending.append({'source':'pastepile.com','url':u})
 except Exception as e: print('PASTEPILE_ERR',repr(e))
 # PasteHTML.dev
 try:
  h=md_to_html(article(10)); r=s.post('https://pastehtml.dev/api/pastes',files={'file':('riyadh-cleaning.html',h.encode(),'text/html')},timeout=40); print('PASTEHTML',r.status_code,r.text[:250]);
  try:u=extract(r.json())
  except:u=''
  v=verify_http('pastehtml.dev',u)
  if v: results.append({'source':'pastehtml.dev','domain':urlparse(v).netloc.lower().removeprefix('www.'),'url':v})
  elif u: pending.append({'source':'pastehtml.dev','url':u})
 except Exception as e: print('PASTEHTML_ERR',repr(e))
 # ShowYourCode
 try:
  h=md_to_html(article(11)); d=s.post('https://www.showyourcode.app/api/works',json={'htmlContent':h,'title':TITLES[11],'topicIds':[],'type':'html','templateId':None},timeout=35); print('SHOWCODE',d.status_code,d.text[:300]); j=d.json() if d.ok else {}; uid=j.get('uuid'); u='https://www.showyourcode.app/share/'+uid if uid else ''; v=verify_http('showyourcode.app',u)
  if v: results.append({'source':'showyourcode.app','domain':urlparse(v).netloc.lower().removeprefix('www.'),'url':v})
  elif u: pending.append({'source':'showyourcode.app','url':u})
 except Exception as e: print('SHOWCODE_ERR',repr(e))
 # dedupe hosts
 final=[];seen=set()
 for x in results:
  d=x['domain']
  if d not in seen:seen.add(d);final.append(x)
 print('COLORFUL2_RESULTS_BEGIN')
 for x in final: print(x['source']+'\t'+x['url'])
 print('COLORFUL2_RESULTS_END')
 print('COLORFUL2_PENDING_BEGIN')
 for x in pending: print(x['source']+'\t'+x['url'])
 print('COLORFUL2_PENDING_END')
 print('COLORFUL2_VALID_COUNT='+str(len(final)))
 print('COLORFUL2_RESULTS_JSON='+json.dumps(final,ensure_ascii=False))
 print('COLORFUL2_PENDING_JSON='+json.dumps(pending,ensure_ascii=False))

if __name__=='__main__': run()
