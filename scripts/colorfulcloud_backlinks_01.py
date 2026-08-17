import requests,re,json,time,hashlib
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup

TARGET='https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'
ANCHOR='أفضل شركة تنظيف في الرياض'
HOME='https://colorfulcloudco.com/'

TITLE='أفضل شركة تنظيف في الرياض: دليل اختيار خدمة تنظيف احترافية'
PARAS=[
('ما الذي يميز شركة التنظيف المحترفة؟','اختيار شركة تنظيف مناسبة في الرياض لا يعتمد على السعر فقط، بل على جودة التنفيذ، خبرة فريق العمل، نوع المعدات المستخدمة، الالتزام بالمواعيد، والقدرة على التعامل مع تفاصيل المنزل أو المكتب دون إهمال. الخدمة الاحترافية تبدأ بتقييم احتياج المكان ثم تحديد الأدوات والمواد المناسبة لكل سطح حتى تكون النتيجة أكثر أمانًا واستمرارية.'),
('تنظيف المنازل يحتاج خطة واضحة','المنازل تختلف من حيث المساحة ونوعية الأرضيات والأثاث ووجود أطفال أو حيوانات أليفة، لذلك يجب أن تكون خطة التنظيف مرنة. من المهم تحديد المناطق ذات الأولوية مثل المطابخ والحمامات والمجالس وغرف النوم، ثم الانتقال إلى التفاصيل مثل الأبواب والزوايا والأسطح المرتفعة. التنظيم الجيد يقلل الوقت ويرفع جودة النتيجة.'),
('أهمية المعدات ومواد التنظيف','المعدات الحديثة تساعد على إزالة الأتربة والبقع بكفاءة أعلى، لكن الأهم هو اختيار مادة مناسبة لكل سطح. استخدام مادة قوية بشكل عشوائي قد يضر الرخام أو الخشب أو الأقمشة. الشركة الجيدة تعرف متى تستخدم التنظيف العميق ومتى تعتمد على معالجة لطيفة تحافظ على الخامات وتمنح المكان مظهرًا نظيفًا دون آثار جانبية.'),
('كيف تقارن بين الشركات في الرياض؟','قبل الحجز من الأفضل مقارنة مستوى الخدمة وليس الإعلان فقط. راجع نوع الخدمات، وضوح السعر، طريقة التواصل، سرعة الاستجابة، تفاصيل ما يشمله الحجز، وهل توجد خدمات إضافية مثل تنظيف الكنب والسجاد أو التعقيم أو تنظيف ما بعد التشطيب. هذه التفاصيل تساعد العميل على اختيار مزود خدمة يناسب احتياجه الحقيقي.'),
('خدمات التنظيف المتخصصة','قد يحتاج العميل إلى تنظيف منزل كامل، فيلا، شقة، مكتب أو منشأة، كما قد تكون الحاجة مركزة على الكنب والسجاد أو الخزانات أو التكييف. كل نوع من هذه الخدمات يحتاج أدوات وخبرة مختلفة، لذلك الشركات التي تقدم نطاقًا واضحًا من الخدمات تستطيع عادةً التعامل مع الحالات المتنوعة بشكل أكثر تنظيمًا.'),
('الالتزام بالمواعيد وجودة التنفيذ','عامل الوقت مهم خصوصًا عند تجهيز منزل قبل مناسبة أو بعد تشطيب أو انتقال. لذلك من معايير الاختيار المهمة الالتزام بموعد الوصول، وضوح مدة التنفيذ، وعدد أفراد الفريق المناسب للمهمة. التنظيم الجيد يظهر في توزيع العمل ومراجعة التفاصيل قبل مغادرة الموقع.'),
('لماذا الخبرة المحلية في الرياض مهمة؟','العمل داخل الرياض يتطلب معرفة طبيعة الأحياء، أوقات الوصول، أنواع العقارات الشائعة، واحتياجات العملاء المختلفة بين الشقق والفلل والمكاتب. الخبرة المحلية تساعد على تقديم خدمة أكثر واقعية من حيث التوقيت والتجهيز وتحديد الفريق المناسب لكل مهمة.'),
('النتيجة الجيدة تبدأ من اختيار صحيح','من يريد نتيجة مريحة ومستقرة يجب أن يختار شركة تشرح الخدمة بوضوح وتلتزم بما تم الاتفاق عليه. يمكن لمن يبحث عن '+ANCHOR+' الاطلاع على دليل غيمة ملونة ومقارنة تفاصيل الخدمة المتاحة قبل اتخاذ قرار الحجز. الهدف في النهاية ليس تنفيذ تنظيف سريع فقط، بل الحصول على مستوى نظافة مناسب يحافظ على المكان ويوفر وقت العميل.'),
]

def html_page():
    out=[f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{TITLE}</title></head><body style="font-family:Arial,Tahoma,sans-serif;max-width:900px;margin:40px auto;padding:0 22px;line-height:2;color:#222">',f'<h1>{TITLE}</h1>','<p>البحث عن شركة تنظيف موثوقة في الرياض يحتاج إلى مقارنة حقيقية بين الجودة والخبرة ونطاق الخدمة، وليس الاعتماد على السعر وحده. هذا الدليل يوضح أهم المعايير العملية التي تساعد على اختيار خدمة تنظيف مناسبة للمنازل والفلل والمكاتب.</p>']
    for i,(h,p) in enumerate(PARAS):
        if i==7:
            p=p.replace(ANCHOR,f'<a href="{TARGET}">{ANCHOR}</a>')
        out.append(f'<h2>{h}</h2><p>{p}</p>')
    out.append(f'<p>للتعرف على نطاق الخدمات بشكل عام يمكن زيارة <a href="{HOME}">شركة غيمة ملونة للتنظيف</a>.</p>')
    out.append('</body></html>')
    return ''.join(out)

PAGE=html_page()
S=requests.Session(); S.headers.update({'User-Agent':'Mozilla/5.0 ColorfulCloudSEO/1.0'})
results=[]

def verify(name,u):
    if not u:return False
    try:
        r=S.get(u,timeout=45,allow_redirects=True)
        soup=BeautifulSoup(r.text,'html.parser')
        hits=[]
        for a in soup.find_all('a',href=True):
            if 'colorfulcloudco.com' in a['href'] and ANCHOR in a.get_text(' ',strip=True): hits.append(a)
        noindex='noindex' in r.headers.get('x-robots-tag','').lower() or bool(soup.find('meta',attrs={'name':re.compile('robots',re.I),'content':re.compile('noindex',re.I)}))
        print('VERIFY',name,r.status_code,r.url,'ANCHORS',len(hits),'NOINDEX',int(noindex))
        if r.status_code<400 and hits and not noindex:
            results.append({'source':name,'url':r.url}); return True
    except Exception as e: print('VERIFY_ERR',name,repr(e))
    return False

def find_url(obj, domains=()):
    vals=[]
    def walk(x):
        if isinstance(x,str): vals.extend(re.findall(r'https?://[^\s"\'<>]+',x))
        elif isinstance(x,dict):
            for v in x.values(): walk(v)
        elif isinstance(x,list):
            for v in x: walk(v)
    walk(obj)
    vals=[x.rstrip('.,);}') for x in vals]
    for d in domains:
        for x in vals:
            if d in x:return x
    return vals[0] if vals else ''

# 1 shipped.page via ship.page
try:
    r=S.post('https://ship.page/deploy',data=PAGE.encode(),headers={'Content-Type':'text/html; charset=utf-8'},timeout=60)
    print('SHIPPAGE',r.status_code,r.text[:500]); d=r.json() if r.ok else r.text; verify('shipped.page',find_url(d,('shipped.page','ship.page')))
except Exception as e: print('SHIPPAGE_ERR',repr(e))

# 2 aired.sh
try:
    r=S.post('https://aired.sh/api/publish',json={'html':PAGE},timeout=50); print('AIRED',r.status_code,r.text[:500]); d=r.json() if r.ok else r.text; verify('aired.sh',find_url(d,('aired.sh',)))
except Exception as e: print('AIRED_ERR',repr(e))

# 3 xdr.no three-step
try:
    data=PAGE.encode(); sha=hashlib.sha256(data).hexdigest(); r=S.post('https://api.xdr.no/api/v1/publish',json={'files':[{'path':'index.html','size':len(data),'contentType':'text/html','sha256':sha}]},timeout=50); print('XDR_CREATE',r.status_code,r.text[:800]); d=r.json(); up=d['uploads'][0]['putUrl']; requests.put(up,data=data,headers={'Content-Type':'text/html'},timeout=55); S.post(d['finalize'],timeout=50); verify('xdr.no',d['url'])
except Exception as e: print('XDR_ERR',repr(e))

# 4 yeetit.site
try:
    r=S.post('https://yeetit.site/v1/publish',json={'html':PAGE,'title':TITLE},timeout=55); print('YEETIT',r.status_code,r.text[:500]); d=r.json() if r.ok else r.text; verify('yeetit.site',find_url(d,('yeetit.site',)))
except Exception as e: print('YEETIT_ERR',repr(e))

# 5 draftlet.io three-step
try:
    data=PAGE.encode(); r=S.post('https://api.draftlet.io/api/v1/publish',json={'files':[{'path':'index.html','contentType':'text/html','size':len(data)}]},timeout=55); print('DRAFTLET',r.status_code,r.text[:800]); d=r.json(); requests.put(d['uploads'][0]['uploadUrl'],data=data,headers={'content-type':'text/html','content-length':str(len(data))},timeout=60); S.post(f"https://api.draftlet.io/api/v1/publish/{d['slug']}/finalize",json={'versionId':d['versionId'],'editToken':d['editToken']},timeout=55); verify('draftlet.io',d['url'])
except Exception as e: print('DRAFTLET_ERR',repr(e))

# 6 yourwebs.cc HTML form
try:
    home=S.get('https://yourwebs.cc/',timeout=40); soup=BeautifulSoup(home.text,'html.parser'); done=False
    for f in soup.find_all('form'):
        action=urljoin(home.url,f.get('action') or home.url); method=(f.get('method') or 'post').lower()
        if method!='post': continue
        data={}; files={}
        for el in f.find_all(['input','textarea']):
            n=el.get('name'); typ=(el.get('type') or '').lower()
            if not n or typ in ('submit','button'): continue
            if typ=='file': files[n]=('cleaning-riyadh.html',PAGE,'text/html')
            elif 'title' in n.lower() or n.lower()=='name': data[n]=TITLE
            elif any(k in n.lower() for k in ('html','content','code','text')): data[n]=PAGE
            else: data[n]=el.get('value','')
        if not files and PAGE not in data.values(): continue
        rr=S.post(action,data=data,files=files or None,timeout=55,allow_redirects=True); print('YOURWEBS_FORM',rr.status_code,rr.url)
        cand=find_url(rr.text,('yourwebs.app','yourwebs.cc')) or (rr.url if rr.url!=action else '')
        if verify('yourwebs.app',cand): done=True; break
except Exception as e: print('YOURWEBS_ERR',repr(e))

print('COLORFUL_RESULTS_BEGIN')
for x in results: print(x['source']+'\t'+x['url'])
print('COLORFUL_RESULTS_END')
print('COLORFUL_VALID_COUNT='+str(len(results)))
print('COLORFUL_RESULTS_JSON='+json.dumps(results,ensure_ascii=False))
