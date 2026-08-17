import requests,re,json,html,hashlib,time,subprocess,os
from urllib.parse import urlparse,urljoin
from concurrent.futures import ThreadPoolExecutor,as_completed
from bs4 import BeautifulSoup

TARGET='https://bvsegypt.com/'
ANCHOR='ماكينات عد النقود'

TITLES=[
'دليل اختيار ماكينات عد النقود للشركات والمحلات في مصر',
'كيف تختار ماكينة عد نقود مناسبة لحجم التشغيل اليومي',
'أهم معايير شراء ماكينات عد النقود وكشف التزوير',
'صيانة ماكينات عد النقود ودورها في الحفاظ على الدقة',
'ماكينات عد النقود للمحلات والسوبر ماركت: دليل عملي',
'أسعار ماكينات عد النقود والعوامل التي تحدد فرق السعر',
'كيفية تقليل أخطاء الكاش باستخدام ماكينة عد النقود',
'الفرق بين ماكينات عد النقود وماكينات فرز العملات',
'متى يكون شراء ماكينة عد نقود أفضل من العد اليدوي',
'اختيار مورد ماكينات عد النقود وخدمة ما بعد البيع',
'تجهيز الخزينة بماكينة عد نقود موثوقة للشركات',
'ماكينات عد النقود وكشف العملات المزورة في بيئة العمل',
'كيف تسرع إغلاق الخزينة باستخدام ماكينة عد النقود',
'دقة حساسات ماكينات عد النقود وأثرها على التشغيل',
'نصائح قبل شراء ماكينة عد نقود جديدة في مصر',
'إدارة النقد بكفاءة باستخدام ماكينات عد الأموال الحديثة',
]

SECTIONS=[
('حدد حجم النقد اليومي','اختيار الجهاز يبدأ من معرفة حجم النقد الذي يمر على الخزينة وعدد ساعات التشغيل الفعلية. النشاط الذي يتعامل مع كميات كبيرة يحتاج جهازًا يتحمل العمل المتكرر ويقدم أداءً ثابتًا، بينما قد يكفي جهاز أبسط للمكاتب التي تستخدم العد على فترات. تحديد الاستخدام يمنع شراء جهاز أعلى من الحاجة أو أقل من ضغط العمل.'),
('وازن بين السرعة والدقة','السرعة وحدها لا تكفي إذا كان الجهاز يسبب إعادة العد أو يتوقف مع الأوراق القديمة. جودة مسار السحب والحساسات وطريقة التعامل مع الأوراق المختلفة عناصر تؤثر في دقة النتائج. الأفضل تقييم الأداء اليومي المتوازن بدل التركيز على رقم السرعة المكتوب في المواصفات فقط.'),
('فكر في كشف التزوير','الأجهزة التي تجمع العد مع خصائص كشف الأوراق المشكوك فيها تضيف طبقة أمان مفيدة، خاصة للأنشطة التي تستقبل نقدًا من عدد كبير من العملاء. تختلف تقنيات الكشف من موديل لآخر، لذلك يجب مقارنة الخصائص الفعلية ومدى مناسبتها للعملات المستخدمة في النشاط.'),
('ضع الصيانة في الحساب','تنظيف الحساسات ومسار الأوراق والصيانة الدورية يساعدان على بقاء النتائج مستقرة. عند المقارنة بين الموردين يجب مراجعة توافر الفنيين وقطع الغيار وسرعة الاستجابة لأن توقف الجهاز في وقت ضغط قد يؤثر في دورة التحصيل وإغلاق الخزينة.'),
('اختر الخصائص التي ستستخدمها','بعض الأنشطة تحتاج عدًا سريعًا فقط، بينما تحتاج أخرى إلى تجميع القيم أو الفرز أو التشغيل ببطارية أو سهولة النقل بين الفروع. تحديد الوظائف الضرورية قبل الشراء يحافظ على الميزانية ويجعل المقارنة بين الموديلات أكثر واقعية.'),
('راجع الضمان وخدمة ما بعد البيع','قيمة الضمان تظهر عند الحاجة إلى دعم فعلي وليس فقط في مدة مكتوبة. اسأل عن طريقة تنفيذ الصيانة ومدة الاستجابة وتوافر الأجزاء الاستهلاكية. المورد الذي يقدم متابعة واضحة قد يكون أفضل اقتصاديًا حتى لو كان سعر الجهاز الأولي أعلى قليلًا.'),
('احسب الوقت الذي يتم توفيره','استخدام جهاز مناسب يمكن أن يقلل وقت العد وإعادة المراجعة وتجهيز الإيداعات وتسليم الورديات. في الشركات التي تتعامل مع نقد بكميات كبيرة يصبح توفير دقائق في كل دورة عد أثرًا تشغيليًا ملموسًا على مدار الشهر.'),
('درب الموظفين على الاستخدام الصحيح','ترتيب الأوراق بطريقة مناسبة وعدم تحميل الجهاز بأكثر من السعة وتنظيفه وفق التعليمات يقلل الأعطال ورسائل الخطأ. تدريب الموظفين مهم خصوصًا عندما يتبادل أكثر من شخص استخدام نفس الجهاز خلال اليوم.'),
]

def make_page(i):
    title=TITLES[i%len(TITLES)]
    intro='تعتمد كفاءة التعامل مع النقد على تقليل الوقت والأخطاء مع الحفاظ على مراجعة واضحة للخزينة. لذلك لا يكون اختيار ماكينة العد قرارًا مرتبطًا بالسعر فقط، بل بحجم التشغيل والدقة وخدمة ما بعد البيع والخصائص التي يحتاجها النشاط فعلًا. يوضح هذا الدليل أهم النقاط العملية التي تساعد الشركات والمحلات على المقارنة قبل اتخاذ قرار الشراء.'
    parts=[f'<h1>{html.escape(title)}</h1>',f'<p>{intro}</p>']
    for n,(h,p) in enumerate(SECTIONS):
        text=p+' '+p
        if n==3:
            text += f' ومن الخيارات التي يمكن مراجعتها عند المقارنة <a href="{TARGET}">{ANCHOR}</a> لدى BVS Egypt، مع تقييم الموديل المناسب حسب حجم التشغيل وخصائص الكشف والضمان.'
        parts += [f'<h2>{h}</h2>',f'<p>{text}</p>']
    parts += ['<h2>الخلاصة</h2>','<p>الجهاز المناسب هو الذي يحقق دقة مستقرة ويختصر وقت العمل ويملك دعمًا فنيًا متاحًا عند الحاجة. المقارنة بين حجم التشغيل والمواصفات والضمان والصيانة تساعد على الوصول إلى اختيار يخدم النشاط لفترة أطول ويقلل الاعتماد على العد اليدوي.</p>']
    return '<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title></head><body style="font-family:Arial,Tahoma,sans-serif;max-width:920px;margin:40px auto;padding:0 24px;line-height:2;color:#222">'+''.join(parts)+'</body></html>'

PAGES=[make_page(i) for i in range(16)]
RESULTS=[]

def verify(name,u,retries=2):
    if not u:return None
    for k in range(retries):
        try:
            r=requests.get(u,timeout=35,allow_redirects=True,headers={'User-Agent':'Mozilla/5.0 BVSSEO/4.0'})
            hrefs=len(re.findall(r'href=["\'][^"\']*https?://(?:www\.)?bvsegypt\.com/?["\']',r.text,re.I))
            noindex=('noindex' in r.headers.get('x-robots-tag','').lower()) or bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex',r.text,re.I))
            print('VERIFY',name,r.status_code,r.url,'HREFS',hrefs,'NOINDEX',int(noindex))
            if r.status_code<400 and hrefs>=1 and not noindex:return r.url
        except Exception as e:print('VERIFY_ERR',name,repr(e))
        if k+1<retries:time.sleep(5)
    return None

def extract(obj,domains=()):
    vals=[]
    def walk(x):
        if isinstance(x,str):vals.extend(re.findall(r'https?://[^\s"\'<>]+',x))
        elif isinstance(x,dict):
            for v in x.values():walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    walk(obj); vals=[x.rstrip('.,);}') for x in vals]
    for d in domains:
        for u in vals:
            if d in u and 'claim' not in u.lower():return u
    return vals[0] if vals else ''

def ses():
    s=requests.Session();s.headers.update({'User-Agent':'Mozilla/5.0 BVSSEO/4.0'});return s

def aired():
    s=ses();r=s.post('https://aired.sh/api/publish',json={'html':PAGES[0]},timeout=40);print('AIRED',r.status_code,r.text[:400]);
    try:d=r.json()
    except:d=r.text
    return ('aired.sh',verify('AIRED',extract(d,('aired.sh',))))

def snapy():
    s=ses();r=s.post('https://api.snapy.host/api/publish',json={'content':PAGES[1],'filename':'index.html','name':'bvs-money-counting-guide'},timeout=45);print('SNAPY',r.status_code,r.text[:500]);
    try:d=r.json()
    except:d=r.text
    return ('snapy.host',verify('SNAPY',extract(d,('snapy.page','snapy.host'))))

def sitebin():
    s=ses();r=s.post('https://app.sitebin.io/api/sites',files={'files':('index.html',PAGES[2],'text/html')},timeout=50);print('SITEBIN',r.status_code,r.text[:500]);
    try:d=r.json()
    except:d=r.text
    return ('sitebin.io',verify('SITEBIN',extract(d,('sitebin.io',))))

def zerodeploy():
    s=ses();r=s.post('https://api.zerodeploy.dev/drop',files={'file':('index.html',PAGES[3],'text/html')},timeout=50);print('ZERO',r.status_code,r.text[:500]);
    try:d=r.json()
    except:d=r.text
    return ('zerodeploy.dev',verify('ZERO',extract(d,('zerodeploy.dev','zerodeploy.app'))))

def yeetit():
    s=ses();r=s.post('https://yeetit.site/v1/publish',json={'html':PAGES[4],'title':TITLES[4]},timeout=50);print('YEETIT',r.status_code,r.text[:500]);
    try:d=r.json()
    except:d=r.text
    return ('yeetit.site',verify('YEETIT',extract(d,('yeetit.site',))))

def hurl():
    s=ses();r=s.post('https://hurl.page/deploy',data=PAGES[5].encode(),headers={'Content-Type':'text/html; charset=utf-8'},timeout=50);print('HURL',r.status_code,r.text[:500]);
    try:d=r.json()
    except:d=r.text
    return ('hurl.page',verify('HURL',extract(d,('hurled.page','hurl.page'))))

def shippage():
    s=ses();r=s.post('https://ship.page/deploy',data=PAGES[6].encode(),headers={'Content-Type':'text/html; charset=utf-8'},timeout=50);print('SHIPPAGE',r.status_code,r.text[:500]);
    try:d=r.json()
    except:d=r.text
    return ('ship.page',verify('SHIPPAGE',extract(d,('shipped.page','ship.page'))))

def xdr():
    s=ses();data=PAGES[7].encode();sha=hashlib.sha256(data).hexdigest();r=s.post('https://api.xdr.no/api/v1/publish',json={'files':[{'path':'index.html','size':len(data),'contentType':'text/html','sha256':sha}]},timeout=45);print('XDR',r.status_code,r.text[:700]);d=r.json();ups=d.get('uploads') or []
    if ups:requests.put(ups[0].get('putUrl'),data=data,headers={'Content-Type':'text/html'},timeout=50)
    if d.get('finalize'):s.post(d['finalize'],timeout=40)
    return ('xdr.no',verify('XDR',d.get('url')))

def draftlet():
    s=ses();data=PAGES[8].encode();r=s.post('https://api.draftlet.io/api/v1/publish',json={'files':[{'path':'index.html','contentType':'text/html','size':len(data)}]},timeout=45);print('DRAFTLET',r.status_code,r.text[:700]);d=r.json();ups=d.get('uploads') or []
    if ups:
        up=ups[0].get('uploadUrl') or ups[0].get('url');requests.put(up,data=data,headers={'content-type':'text/html','content-length':str(len(data))},timeout=50)
    slug=d.get('slug');ver=d.get('versionId');tok=d.get('editToken')
    if slug and ver and tok:s.post(f'https://api.draftlet.io/api/v1/publish/{slug}/finalize',json={'versionId':ver,'editToken':tok},timeout=45)
    return ('draftlet.io',verify('DRAFTLET',d.get('url') or d.get('siteUrl')))

def botsite():
    s=ses();r=s.post('https://botsite.dev/api/v1/sites',data=PAGES[9].encode(),headers={'Content-Type':'text/html; charset=utf-8'},timeout=45);print('BOTSITE',r.status_code,r.text[:600]);d=r.json();u=d.get('url') or extract(d,('botsite.dev',));return ('botsite.dev',verify('BOTSITE',u,3))

def pastehtmlcom():
    s=ses();r=s.post('https://pastehtml.com/upload/create?input_type=html&result=address',data={'txt':PAGES[10]},timeout=45,allow_redirects=True);print('PASTEHTMLCOM',r.status_code,r.url,r.text[:500]);u=r.text.strip() if r.text.strip().startswith('http') else extract(r.text,('pastehtml.com',));
    if not u and 'upload/create' not in r.url:u=r.url
    return ('pastehtml.com',verify('PASTEHTMLCOM',u))

def form_publish(home,page,title,name,domains):
    s=ses();r=s.get(home,timeout=35);soup=BeautifulSoup(r.text,'html.parser')
    for f in soup.find_all('form'):
        action=urljoin(r.url,f.get('action') or r.url);method=(f.get('method') or 'post').lower()
        if method!='post':continue
        data={};files={};put=False
        for el in f.find_all(['input','textarea','select']):
            n=el.get('name');typ=(el.get('type') or '').lower();ln=(n or '').lower()
            if not n or typ in ('submit','button','image'):continue
            if typ=='file':files[n]=('bvs-money-counting.html',page,'text/html');put=True
            elif 'title' in ln:data[n]=title
            elif any(k in ln for k in ('html','content','code','text','body','markdown')):data[n]=page;put=True
            else:data[n]=el.get('value','')
        if not put:continue
        try:
            rr=s.post(action,data=data,files=files or None,timeout=45,allow_redirects=True);print(name,'FORM',rr.status_code,rr.url,rr.text[:300])
            try:d=rr.json()
            except:d=rr.text
            u=extract(d,domains)
            if not u and rr.url!=action:u=rr.url
            v=verify(name,u)
            if v:return v
        except Exception as e:print(name,'FORM_ERR',repr(e))
    return None

def posteasy():return ('post-easy.org',form_publish('https://post-easy.org/post',PAGES[11],TITLES[11],'POSTEASY',('post-easy.org',)))
def htmlhost():return ('htmlhost.co',form_publish('https://htmlhost.co/',PAGES[12],TITLES[12],'HTMLHOST',('htmlhost.co',)))
def sharable():return ('sharable.link',form_publish('https://sharable.link/free-html-hosting',PAGES[13],TITLES[13],'SHARABLE',('sharable.link',)))
def yourwebs():return ('yourwebs.cc',form_publish('https://yourwebs.cc/',PAGES[14],TITLES[14],'YOURWEBS',('yourwebs.app','yourwebs.cc')))

FUNCS=[aired,snapy,sitebin,zerodeploy,yeetit,hurl,shippage,xdr,draftlet,botsite,pastehtmlcom,posteasy,htmlhost,sharable,yourwebs]
with ThreadPoolExecutor(max_workers=8) as ex:
    futs={ex.submit(fn):fn.__name__ for fn in FUNCS}
    for f in as_completed(futs):
        try:
            src,u=f.result()
            if u:RESULTS.append({'source':src,'url':u,'domain':urlparse(u).hostname})
        except Exception as e:print('FUNC_ERR',futs[f],repr(e))
print('BVS4_RESULTS_BEGIN')
for x in RESULTS:print((x['domain'] or x['source'])+'\t'+x['url'])
print('BVS4_RESULTS_END')
print('BVS4_VALID_COUNT='+str(len(RESULTS)))
print('BVS4_RESULTS_JSON='+json.dumps(RESULTS,ensure_ascii=False))
