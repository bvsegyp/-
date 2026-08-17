import requests,re,json,html,secrets,time
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup

HOME='https://colorfulcloudco.com/'
LINKS=[
 ('أفضل شركة تنظيف في الرياض','https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'),
 ('أفضل شركة تنظيف شقق بالرياض','https://colorfulcloudco.com/افضل-شركة-تنظيف-شقق-بالرياض/'),
 ('تنظيف منازل بالساعة بالرياض','https://colorfulcloudco.com/تنظيف-منازل-بالساعة-بالرياض/'),
 ('شركات تنظيف في الرياض','https://colorfulcloudco.com/شركات-تنظيف-في-الرياض/'),
 ('شركة غيمة ملونة للتنظيف','https://colorfulcloudco.com/'),
]
TITLES=[
 'أفضل شركة تنظيف في الرياض وكيف تختار الخدمة المناسبة لمنزلك',
 'دليل تنظيف المنازل في الرياض من الحجز حتى استلام المكان',
 'كيف تختار شركة تنظيف شقق بالرياض بمعايير احترافية',
 'تنظيف المنازل والفلل في الرياض بخطة عملية ونتائج أفضل',
 'معايير مقارنة شركات التنظيف في الرياض قبل طلب الخدمة',
 'متى تحتاج تنظيف عميق للمنزل في الرياض وكيف تستعد له',
 'خدمات تنظيف الشقق بالرياض وأهم التفاصيل قبل الحجز',
 'تنظيف المنزل بالساعة في الرياض ومتى يكون الخيار الأنسب',
 'دليل العناية بالمنزل بعد التنظيف الاحترافي في الرياض',
 'كيف تحافظ على نظافة البيت بين زيارات شركة التنظيف',
 'تنظيف الفلل والمنازل الكبيرة في الرياض بخطوات منظمة',
 'اختيار فريق تنظيف محترف بالرياض دون الاعتماد على السعر فقط',
 'أفضل طرق تقييم خدمة تنظيف منزلية قبل تكرار الحجز',
]

BASE_SECTIONS=[
 ('ابدأ بتحديد احتياج المكان','قبل طلب أي خدمة تنظيف من الأفضل تحديد المساحة ونوع العقار وأهم المناطق التي تحتاج إلى عناية أكبر. الشقق الصغيرة تختلف عن الفلل متعددة الطوابق، كما أن التنظيف الدوري يختلف عن التنظيف العميق بعد التشطيب أو الانتقال. كتابة قائمة قصيرة بالأولويات تساعد الفريق على توزيع الوقت بشكل أفضل وتقلل احتمالات إغفال التفاصيل.'),
 ('الجودة تبدأ من طريقة التنفيذ','الخدمة الاحترافية لا تعني استخدام منظفات قوية في كل مكان، بل اختيار الطريقة المناسبة لكل خامة. الرخام والخشب والزجاج والأقمشة تحتاج إلى مواد وأدوات مختلفة، كما أن إزالة البقع يجب أن تتم تدريجيًا حتى لا يتغير اللون أو يتضرر السطح. هذه التفاصيل هي التي تفرق بين التنظيف السريع والتنظيف المنظم.'),
 ('المطبخ والحمامات تحتاج عناية خاصة','المطابخ والحمامات من أكثر المناطق التي تحتاج إلى خطة واضحة بسبب الدهون والرطوبة وكثرة الاستخدام. يبدأ العمل عادة بإزالة الأتربة والمخلفات ثم تنظيف الأسطح والأرضيات والتعامل مع البقع الصعبة، وبعدها تأتي مرحلة التعقيم المناسبة. ترتيب الخطوات يمنع إعادة اتساخ المناطق التي تم تنظيفها بالفعل.'),
 ('اختيار الخدمة حسب الوقت المتاح','بعض العملاء يحتاجون تنظيفًا كاملًا في يوم واحد، بينما يفضل آخرون تقسيم العمل على زيارات دورية أو الاستفادة من خدمة بالساعة. الاختيار الصحيح يعتمد على مساحة المنزل وعدد الغرف ومستوى الاتساخ والميزانية. المهم أن يكون نطاق الخدمة واضحًا قبل بدء العمل حتى تكون التوقعات متوافقة مع الوقت المتاح.'),
 ('قارن التفاصيل وليس السعر فقط','عند مقارنة أكثر من شركة، راجع ما يتضمنه السعر: عدد أفراد الفريق، مدة العمل، المواد المستخدمة، المعدات، إمكانية إضافة تنظيف الكنب أو السجاد، وطريقة التعامل مع الملاحظات بعد التنفيذ. السعر المنخفض قد يكون مناسبًا إذا كان نطاق الخدمة واضحًا، لكنه لا يكفي وحده للحكم على جودة التجربة.'),
 ('التجهيز المسبق يوفر وقت التنفيذ','ترتيب الأغراض الشخصية وإخلاء الأسطح قدر الإمكان قبل وصول فريق التنظيف يساعد على بدء العمل مباشرة. كما أن تحديد الغرف ذات الأولوية والمناطق الحساسة يختصر كثيرًا من الوقت. في المنازل الكبيرة من المفيد تقسيم العمل إلى مناطق حتى يتم إنهاء كل جزء ومراجعته قبل الانتقال إلى الجزء التالي.'),
 ('بعد انتهاء الخدمة راجع التفاصيل','المراجعة النهائية مهمة للتأكد من الوصول إلى النتيجة المطلوبة. راجع الأرضيات والزوايا والأسطح والمطبخ والحمامات، وتأكد من إعادة الأثاث إلى مكانه عند الاتفاق على ذلك. إذا كانت هناك ملاحظة بسيطة فمن الأفضل إبلاغ الفريق فورًا حتى تتم معالجتها قبل المغادرة.'),
 ('الاستمرارية تقلل الحاجة للتنظيف الشاق','الحفاظ على روتين بسيط بعد التنظيف الاحترافي يجعل المنزل مرتبًا لفترة أطول. إزالة الغبار بانتظام، تنظيف الانسكابات فور حدوثها، تهوية المكان، وتنظيم الأدوات المستخدمة يوميًا يقلل تراكم الأوساخ. كما يمكن تحديد زيارة دورية حسب عدد أفراد الأسرة وطبيعة الاستخدام.'),
]

def article(i):
    title=TITLES[i%len(TITLES)]
    intro=('اختيار خدمة تنظيف مناسبة في الرياض يحتاج إلى موازنة بين الخبرة وجودة التنفيذ ووضوح نطاق العمل. '
           'هذا الدليل يشرح خطوات عملية تساعدك على تقييم الخدمة وتنظيم عملية التنظيف من البداية للنهاية، سواء كان المطلوب شقة أو منزلًا كبيرًا أو فيلا أو تنظيفًا دوريًا.')
    sections=list(BASE_SECTIONS)
    # rotate sections to keep articles distinct
    shift=i%len(sections); sections=sections[shift:]+sections[:shift]
    parts=[f'# {title}',intro]
    link_blocks=[
      f'عند البحث عن خدمة شاملة، يمكن مراجعة دليل [{LINKS[0][0]}]({LINKS[0][1]}) لمعرفة أهم المعايير التي تساعد في المقارنة قبل الحجز.',
      f'ولمن يسكن في شقة، يفيد الاطلاع على تفاصيل [{LINKS[1][0]}]({LINKS[1][1]}) لفهم طبيعة الخدمات المناسبة للوحدات السكنية.',
      f'أما إذا كان المطلوب مرونة أكبر في الوقت، فخدمة [{LINKS[2][0]}]({LINKS[2][1]}) تساعد على تخصيص عدد الساعات والمهام حسب الاحتياج.',
      f'وقبل اتخاذ القرار النهائي، يمكن مقارنة الخيارات من خلال دليل [{LINKS[3][0]}]({LINKS[3][1]}) ومعرفة الفروق في نطاق الخدمات.',
      f'كما يمكن التعرف على نطاق خدمات [{LINKS[4][0]}]({LINKS[4][1]}) ومراجعة الخدمات المتاحة للمنازل والمنشآت.',
    ]
    for idx,(h,p) in enumerate(sections):
        parts += [f'## {h}',p]
        if idx < 5: parts.append(link_blocks[idx])
    parts += ['## خلاصة عملية','أفضل نتيجة تبدأ من تحديد المطلوب بدقة، اختيار مزود خدمة واضح، وتجهيز المكان قبل وصول الفريق. بعد التنفيذ تأتي المراجعة النهائية ثم الحفاظ على روتين بسيط يمنع تراكم الأوساخ بسرعة. بهذه الطريقة يصبح التنظيف الاحترافي استثمارًا في الراحة والوقت وليس مجرد مهمة مؤقتة.']
    return '\n\n'.join(parts)

def md_to_html(md):
    out=[]
    for b in re.split(r'\n\s*\n',md):
        b=b.strip()
        if not b: continue
        if b.startswith('# '): out.append('<h1>'+html.escape(b[2:])+'</h1>'); continue
        if b.startswith('## '): out.append('<h2>'+html.escape(b[3:])+'</h2>'); continue
        parts=[];pos=0
        for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',b):
            parts.append(html.escape(b[pos:m.start()])); parts.append('<a href="'+html.escape(m.group(2),quote=True)+'">'+html.escape(m.group(1))+'</a>'); pos=m.end()
        parts.append(html.escape(b[pos:])); out.append('<p>'+''.join(parts).replace('\n',' ')+'</p>')
    return '<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>دليل تنظيف الرياض</title></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,Tahoma,sans-serif;line-height:2;color:#222">'+''.join(out)+'</main></body></html>'

def extract(obj):
    vals=[]
    def walk(x):
        if isinstance(x,str): vals.extend(re.findall(r'https?://[^\s"\'<>]+',x))
        elif isinstance(x,dict):
            for v in x.values(): walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
    walk(obj)
    return [v.rstrip('.,);}') for v in vals]

def pick(obj, domains=()):
    vals=extract(obj)
    for d in domains:
        for v in vals:
            if d in v:return v
    return vals[0] if vals else ''

s=requests.Session(); s.headers.update({'User-Agent':'Mozilla/5.0 ColorfulCloudEditorial/5.0'})
results=[]
USED={'shipped.page','aired.sh','xdr.no','yeetit.site','draftlet.io','yourwebs.app','telegra.ph','shareyourhtml.com','md.page','markdown.page','yeet.md','mdview.io','output.pub','quicky.page','thethings.ai','unmarkdown.com','leafmill.net','htmldrop.link','shipsite.co','pubmark.site','here.now','htmlshare.net','zerodeploy.app','sitebin.io','based.page','pastebox.ai','ht-ml.app','pitchey.app'}

def root(host):
    h=host.lower().removeprefix('www.')
    for p in USED:
        if h==p or h.endswith('.'+p): return p
    parts=h.split('.')
    return '.'.join(parts[-2:]) if len(parts)>=2 else h

def verify(name,u):
    if not u or not u.startswith('http'): return False
    try:
        r=s.get(u,timeout=40,allow_redirects=True)
        soup=BeautifulSoup(r.text,'html.parser')
        hrefs=[a.get('href','') for a in soup.find_all('a',href=True) if 'colorfulcloudco.com' in a.get('href','').lower()]
        noindex=('noindex' in r.headers.get('x-robots-tag','').lower()) or bool(soup.find('meta',attrs={'name':re.compile('robots',re.I),'content':re.compile('noindex',re.I)}))
        prov=root(urlparse(r.url).netloc)
        print(f'VERIFY {name} STATUS={r.status_code} URL={r.url} HREFS={len(hrefs)} NOINDEX={int(noindex)} PROVIDER={prov}')
        if r.status_code<400 and len(hrefs)>=5 and not noindex and prov not in USED:
            USED.add(prov); results.append({'source':name,'provider':prov,'url':r.url,'hrefs':len(hrefs)}); print('VALID',name,r.url); return True
    except Exception as e: print('VERIFY_ERR',name,repr(e))
    return False

def pjson(url,payload,domains=()):
    r=s.post(url,json=payload,timeout=45); print('POST',url,r.status_code,r.text[:350].replace('\n',' '))
    if not r.ok:return ''
    try:return pick(r.json(),domains)
    except:return pick(r.text,domains)

# 1 public.dsp.so
try:
    h=md_to_html(article(0)); r=s.post('https://api.display.dev/v1/public/artifacts',files={'file':('riyadh-cleaning-guide.html',h.encode(),'text/html')},data={'name':'riyadh-cleaning-five-links'},timeout=45); print('DISPLAY',r.status_code,r.text[:400]); d=r.json() if r.ok else r.text; verify('public.dsp.so',pick(d,('public.dsp.so','dsp.so')))
except Exception as e: print('DISPLAY_ERR',repr(e))

# 2 mdshare.live
try:
    md=article(1); d=s.post('https://mdshare.live/api/documents',data=md.encode(),headers={'Content-Type':'text/markdown'},timeout=45).json(); doc=d.get('document_id',''); key=d.get('admin_key',''); u=''
    if doc and key:
        q=s.post(f'https://mdshare.live/api/d/{doc}/links?key={key}',json={'permission':'view','label':'public-view'},timeout=45); print('MDSHARE_LINK',q.status_code,q.text[:400]); u=pick(q.json() if q.ok else q.text,('mdshare.live',))
    verify('mdshare.live',u)
except Exception as e: print('MDSHARE_ERR',repr(e))

# 3 pastepile.com
try:
    u=pjson('https://www.pastepile.com/api/public/pastes',{'title':TITLES[2],'content':article(2),'language':'markdown','expiry':'1mo','visibility':'public'},('pastepile.com',)); verify('pastepile.com',u)
except Exception as e: print('PASTEPILE_ERR',repr(e))

# 4 dpaste.org
try:
    r=s.post('https://dpaste.org/api/',data={'content':article(3),'lexer':'_markdown','format':'json','expires':'never'},timeout=45); print('DPASTE',r.status_code,r.text[:350]); d=r.json() if r.ok else r.text; verify('dpaste.org',pick(d,('dpaste.org',)))
except Exception as e: print('DPASTE_ERR',repr(e))

# 5 pastehtml.dev
try:
    h=md_to_html(article(4)); r=s.post('https://pastehtml.dev/api/pastes',files={'file':('riyadh-cleaning.html',h.encode(),'text/html')},timeout=45); print('PASTEHTML',r.status_code,r.text[:400]); d=r.json() if r.ok else r.text; verify('pastehtml.dev',pick(d,('pastehtml.dev',)))
except Exception as e: print('PASTEHTML_ERR',repr(e))

# 6 mdlib.dev
try:
    u=pjson('https://mdlib.dev/v1/docs',{'markdown':article(5),'title':TITLES[5],'is_public':True},('mdlib.dev',)); verify('mdlib.dev',u)
except Exception as e: print('MDLIB_ERR',repr(e))

# 7 jotbird.com
try:
    r=s.post('https://api.jotbird.com/trial/publish',json={'markdown':article(6),'title':TITLES[6]},headers={'User-Agent':'jotbird-vscode/1.0.0'},timeout=45); print('JOTBIRD',r.status_code,r.text[:400]); d=r.json() if r.ok else r.text; verify('jotbird.com',pick(d,('jotbird.com',)))
except Exception as e: print('JOTBIRD_ERR',repr(e))

# 8 showyourcode.app
try:
    h=md_to_html(article(7)); r=s.post('https://www.showyourcode.app/api/works',json={'htmlContent':h,'title':TITLES[7],'topicIds':[],'type':'html','templateId':None},timeout=45); print('SHOWCODE',r.status_code,r.text[:350]); j=r.json() if r.ok else {}; uid=j.get('uuid'); u='https://www.showyourcode.app/share/'+uid if uid else ''; verify('showyourcode.app',u)
except Exception as e: print('SHOWCODE_ERR',repr(e))

# 9 pagepaste.com
try:
    h=md_to_html(article(8)); r=s.post('https://pagepaste.com/',data={'html':h,'title':TITLES[8]},timeout=45,allow_redirects=True); print('PAGEPASTE',r.status_code,r.url); c=[]
    if r.url.rstrip('/')!='https://pagepaste.com': c.append(r.url)
    c += re.findall(r'https://[A-Za-z0-9.-]*pagepaste\.com/[A-Za-z0-9_./?=-]+',r.text,re.I)
    for u in c:
        if verify('pagepaste.com',u): break
except Exception as e: print('PAGEPASTE_ERR',repr(e))

# 10 stacktr.ee
try:
    h=md_to_html(article(9)); r=s.post('https://api.stacktr.ee/sites',files={'file':('index.html',h.encode(),'text/html')},timeout=45); print('STACKTREE',r.status_code,r.text[:400]); d=r.json() if r.ok else r.text; verify('stacktr.ee',pick(d,('stacktr.ee',)))
except Exception as e: print('STACKTREE_ERR',repr(e))

# 11 rentry.co
try:
    rs=requests.Session(); rs.headers.update({'User-Agent':'Mozilla/5.0'}); rs.get('https://rentry.co/',timeout=45); csrf=rs.cookies.get('csrftoken',''); rr=rs.post('https://rentry.co/api/new',data={'csrfmiddlewaretoken':csrf,'text':article(10),'edit_code':secrets.token_urlsafe(12),'url':''},headers={'Referer':'https://rentry.co/'},timeout=45); print('RENTRY',rr.status_code,rr.text[:400]); d=rr.json() if rr.ok else {}; verify('rentry.co',d.get('url',''))
except Exception as e: print('RENTRY_ERR',repr(e))

# 12 publishto.us
try:
    r=s.get('https://publishto.us/new?lang=en',timeout=45); soup=BeautifulSoup(r.text,'html.parser'); form=soup.find('form'); u=''
    if form:
        action=urljoin(r.url,form.get('action') or r.url); data={}
        for x in form.find_all(['input','textarea']):
            n=x.get('name')
            if n:data[n]=x.get('value') or ''
        for k in list(data):
            lk=k.lower()
            if 'title' in lk:data[k]=TITLES[11]
            elif 'body' in lk or 'content' in lk or 'text' in lk:data[k]=article(11)
            elif 'keyword' in lk:data[k]='أفضل شركة تنظيف في الرياض'
        q=s.post(action,data=data,allow_redirects=True,timeout=45); print('PUBLISHTO',q.status_code,q.url); u=q.url if '/new' not in q.url else ''
    verify('publishto.us',u)
except Exception as e: print('PUBLISHTO_ERR',repr(e))

# 13 post-easy.org
try:
    r=s.get('https://post-easy.org/post',timeout=45); soup=BeautifulSoup(r.text,'html.parser'); form=None
    for f in soup.find_all('form'):
        names={x.get('name') for x in f.find_all(['input','textarea','select']) if x.get('name')}
        if 'content' in names and 'title' in names: form=f; break
    if form:
        action=urljoin(r.url,form.get('action') or r.url); data={}
        for inp in form.find_all('input'):
            n=inp.get('name'); typ=(inp.get('type') or 'text').lower()
            if n and typ not in ('submit','button','image','file'): data[n]=inp.get('value','')
        data['title']=TITLES[12]; data['content']=article(12)
        if form.find(attrs={'name':'category'}): data['category']='Home'
        if form.find(attrs={'name':'author'}): data['author']='Cleaning Editorial'
        q=s.post(action,data=data,allow_redirects=True,timeout=45); print('POSTEASY',q.status_code,q.url); verify('post-easy.org',q.url if q.url.rstrip('/')!='https://post-easy.org/post' else '')
except Exception as e: print('POSTEASY_ERR',repr(e))

print('COLORFUL5_RESULTS_BEGIN')
for x in results: print(x['source']+'\t'+x['url']+'\tHREFS='+str(x['hrefs']))
print('COLORFUL5_RESULTS_END')
print('COLORFUL5_VALID_COUNT='+str(len(results)))
print('COLORFUL5_RESULTS_JSON='+json.dumps(results,ensure_ascii=False))
