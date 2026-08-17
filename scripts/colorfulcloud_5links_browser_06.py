import asyncio,re,json,html,os,requests
from urllib.parse import urlparse
from playwright.async_api import async_playwright

LINKS=[
 ('أفضل شركة تنظيف في الرياض','https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'),
 ('أفضل شركة تنظيف شقق بالرياض','https://colorfulcloudco.com/افضل-شركة-تنظيف-شقق-بالرياض/'),
 ('تنظيف منازل بالساعة بالرياض','https://colorfulcloudco.com/تنظيف-منازل-بالساعة-بالرياض/'),
 ('شركات تنظيف في الرياض','https://colorfulcloudco.com/شركات-تنظيف-في-الرياض/'),
 ('شركة غيمة ملونة للتنظيف','https://colorfulcloudco.com/'),
]
TARGETS=[
 ('notesh.ink','https://notesh.ink/','md'),
 ('yapp.page','https://yapp.page/','html'),
 ('publishmarkdown.com','https://publishmarkdown.com/','md'),
 ('markdshare.com','https://markdshare.com/','md'),
 ('share-html.com','https://share-html.com/','html'),
 ('dochost.io','https://dochost.io/','html'),
 ('htmlhost.co','https://htmlhost.co/','html'),
 ('fylo.host','https://fylo.host/','html'),
 ('pagelive.io','https://pagelive.io/','html'),
 ('pagegate.app','https://pagegate.app/','html'),
 ('htmldrop.app','https://htmldrop.app/','html'),
 ('crevioo.com','https://crevioo.com/','html'),
]
TITLES=[
 'دليل اختيار أفضل شركة تنظيف في الرياض بخطوات عملية',
 'تنظيف المنازل بالرياض: كيف تحصل على نتيجة أفضل من أول زيارة',
 'مقارنة خدمات تنظيف الشقق والفلل في الرياض قبل الحجز',
 'ما الذي يميز شركة تنظيف محترفة في الرياض عن الخدمة العادية',
 'تنظيف البيت في الرياض من التخطيط حتى المراجعة النهائية',
 'كيف تختار خدمة تنظيف تناسب مساحة منزلك وميزانيتك',
 'دليل عملي لتنظيف الشقق بالرياض والحفاظ على النتيجة',
 'تنظيف المنازل بالساعة أم التنظيف الشامل: أيهما أنسب',
 'معايير جودة شركات التنظيف في الرياض التي يجب مراجعتها',
 'خطة تنظيف منزل احترافية تقلل الوقت وتحسن النتيجة',
 'تنظيف الفلل بالرياض: تنظيم العمل للمساحات الكبيرة',
 'كيف تقيّم شركة التنظيف بعد أول زيارة قبل تكرار الحجز',
]
SECTIONS=[
 ('حدد الأولويات قبل الحجز','تحديد المطلوب قبل وصول فريق التنظيف يجعل وقت التنفيذ أكثر فاعلية. من المفيد كتابة الغرف ذات الأولوية، المناطق التي تحتوي على بقع أو دهون، والأسطح التي تحتاج مواد خاصة. كما يساعد ذكر مساحة العقار وعدد الغرف على تقدير عدد أفراد الفريق والمدة المناسبة.'),
 ('اختر الأسلوب المناسب لكل سطح','الأسطح ليست متشابهة؛ الرخام والخشب والزجاج والأقمشة تحتاج إلى أدوات ومواد مختلفة. الاستخدام العشوائي للمنظفات القوية قد يسبب بهتانًا أو تلفًا، لذلك تعتمد الخدمة المحترفة على اختبار المادة واختيار الطريقة المناسبة قبل التعامل مع المساحات الكبيرة.'),
 ('رتب مراحل التنظيف','البدء من الأعلى إلى الأسفل ومن المناطق الأقل اتساخًا إلى الأكثر اتساخًا يقلل إعادة العمل. إزالة الغبار أولًا ثم تنظيف الأسطح والأرضيات وبعدها التعقيم في الأماكن المناسبة يجعل النتيجة أكثر تنظيمًا. وفي المنازل الكبيرة يفضل تقسيم العمل إلى مناطق ومراجعة كل منطقة قبل الانتقال لغيرها.'),
 ('راجع ما يشمله السعر','قبل تأكيد الحجز يجب معرفة ما يدخل ضمن السعر: عدد العمال، مدة الزيارة، المواد، المعدات، وهل تشمل الخدمة النوافذ أو الكنب أو السجاد أو المطابخ العميقة. وضوح التفاصيل يمنع سوء الفهم ويجعل المقارنة بين العروض أكثر عدلًا.'),
 ('المراجعة النهائية جزء من الخدمة','بعد انتهاء التنظيف من المفيد المرور على الغرف ومراجعة الزوايا والأسطح والمطبخ والحمامات. أي ملاحظة بسيطة يفضل ذكرها قبل مغادرة الفريق، لأن المعالجة الفورية أسهل من محاولة ترتيب زيارة أخرى. المراجعة أيضًا تساعد على معرفة مستوى الخدمة الحقيقي.'),
 ('حافظ على النتيجة بعد الزيارة','يمكن إطالة أثر التنظيف من خلال إزالة الانسكابات سريعًا، تهوية المكان، مسح الأسطح الأكثر استخدامًا، وتنظيم الأدوات اليومية. عندما يتم الحفاظ على روتين بسيط بين الزيارات تقل الحاجة إلى تنظيف عميق متكرر ويصبح الوقت المطلوب في الزيارة التالية أقل.'),
 ('لا تجعل السعر المعيار الوحيد','السعر مهم لكنه لا يكشف وحده عن جودة الخدمة. سرعة التواصل، وضوح الموعد، خبرة الفريق، المواد المستخدمة، والقدرة على التعامل مع الملاحظات عوامل تؤثر في التجربة. المقارنة المتوازنة بين هذه العناصر تعطي صورة أدق من التركيز على أقل رقم فقط.'),
 ('اختيار الخدمة حسب نمط الاستخدام','منزل به أطفال أو استخدام يومي مكثف قد يحتاج زيارات أكثر انتظامًا من شقة قليلة الاستخدام. كذلك تختلف الأولويات في الفلل والمكاتب عن الشقق. تحديد نمط الاستخدام يساعد على اختيار تنظيف شامل أو دوري أو بالساعة بطريقة أقرب للاحتياج الحقيقي.'),
]

def md_article(i):
    title=TITLES[i%len(TITLES)]; shift=i%len(SECTIONS); ss=SECTIONS[shift:]+SECTIONS[:shift]
    out=[f'# {title}','','اختيار شركة تنظيف في الرياض يحتاج إلى معرفة ما تريده من الخدمة قبل مقارنة الأسعار. هذا الدليل يجمع أهم النقاط العملية التي تساعد على تنظيم عملية التنظيف والحصول على نتيجة أكثر ثباتًا، سواء كان المكان شقة أو فيلا أو منزلًا يحتاج إلى تنظيف دوري.','']
    linktexts=[
      f'يمكن مراجعة دليل [{LINKS[0][0]}]({LINKS[0][1]}) للتعرف على معايير الاختيار قبل الحجز.',
      f'ولخدمات الشقق يمكن الاطلاع على [{LINKS[1][0]}]({LINKS[1][1]}) ومقارنة تفاصيل الخدمة.',
      f'إذا كان الوقت هو العامل الأهم، فخيار [{LINKS[2][0]}]({LINKS[2][1]}) يوضح فكرة الحجز المرن.',
      f'كما يفيد دليل [{LINKS[3][0]}]({LINKS[3][1]}) عند مقارنة أكثر من مزود خدمة داخل المدينة.',
      f'ولمعرفة نطاق الخدمات بشكل عام يمكن زيارة [{LINKS[4][0]}]({LINKS[4][1]}).',
    ]
    for n,(h,p) in enumerate(ss):
        out += [f'## {h}','',p,'']
        if n<5: out += [linktexts[n],'']
    out += ['## الخلاصة','','التنظيف الاحترافي يصبح أكثر فاعلية عندما تبدأ العملية بتحديد المطلوب وتنتهي بمراجعة النتيجة. اختيار فريق واضح في نطاق عمله، ثم الحفاظ على روتين بسيط بعد الزيارة، يساعد على إبقاء المنزل نظيفًا لفترة أطول ويجعل الزيارات التالية أسرع وأكثر تنظيمًا.']
    return '\n'.join(out)

def html_article(i):
    md=md_article(i); blocks=[]
    for b in re.split(r'\n\s*\n',md):
        b=b.strip()
        if not b: continue
        if b.startswith('# '): blocks.append('<h1>'+html.escape(b[2:])+'</h1>'); continue
        if b.startswith('## '): blocks.append('<h2>'+html.escape(b[3:])+'</h2>'); continue
        pos=0; parts=[]
        for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',b):
            parts.append(html.escape(b[pos:m.start()])); parts.append('<a href="'+html.escape(m.group(2),quote=True)+'">'+html.escape(m.group(1))+'</a>'); pos=m.end()
        parts.append(html.escape(b[pos:])); blocks.append('<p>'+''.join(parts)+'</p>')
    return '<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(TITLES[i%len(TITLES)])+'</title></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,Tahoma,sans-serif;line-height:2;color:#222">'+''.join(blocks)+'</main></body></html>'

async def count_links(page):
    n=0
    try: n += await page.locator('a[href*="colorfulcloudco.com"]').count()
    except: pass
    for fr in page.frames:
        if fr==page.main_frame: continue
        try: n += await fr.locator('a[href*="colorfulcloudco.com"]').count()
        except: pass
    return n

async def verify(browser,url):
    p=await browser.new_page(); resp=None
    try:
        resp=await p.goto(url,wait_until='domcontentloaded',timeout=40000); await p.wait_for_timeout(2500)
        n=await count_links(p)
        robots=''
        try:
            vals=await p.locator('meta[name="robots"],meta[name="googlebot"]').evaluate_all("els=>els.map(e=>e.content||'').join(' ')")
            robots=vals.lower()
        except: pass
        xrob=''
        try: xrob=(await resp.all_headers()).get('x-robots-tag','').lower() if resp else ''
        except: pass
        noindex=('noindex' in robots or 'noindex' in xrob)
        print('VERIFY',url,'HREFS',n,'NOINDEX',int(noindex),'FINAL',p.url)
        final=p.url; await p.close(); return final,n,noindex
    except Exception as e:
        print('VERIFY_ERR',url,repr(e));
        try: await p.close()
        except: pass
        return url,0,True

async def publish(browser,idx,domain,url,mode):
    pg=await browser.new_page(); md=md_article(idx); ht=html_article(idx); content=md if mode=='md' else ht
    print('TRY',domain,'LINKS_IN_SOURCE',content.count('colorfulcloudco.com'))
    try:
        await pg.goto(url,wait_until='domcontentloaded',timeout=45000); await pg.wait_for_timeout(1200)
        # title fields
        for sel in ['input[name*=title i]','input[placeholder*=title i]','input[type=text]']:
            loc=pg.locator(sel)
            if await loc.count():
                try: await loc.first.fill(TITLES[idx%len(TITLES)]); break
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
            fis=pg.locator('input[type=file]')
            if await fis.count():
                path=f'/tmp/colorful-{idx}.html'; open(path,'w',encoding='utf-8').write(ht)
                try: await fis.first.set_input_files(path); filled=True
                except: pass
        if not filled:
            print(domain,'NO_INPUT'); await pg.close(); return None
        await pg.wait_for_timeout(800)
        for pat in ['Get my shareable link','Get shareable link','Generate link','Generate Link','Generate Live Page','Deploy Page','Deploy','Publish','Share Note','Share','Host','Upload','Generate','Create Link','Create','Save']:
            btn=pg.get_by_role('button',name=re.compile(pat,re.I))
            if await btn.count():
                try: await btn.first.click(timeout=5000); break
                except: pass
        await pg.wait_for_timeout(3500)
        candidates=[]
        if pg.url.rstrip('/') != url.rstrip('/'): candidates.append(pg.url)
        try:
            hrefs=await pg.locator('a[href]').evaluate_all('els=>els.map(e=>e.href)')
            candidates += [h for h in hrefs if domain in h]
        except: pass
        try:
            vals=await pg.locator('input').evaluate_all('els=>els.map(e=>e.value).filter(Boolean)')
            candidates += [v for v in vals if isinstance(v,str) and v.startswith('http') and domain in v]
        except: pass
        seen=set()
        for cand in candidates:
            if cand in seen: continue
            seen.add(cand)
            if any(x in cand for x in ['/api/','/assets/','favicon','manifest','login','signup']): continue
            final,n,noindex=await verify(browser,cand)
            if n>=5 and not noindex:
                print('VALID',domain,final); await pg.close(); return final
        print(domain,'NO_VALID_CANDIDATE',candidates[:10])
    except Exception as e: print(domain,'ERR',repr(e))
    try: await pg.close()
    except: pass
    return None

async def direct_publish(browser):
    out=[]; s=requests.Session(); s.headers.update({'User-Agent':'Mozilla/5.0 ColorfulCloudSEO/6.0'})
    # Draftmark
    try:
        r=s.post('https://draftmark.app/api/v1/docs',json={'content':md_article(20),'visibility':'public'},timeout=45); print('DRAFTMARK_POST',r.status_code,r.text[:500]); d=r.json() if r.ok else {}; u=d.get('url','');
        if u and not u.startswith('http'): u='https://'+u.lstrip('/')
        if u:
            final,n,noindex=await verify(browser,u)
            if n>=5 and not noindex: out.append(('draftmark.app',final)); print('VALID draftmark.app',final)
    except Exception as e: print('DRAFTMARK_ERR',repr(e))
    # Share-HTML direct API
    try:
        r=s.post('https://share-html.com/api/v1/pages',json={'html':html_article(21)},timeout=45); print('SHAREHTML_POST',r.status_code,r.text[:500]);
        d=r.json() if r.ok else {}; vals=[]
        def walk(x):
            if isinstance(x,str) and x.startswith('http'): vals.append(x)
            elif isinstance(x,dict):
                for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(d)
        for u in vals:
            if 'share-html.com' not in u or '/api/' in u: continue
            final,n,noindex=await verify(browser,u)
            if n>=5 and not noindex: out.append(('share-html.com',final)); print('VALID share-html.com',final); break
    except Exception as e: print('SHAREHTML_DIRECT_ERR',repr(e))
    return out

async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True)
        out=await direct_publish(browser)
        used={x[0] for x in out}
        for i,t in enumerate(TARGETS):
            if t[0] in used: continue
            u=await publish(browser,i,*t)
            if u: out.append((t[0],u)); used.add(t[0])
        print('COLORFUL6_RESULTS_BEGIN')
        for d,u in out: print(d+'\t'+u)
        print('COLORFUL6_RESULTS_END')
        print('COLORFUL6_VALID_COUNT='+str(len(out)))
        print('COLORFUL6_RESULTS_JSON='+json.dumps([{'source':d,'url':u} for d,u in out],ensure_ascii=False))
        await browser.close()

asyncio.run(main())
