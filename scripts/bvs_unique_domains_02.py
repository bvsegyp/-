import requests,re,json,html,secrets,hashlib,sys,time
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup

HOME='https://bvsegypt.com/'
s=requests.Session(); s.headers.update({'User-Agent':'Mozilla/5.0 BVSEditorial/2.0'})

TITLES=[
'أسعار ماكينات عد النقود في مصر وكيف تختار الأنسب',
'أفضل ماكينة عد فلوس للمحلات والسوبر ماركت',
'أجهزة كشف العملات المزورة ودورها في حماية الخزينة',
'متى تحتاج إلى صيانة ماكينة عد النقود',
'أسباب أخطاء العد في ماكينات عد الفلوس وكيف تقللها',
'مقارنة شراء وتأجير ماكينة عد النقود للشركات',
'كيفية تنظيف حساس ماكينة عد النقود والمحافظة على الدقة',
'اختيار ماكينة عد نقود للاستخدام المكثف في الشركات',
'الفرق بين عد النقود وفرزها داخل بيئة العمل',
'كيف تقلل أخطاء الكاش باستخدام معدات عد النقود',
'إدارة الخزينة اليومية بسرعة ودقة أكبر',
'أهم مواصفات ماكينة عد النقود قبل الشراء',
'متى تحتاج جهاز كشف تزوير مستقل بجانب ماكينة العد',
'دليل صيانة ماكينات عد النقود للشركات والمحلات',
'حلول عملية لتنظيم النقد داخل نقاط البيع',
'كيفية تدريب الموظفين على استخدام ماكينة عد النقود',
'اختيار معدات عد النقد المناسبة لحجم النشاط',
'كيف ترفع كفاءة التعامل مع النقد داخل شركتك'
]

def article(i):
 t=TITLES[i%len(TITLES)]
 return f'''# {t}

التعامل مع النقد داخل الشركات والمحلات يحتاج إلى نظام واضح يقلل الأخطاء ويوفر الوقت، خصوصًا عندما يرتفع عدد المعاملات اليومية. الاعتماد على العد اليدوي وحده قد يؤدي إلى إعادة العد أكثر من مرة ويزيد الضغط على الموظفين عند إغلاق الخزينة، لذلك أصبحت ماكينات عد وفرز النقد وأجهزة كشف العملات أدوات عملية في كثير من الأنشطة.

## ابدأ من حجم الاستخدام الفعلي

قبل شراء أي ماكينة يجب معرفة متوسط عدد الأوراق النقدية التي يتم التعامل معها يوميًا وعدد ساعات التشغيل المتوقعة. الاستخدام الخفيف يختلف عن الاستخدام المكثف في شركات التحصيل أو المتاجر الكبيرة أو المؤسسات التي تستقبل كميات نقدية كبيرة. اختيار جهاز أعلى من الحاجة قد يزيد التكلفة دون فائدة حقيقية، بينما اختيار جهاز أقل من المطلوب قد يؤدي إلى بطء التشغيل وكثرة الأعطال.

## الدقة وكشف الأوراق المشتبه بها

سرعة العد مهمة، لكنها ليست المعيار الوحيد. من الأفضل الاهتمام بثبات نتائج العد، وجود تقنيات مساعدة على كشف الأوراق المشتبه بها، وسهولة التعامل مع التنبيهات. يمكن التعرف على حلول متخصصة في معدات التعامل مع النقد من خلال [BVS Egypt]({HOME}) ومقارنة الخيارات وفق طبيعة النشاط وحجم الاستخدام.

## الصيانة تؤثر مباشرة في الأداء

الحساسات ومسار سحب الأوراق تتعرض للأتربة وبقايا الورق مع الاستخدام المستمر. التنظيف الدوري والفحص عند ظهور أخطاء متكررة يساعدان على الحفاظ على دقة الماكينة. كما أن الاستمرار في تشغيل الجهاز رغم ظهور أصوات غير طبيعية أو أخطاء سحب متكررة قد يحول مشكلة بسيطة إلى عطل أكبر.

## تنظيم إجراءات العمل حول الجهاز

وجود ماكينة جيدة لا يكفي إذا لم توجد طريقة تشغيل واضحة. من المفيد تحديد مسؤولية الموظف الذي يستخدم الجهاز، طريقة التعامل مع الأوراق التي يرفضها، عدد مرات المراجعة المطلوبة، وكيفية تسجيل الفروق إن ظهرت. بهذه الطريقة تصبح الماكينة جزءًا من نظام رقابة نقدية وليس مجرد أداة للعد السريع.

## راجع خدمة ما بعد البيع

عند المقارنة بين الأجهزة، من المهم النظر إلى توافر الصيانة وقطع الغيار والدعم الفني، وليس السعر الأولي فقط. تكلفة التوقف عن العمل بسبب عطل قد تكون أكبر من فرق السعر بين جهازين، لذلك تساعد خدمة ما بعد البيع في تقليل مخاطر التشغيل على المدى الطويل.

## الخلاصة

الاختيار الصحيح يبدأ بفهم حجم التعامل النقدي، ثم مقارنة السرعة والدقة ووظائف الكشف والتحمل وسهولة الصيانة. عندما تتكامل الماكينة مع إجراءات تشغيل واضحة وصيانة منتظمة، يمكن تقليل وقت إغلاق الخزينة وتحسين دقة المراجعة اليومية ورفع كفاءة الفريق.'''

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
 return '<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>BVS Egypt</title></head><body><main style="max-width:900px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.9">'+''.join(out)+'</main></body></html>'

def extract(d):
 if isinstance(d,dict):
  for k in ['url','share_url','shareUrl','publicUrl','public_url','previewUrl','pageUrl','siteUrl','link']:
   v=d.get(k)
   if isinstance(v,str) and v.startswith('http'): return v
  for v in d.values():
   u=extract(v)
   if u:return u
 if isinstance(d,list):
  for v in d:
   u=extract(v)
   if u:return u
 return ''

def verify(name,u):
 if not u or not u.startswith('http'): return None
 try:
  r=s.get(u,timeout=35,allow_redirects=True)
  soup=BeautifulSoup(r.text,'html.parser')
  hrefs=[a.get('href','') for a in soup.find_all('a',href=True) if 'bvsegypt.com' in a.get('href','').lower()]
  ok=r.status_code<400 and len(hrefs)>=1
  print('VERIFY',name,r.status_code,'HREFS',len(hrefs),r.url)
  return r.url if ok else None
 except Exception as e:
  print('VERIFY_ERR',name,repr(e)); return None

def add(results,name,u):
 v=verify(name,u)
 if v: results.append({'source':name,'domain':urlparse(v).netloc.lower().removeprefix('www.'),'url':v})

def pjson(url,payload,**kwargs):
 r=s.post(url,json=payload,timeout=35,**kwargs); print('POST',url,r.status_code,r.text[:300].replace('\n',' '))
 if not r.ok:return ''
 try:return extract(r.json())
 except:return ''

def run():
 results=[]
 # emdee.info
 try:
  md=article(0); r=s.post('https://emdee.info/api/',data=md.encode(),headers={'Content-Type':'text/markdown'},timeout=35); print('EMDEE',r.status_code,r.text[:250]);
  try:u=extract(r.json())
  except:u=r.text.strip().strip('"')
  add(results,'emdee.info',u)
 except Exception as e: print('EMDEE_ERR',repr(e))
 # display.dev/public.dsp.so with ASCII name
 try:
  h=md_to_html(article(1)); r=s.post('https://api.display.dev/v1/public/artifacts',files={'file':('bvs-money-guide.html',h.encode(),'text/html')},data={'name':'bvs-money-guide'},timeout=35); print('DISPLAY',r.status_code,r.text[:300]);
  try:u=extract(r.json())
  except:u=''
  add(results,'public.dsp.so',u)
 except Exception as e: print('DISPLAY_ERR',repr(e))
 # mdshare.live public view link
 try:
  md=article(2); d=s.post('https://mdshare.live/api/documents',data=md.encode(),headers={'Content-Type':'text/markdown'},timeout=35).json(); doc=d.get('document_id',''); key=d.get('admin_key',''); u=''
  if doc and key:
   q=s.post(f'https://mdshare.live/api/d/{doc}/links?key={key}',json={'permission':'view','label':'public-view'},timeout=35); print('MDSHARE_LINK',q.status_code,q.text[:300]);
   try:u=extract(q.json())
   except:u=''
  add(results,'mdshare.live',u)
 except Exception as e: print('MDSHARE_ERR',repr(e))
 # pastebox.ai
 try:
  u=pjson('https://lfdekutkxwsczpasjgsg.supabase.co/functions/v1/create-share',{'content':article(3),'title':TITLES[3],'language':'markdown','content_type':'text','expiration':'1M','exposure':'public','source':'api'}); add(results,'pastebox.ai',u)
 except Exception as e: print('PASTEBOX_ERR',repr(e))
 # pastepile
 try:
  u=pjson('https://www.pastepile.com/api/public/pastes',{'title':TITLES[4],'content':article(4),'language':'markdown','expiry':'1mo','visibility':'public'}); add(results,'pastepile.com',u)
 except Exception as e: print('PASTEPILE_ERR',repr(e))
 # dpaste.org
 try:
  r=s.post('https://dpaste.org/api/',data={'content':article(5),'lexer':'_markdown','format':'json','expires':'never'},timeout=35); print('DPASTE',r.status_code,r.text[:250]);
  try:u=extract(r.json())
  except:u=r.text.strip().strip('"')
  add(results,'dpaste.org',u)
 except Exception as e: print('DPASTE_ERR',repr(e))
 # pastehtml.dev
 try:
  h=md_to_html(article(6)); r=s.post('https://pastehtml.dev/api/pastes',files={'file':('bvs-cash-guide.html',h.encode(),'text/html')},timeout=40); print('PASTEHTML',r.status_code,r.text[:250]);
  try:u=extract(r.json())
  except:u=''
  add(results,'pastehtml.dev',u)
 except Exception as e: print('PASTEHTML_ERR',repr(e))
 # pubmark.site
 try:
  r=s.post('https://pubmark.site/api/documents',json={'title':TITLES[7]},timeout=35); print('PUBMARK_CREATE',r.status_code,r.text[:250]); d=r.json(); sid=d.get('secretId'); u=''
  if sid:
   s.put('https://pubmark.site/api/documents/'+sid,json={'content':article(7),'title':TITLES[7],'theme':'clean','colorPreset':'blue'},timeout=35)
   p=s.post('https://pubmark.site/api/documents/'+sid+'/publish',json={},timeout=35); print('PUBMARK_PUB',p.status_code,p.text[:250]); slug=(p.json() if p.ok else {}).get('slug'); u='https://pubmark.site/p/'+slug if slug else ''
  add(results,'pubmark.site',u)
 except Exception as e: print('PUBMARK_ERR',repr(e))
 # mdlib.dev
 try:
  u=pjson('https://mdlib.dev/v1/docs',{'markdown':article(8),'title':TITLES[8],'is_public':True}); add(results,'mdlib.dev',u)
 except Exception as e: print('MDLIB_ERR',repr(e))
 # jotbird
 try:
  r=s.post('https://api.jotbird.com/trial/publish',json={'markdown':article(9),'title':TITLES[9]},headers={'User-Agent':'jotbird-vscode/1.0.0'},timeout=35); print('JOTBIRD',r.status_code,r.text[:250]);
  try:u=extract(r.json())
  except:u=''
  add(results,'jotbird.com',u)
 except Exception as e: print('JOTBIRD_ERR',repr(e))
 # showyourcode
 try:
  h=md_to_html(article(10)); d=s.post('https://www.showyourcode.app/api/works',json={'htmlContent':h,'title':TITLES[10],'topicIds':[],'type':'html','templateId':None},timeout=35); print('SHOWCODE',d.status_code,d.text[:300]); j=d.json() if d.ok else {}; uid=j.get('uuid'); u='https://www.showyourcode.app/share/'+uid if uid else ''; add(results,'showyourcode.app',u)
 except Exception as e: print('SHOWCODE_ERR',repr(e))
 # pagepaste old direct form
 try:
  h=md_to_html(article(11)); r=s.post('https://pagepaste.com/',data={'html':h,'title':TITLES[11]},timeout=35,allow_redirects=True); print('PAGEPASTE',r.status_code,r.url); c=[]
  if r.url.rstrip('/')!='https://pagepaste.com': c.append(r.url)
  c += re.findall(r'https://[A-Za-z0-9.-]*pagepaste\.com/[A-Za-z0-9_./?=-]+',r.text,re.I)
  for u in c:
   if verify('pagepaste.com',u): results.append({'source':'pagepaste.com','domain':urlparse(u).netloc.lower().removeprefix('www.'),'url':u}); break
 except Exception as e: print('PAGEPASTE_ERR',repr(e))
 # oneclicklive
 try:
  h=md_to_html(article(12)); r=s.post('https://oneclicklive.app/api/deploy',json={'code':h,'title':TITLES[12]},timeout=60); print('ONECLICK',r.status_code,r.text[:300]); d=r.json() if r.ok else {}; u=d.get('url') or ('https://'+d.get('slug','')+'.oneclicklive.app' if d.get('slug') else '');
  for _ in range(4):
   if verify('oneclicklive.app',u): results.append({'source':'oneclicklive.app','domain':urlparse(u).netloc.lower().removeprefix('www.'),'url':u}); break
   time.sleep(2)
 except Exception as e: print('ONECLICK_ERR',repr(e))
 # botsite.dev
 try:
  h=md_to_html(article(13)); r=s.post('https://botsite.dev/api/v1/sites',data=h.encode(),headers={'Content-Type':'text/html'},timeout=35); print('BOTSITE',r.status_code,r.text[:250]);
  try:u=extract(r.json())
  except:u=''
  add(results,'botsite.dev',u)
 except Exception as e: print('BOTSITE_ERR',repr(e))
 # stacktr.ee
 try:
  h=md_to_html(article(14)); r=s.post('https://api.stacktr.ee/sites',files={'file':('index.html',h.encode(),'text/html')},timeout=40); print('STACKTREE',r.status_code,r.text[:250]);
  try:u=extract(r.json())
  except:u=''
  add(results,'stacktr.ee',u)
 except Exception as e: print('STACKTREE_ERR',repr(e))
 # here.now
 try:
  h=md_to_html(article(15)); b=h.encode(); sha=hashlib.sha256(b).hexdigest(); d=s.post('https://here.now/api/v1/publish',headers={'X-HereNow-Client':'chatgpt/direct-api','Content-Type':'application/json'},json={'files':[{'path':'index.html','size':len(b),'contentType':'text/html; charset=utf-8','hash':sha}],'viewer':{'title':TITLES[15]}},timeout=40).json(); site=d.get('siteUrl',''); up=d.get('upload') or {}; ups=up.get('uploads') or []
  if ups: requests.put(ups[0]['url'],data=b,headers=ups[0].get('headers') or {'Content-Type':'text/html; charset=utf-8'},timeout=40)
  if up.get('finalizeUrl') and up.get('versionId'): s.post(up['finalizeUrl'],json={'versionId':up['versionId']},timeout=35)
  add(results,'here.now',site)
 except Exception as e: print('HERENOW_ERR',repr(e))
 # Rentry
 try:
  rs=requests.Session(); rs.headers.update({'User-Agent':'Mozilla/5.0'}); rs.get('https://rentry.co/',timeout=35); csrf=rs.cookies.get('csrftoken',''); rr=rs.post('https://rentry.co/api/new',data={'csrfmiddlewaretoken':csrf,'text':article(16),'edit_code':secrets.token_urlsafe(12),'url':''},headers={'Referer':'https://rentry.co/'},timeout=35); print('RENTRY',rr.status_code,rr.text[:250]); d=rr.json() if rr.ok else {}; u=d.get('url',''); add(results,'rentry.co',u)
 except Exception as e: print('RENTRY_ERR',repr(e))
 # PublishTo.us form
 try:
  r=s.get('https://publishto.us/new?lang=en',timeout=35); soup=BeautifulSoup(r.text,'html.parser'); form=soup.find('form'); u=''
  if form:
   action=urljoin(r.url,form.get('action') or r.url); data={}
   for x in form.find_all(['input','textarea']):
    n=x.get('name');
    if n:data[n]=x.get('value') or ''
   for k in list(data):
    lk=k.lower()
    if 'title' in lk:data[k]=TITLES[17]
    elif 'body' in lk or 'content' in lk or 'text' in lk:data[k]=article(17)
    elif 'keyword' in lk:data[k]='ماكينات عد النقود'
   q=s.post(action,data=data,allow_redirects=True,timeout=35); print('PUBLISHTOUS',q.status_code,q.url); u=q.url if '/new' not in q.url else ''
  add(results,'publishto.us',u)
 except Exception as e: print('PUBLISHTOUS_ERR',repr(e))
 # de-duplicate root host families, preserve only verified
 final=[]; seen=set()
 for x in results:
  d=x['domain']
  root=d
  if root not in seen: seen.add(root); final.append(x)
 print('BVS2_RESULTS_BEGIN')
 for x in final: print(x['domain']+'\t'+x['url'])
 print('BVS2_RESULTS_END')
 print('BVS2_VALID_COUNT='+str(len(final)))
 print('BVS2_RESULTS_JSON='+json.dumps(final,ensure_ascii=False))

if __name__=='__main__': run()
