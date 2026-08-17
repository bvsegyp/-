import asyncio,re,json,html,os
from urllib.parse import urlparse
from playwright.async_api import async_playwright

TARGET_URL='https://bvsegypt.com/'
ANCHOR='ماكينات عد النقود'

TARGETS=[
 ('share-html.com','https://share-html.com/','html'),
 ('pagegate.app','https://pagegate.app/','html'),
 ('swolvy.com','https://swolvy.com/','html'),
 ('uploadthefile.com','https://uploadthefile.com/','html'),
 ('htmlspot.com','https://www.htmlspot.com/','html'),
 ('htmlput.com','https://htmlput.com/','html'),
 ('pastemd.io','https://pastemd.io/','md'),
 ('notesh.ink','https://notesh.ink/','md'),
 ('noterift.com','https://noterift.com/','md'),
 ('yapp.page','https://yapp.page/','html'),
 ('publishmarkdown.com','https://publishmarkdown.com/','md'),
 ('htmldrop.app','https://htmldrop.app/','html'),
 ('dochost.io','https://dochost.io/','html'),
 ('paste.page','https://paste.page/','html'),
 ('crevioo.com','https://crevioo.com/','html'),
 ('pagelive.io','https://pagelive.io/','html'),
 ('fylo.host','https://fylo.host/','html'),
 ('oneclicklive.app','https://oneclicklive.app/','html'),
 ('markdshare.com','https://markdshare.com/','md'),
 ('pastes.io','https://pastes.io/','md'),
]

TOPICS=[
 'دليل اختيار ماكينات عد النقود للشركات والمحلات في مصر',
 'كيف تختار ماكينة عد نقود دقيقة لنشاطك التجاري',
 'أهم معايير شراء ماكينات عد النقود وكشف التزوير',
 'أسعار ماكينات عد النقود وما الذي يحدد فرق السعر',
 'ماكينات عد النقود للمحلات والسوبر ماركت: دليل عملي',
 'صيانة ماكينات عد النقود وأثرها على دقة العد',
 'أخطاء عد النقد الشائعة وكيف تقللها داخل الخزينة',
 'الفرق بين ماكينات عد النقود العادية وماكينات الفرز',
 'متى يكون تأجير ماكينة عد نقود أفضل من الشراء',
 'كيف ترفع كفاءة إدارة الكاش باستخدام ماكينة عد النقود',
 'دليل تجهيز نقطة الكاش بماكينة عد نقود موثوقة',
 'ماكينات عد وكشف العملات المزورة للشركات',
 'اختيار ماكينة عد النقود المناسبة لحجم التشغيل اليومي',
 'لماذا تحتاج الشركات إلى صيانة دورية لماكينات عد الأموال',
 'كيف تقلل وقت إغلاق الخزينة باستخدام ماكينة عد نقود',
 'نصائح قبل شراء ماكينة عد نقود جديدة في مصر',
 'دقة حساسات ماكينات عد النقود وأهميتها في التشغيل',
 'ماكينة عد النقود للمكاتب المالية ونقاط التحصيل',
 'مقارنة عملية بين أنواع ماكينات عد النقود',
 'كيفية اختيار مورد موثوق لماكينات عد النقود في مصر',
]

SECTIONS=[
 ('ابدأ بحجم التشغيل الحقيقي','اختيار ماكينة عد مناسبة يبدأ من فهم حجم النقد الذي يمر على الخزينة يوميًا. النشاط الذي يتعامل مع عشرات الرزم خلال اليوم يحتاج قدرة تشغيل وتحمل أعلى من مكتب صغير يستخدم الجهاز لفترات متقطعة. معرفة متوسط عدد الأوراق وساعات التشغيل تساعد على اختيار جهاز مناسب بدل شراء موديل أكبر من الحاجة أو جهاز أقل من المطلوب.'),
 ('الدقة أهم من السرعة وحدها','السرعة رقم مهم، لكنها ليست المعيار الوحيد. جودة الحساسات وثبات سحب الأوراق وقدرة الجهاز على التعامل مع الأوراق القديمة أو المختلفة في الحالة تؤثر مباشرة في دقة النتائج. في بيئة العمل اليومية، الخطأ في العد قد يستهلك وقتًا أكبر من الوقت الذي تم توفيره بالسرعة، لذلك يجب تقييم الأداء المتوازن بين السرعة والدقة.'),
 ('فحص التزوير يضيف طبقة أمان','بعض الأجهزة تجمع بين العد وخصائص كشف العملات المشكوك فيها عبر تقنيات مثل الأشعة فوق البنفسجية أو الأشعة تحت الحمراء أو الحساسات المغناطيسية بحسب الموديل. هذه الوظائف لا تلغي إجراءات المراجعة الداخلية، لكنها تضيف طبقة مساعدة مهمة خصوصًا في الأنشطة التي تستقبل نقدًا من عدد كبير من العملاء.'),
 ('سهولة الصيانة توفر تكلفة لاحقًا','قبل الشراء من المهم معرفة مدى توافر الصيانة وقطع الغيار والدعم الفني. الجهاز الذي يعمل لساعات طويلة يحتاج تنظيفًا دوريًا للحساسات ومسار الأوراق وقد يحتاج أجزاء استهلاكية مع الوقت. وجود دعم فني سريع يقلل فترة توقف الخزينة ويجعل التكلفة الإجمالية للجهاز أكثر وضوحًا.'),
 ('اختيار الجهاز حسب طبيعة النشاط','المحل والسوبر ماركت وشركة التوزيع والمكتب المالي قد تحتاج كل جهة خصائص مختلفة. بعض الأنشطة تركز على العد السريع، بينما تحتاج أنشطة أخرى إلى تجميع الفئات أو الفرز أو العمل ببطارية أو سهولة النقل بين الفروع. تحديد السيناريو اليومي قبل مقارنة الموديلات يمنع دفع تكلفة في خصائص لن يتم استخدامها.'),
 ('اختبر سهولة الاستخدام','واجهة واضحة وأزرار مفهومة وإمكانية تصفير النتائج أو التجميع بسهولة تقلل أخطاء الموظفين الجدد. التدريب البسيط على طريقة ترتيب الأوراق وتنظيف الجهاز والتعامل مع رسائل الخطأ يجعل الاستخدام اليومي أكثر استقرارًا، خصوصًا عندما يستخدم نفس الجهاز أكثر من موظف خلال الورديات.'),
 ('راجع الضمان وخدمة ما بعد البيع','الضمان لا يتعلق فقط بمدة مكتوبة على الفاتورة، بل بسرعة الاستجابة وطريقة تنفيذ الصيانة وتوافر الفنيين وقطع الغيار. هذه النقاط مهمة للشركات التي لا تستطيع تعطيل نقطة التحصيل لفترة طويلة. المقارنة بين الموردين يجب أن تشمل الخدمة بعد البيع وليس سعر الجهاز فقط.'),
 ('احسب العائد من تقليل الوقت والأخطاء','القيمة الحقيقية للجهاز تظهر في تقليل الوقت المستغرق في العد اليدوي والمراجعة وإعادة العد، بالإضافة إلى خفض احتمالات الفروق البشرية. عندما يكون حجم النقد كبيرًا، يمكن أن ينعكس ذلك على سرعة إغلاق الخزينة وتسليم الورديات وتجهيز الإيداعات البنكية بشكل أكثر تنظيمًا.'),
]

def article(i, markdown=False):
    title=TOPICS[i%len(TOPICS)]
    intro='إدارة النقد داخل الشركات والمحلات تعتمد على السرعة والدقة معًا، لذلك أصبح اختيار ماكينة عد مناسبة قرارًا تشغيليًا يؤثر في وقت الموظفين ودقة الخزينة وسهولة المراجعة اليومية. هذا الدليل يوضح أهم النقاط التي تساعد على تقييم الأجهزة بصورة عملية قبل الشراء أو التأجير، مع التركيز على احتياجات السوق المصري وطبيعة الاستخدام الفعلي.'
    paras=[]
    if markdown:
        paras=[f'# {title}','',intro,'']
        for n,(h,p) in enumerate(SECTIONS):
            paras += [f'## {h}','']
            text=p+' '+p
            if n==3:
                text += f' وعند مقارنة الموردين يمكن مراجعة [{ANCHOR}]({TARGET_URL}) المتاحة لدى BVS Egypt ضمن خيارات السوق، ثم مقارنة الموديلات بحسب حجم التشغيل وخصائص كشف التزوير وخدمة ما بعد البيع.'
            paras += [text,'']
        paras += ['## الخلاصة','', 'أفضل اختيار ليس دائمًا الجهاز الأسرع أو الأعلى سعرًا، بل الجهاز الذي يناسب حجم النقد الفعلي ويقدم دقة مستقرة مع صيانة متاحة ودعم واضح. تحديد الاحتياجات أولًا ثم مقارنة المواصفات والخدمة والضمان يساعد على اتخاذ قرار أكثر كفاءة على المدى الطويل.']
        return '\n'.join(paras)
    parts=[f'<h1>{html.escape(title)}</h1>',f'<p>{html.escape(intro)}</p>']
    for n,(h,p) in enumerate(SECTIONS):
        parts.append(f'<h2>{html.escape(h)}</h2>')
        text=p+' '+p
        if n==3:
            text += f' وعند مقارنة الموردين يمكن مراجعة <a href="{TARGET_URL}">{ANCHOR}</a> المتاحة لدى BVS Egypt ضمن خيارات السوق، ثم مقارنة الموديلات بحسب حجم التشغيل وخصائص كشف التزوير وخدمة ما بعد البيع.'
        parts.append(f'<p>{text}</p>')
    parts.append('<h2>الخلاصة</h2><p>أفضل اختيار ليس دائمًا الجهاز الأسرع أو الأعلى سعرًا، بل الجهاز الذي يناسب حجم النقد الفعلي ويقدم دقة مستقرة مع صيانة متاحة ودعم واضح. تحديد الاحتياجات أولًا ثم مقارنة المواصفات والخدمة والضمان يساعد على اتخاذ قرار أكثر كفاءة على المدى الطويل.</p>')
    return '<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title></head><body style="font-family:Arial,sans-serif;max-width:900px;margin:40px auto;line-height:1.9;padding:0 22px">'+''.join(parts)+'</body></html>'

async def verify(browser,url):
    p=await browser.new_page()
    try:
        await p.goto(url,wait_until='domcontentloaded',timeout=35000)
        await p.wait_for_timeout(2500)
        n=await p.locator('a[href*="bvsegypt.com"]').count()
        final=p.url
        if n<1:
            for fr in p.frames:
                try:
                    n=max(n,await fr.locator('a[href*="bvsegypt.com"]').count())
                except: pass
        print('VERIFY',final,'HREFS',n)
        await p.close()
        return final,n
    except Exception as e:
        print('VERIFY_ERR',url,repr(e))
        try: await p.close()
        except: pass
        return url,0

async def publish(browser,idx,domain,url,mode):
    pg=await browser.new_page()
    md=article(idx,True); ht=article(idx,False); content=md if mode=='md' else ht
    print('TRY',domain,'MODE',mode,'ANCHOR',ANCHOR,'TARGETS',content.count('bvsegypt.com'))
    try:
        await pg.goto(url,wait_until='domcontentloaded',timeout=45000)
        await pg.wait_for_timeout(2200)
        # Optional create/start action.
        for pat in ['Start writing','Create note','New note','Paste HTML','paste HTML','Paste Code','Paste code','or paste HTML code','Upload HTML']:
            el=pg.get_by_text(re.compile(re.escape(pat),re.I))
            if await el.count():
                try: await el.first.click(timeout=2500); await pg.wait_for_timeout(600); break
                except: pass
        # Fill title/name where available.
        title=TOPICS[idx%len(TOPICS)]
        for sel in ['input[placeholder*="title" i]:visible','input[name*="title" i]:visible','input[placeholder*="name" i]:visible','input[name*="name" i]:visible']:
            loc=pg.locator(sel)
            if await loc.count():
                try: await loc.first.fill(title); break
                except: pass
        filled=False
        tas=pg.locator('textarea:visible')
        if await tas.count():
            best=None; area=-1
            for j in range(await tas.count()):
                e=tas.nth(j)
                try:
                    bb=await e.bounding_box(); a=bb['width']*bb['height'] if bb else 0
                    if a>area: best=e; area=a
                except: pass
            if best:
                try: await best.fill(content); filled=True
                except: pass
        if not filled:
            ces=pg.locator('[contenteditable="true"]:visible')
            if await ces.count():
                try: await ces.first.fill(content); filled=True
                except: pass
        if not filled:
            fis=pg.locator('input[type="file"]')
            if await fis.count():
                path=f'/tmp/bvs-{idx}.html'; open(path,'w',encoding='utf-8').write(ht)
                try: await fis.first.set_input_files(path); filled=True
                except: pass
        if not filled:
            print(domain,'NO_INPUT'); await pg.close(); return None
        await pg.wait_for_timeout(800)
        clicked=False
        for pat in ['Get my shareable link','Get shareable link','Generate link','Generate Link','Generate Live Page','Deploy Page','Deploy','Publish','Share Note','Share','Host','Upload','Generate','Create Link','Create','Save']:
            btn=pg.get_by_role('button',name=re.compile(pat,re.I))
            if await btn.count():
                try: await btn.first.click(timeout=4500); clicked=True; break
                except: pass
            txt=pg.get_by_text(re.compile('^'+re.escape(pat)+'$',re.I))
            if await txt.count():
                try: await txt.first.click(timeout=4500); clicked=True; break
                except: pass
        # Some editors autosave/publish on navigation.
        await pg.wait_for_timeout(6500 if clicked else 3500)
        cands=[]
        if pg.url.rstrip('/')!=url.rstrip('/'): cands.append(pg.url)
        for a in await pg.locator('a[href^="http"]').all():
            try:
                h=await a.get_attribute('href')
                if h and h not in cands: cands.append(h)
            except: pass
        body=''
        try: body=await pg.locator('body').inner_text()
        except: pass
        for m in re.findall(r'https?://[^\s)\]<>"\']+',body):
            m=m.rstrip('.,')
            if m not in cands: cands.append(m)
        for inp in await pg.locator('input:visible').all():
            try:
                v=await inp.input_value()
                if v.startswith('http') and v not in cands: cands.append(v)
            except: pass
        root=domain.replace('www.','')
        cands=sorted(cands,key=lambda x:0 if root in x.replace('www.','') else 1)
        print(domain,'CANDIDATES',cands[:12])
        for cand in cands[:20]:
            final,n=await verify(browser,cand)
            if n>=1:
                await pg.close(); return final
    except Exception as e:
        print(domain,'ERR',repr(e))
    try: await pg.close()
    except: pass
    return None

async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True)
        out=[]
        for i,t in enumerate(TARGETS):
            u=await publish(browser,i,*t)
            if u:
                host=urlparse(u).hostname or t[0]
                out.append({'source':t[0],'domain':host,'url':u})
        await browser.close()
        print('BVS3_RESULTS_BEGIN')
        for x in out: print(x['domain']+'\t'+x['url'])
        print('BVS3_RESULTS_END')
        print('BVS3_VALID_COUNT='+str(len(out)))
        print('BVS3_RESULTS_JSON='+json.dumps(out,ensure_ascii=False))
asyncio.run(main())
