import asyncio,re,json,html
from playwright.async_api import async_playwright

TARGET='https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'
ANCHOR='أفضل شركة تنظيف في الرياض'
TARGETS=[
 ('notesh.ink','https://notesh.ink/','md'),
 ('yapp.page','https://yapp.page/','html'),
 ('publishmarkdown.com','https://publishmarkdown.com/','md'),
 ('markdshare.com','https://markdshare.com/','md'),
]

def article(mode):
    title='أفضل شركة تنظيف في الرياض: معايير الاختيار والخدمة الاحترافية'
    paras=[
      ('اختيار شركة تنظيف مناسبة','عند البحث عن خدمة تنظيف في الرياض، من المهم مقارنة الجودة والخبرة ونطاق الخدمة وسرعة الاستجابة، وعدم الاعتماد على السعر فقط. الشركة المناسبة توضح ما يتضمنه الحجز وتستخدم فريقًا مدربًا وأدوات مناسبة لكل نوع من الأسطح.'),
      ('تنظيف المنازل والفلل','تنظيف المنزل الاحترافي يشمل ترتيب مراحل العمل وتحديد الأولويات مثل المطابخ والحمامات والمجالس وغرف النوم. كما يجب مراعاة نوع الأرضيات والأثاث والمواد المستخدمة حتى تكون النتيجة فعالة وآمنة في الوقت نفسه.'),
      ('المعدات والمواد','المعدات الحديثة ترفع كفاءة إزالة الأتربة والبقع، لكن اختيار المواد المناسبة يظل عنصرًا أساسيًا. فالرخام والخشب والأقمشة تحتاج إلى طرق مختلفة، والخبرة تساعد على تجنب التلف والحفاظ على جودة الأسطح.'),
      ('الالتزام بالمواعيد','الشركة المنظمة تحدد وقت الوصول ومدة التنفيذ وعدد أفراد الفريق قبل بدء المهمة. هذا مهم خصوصًا في تنظيف ما بعد التشطيب أو قبل المناسبات أو عند تجهيز منزل جديد للسكن.'),
      ('كيف تقارن بين مقدمي الخدمة','يمكن مقارنة الشركات من خلال وضوح الأسعار وتفاصيل الخدمة وسهولة التواصل وتنوع الحلول مثل تنظيف الكنب والسجاد والتعقيم وتنظيف المكاتب والمنشآت. كلما كانت المعلومات واضحة أصبح اتخاذ القرار أسهل.'),
      ('الخيار المناسب في الرياض','إذا كنت تبحث عن '+ANCHOR+' فمن المفيد مراجعة تفاصيل الخدمة والخبرة ونطاق التغطية قبل الحجز. غيمة ملونة تعرض خدمات تنظيف المنازل والفلل والمكاتب داخل الرياض ويمكن مقارنة ما تقدمه مع احتياج المكان الفعلي.'),
      ('نتيجة أفضل مع تخطيط صحيح','أفضل نتائج التنظيف تبدأ من تحديد المطلوب بدقة، ثم اختيار الفريق المناسب والأدوات المناسبة، وأخيرًا مراجعة التفاصيل بعد انتهاء العمل. هذا الأسلوب يوفر الوقت ويمنح العميل نتيجة أكثر ثباتًا ووضوحًا.'),
    ]
    if mode=='md':
        out=[f'# {title}','']
        for h,p in paras:
            if ANCHOR in p: p=p.replace(ANCHOR,f'[{ANCHOR}]({TARGET})')
            out += [f'## {h}','',p,'']
        return '\n'.join(out)
    out=[f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>{html.escape(title)}</title></head><body style="font-family:Arial,Tahoma,sans-serif;max-width:900px;margin:40px auto;line-height:2;padding:0 20px"><h1>{html.escape(title)}</h1>']
    for h,p in paras:
        if ANCHOR in p: p=p.replace(ANCHOR,f'<a href="{TARGET}">{ANCHOR}</a>')
        out.append(f'<h2>{html.escape(h)}</h2><p>{p}</p>')
    out.append('</body></html>')
    return ''.join(out)

async def verify(browser,url):
    p=await browser.new_page()
    try:
        await p.goto(url,wait_until='domcontentloaded',timeout=35000); await p.wait_for_timeout(2000)
        count=0
        for fr in p.frames:
            try:
                els=fr.locator('a[href*="colorfulcloudco.com"]')
                for i in range(await els.count()):
                    txt=(await els.nth(i).inner_text()).strip()
                    if ANCHOR in txt: count+=1
            except: pass
        final=p.url; print('VERIFY',url,'FINAL',final,'MATCHES',count)
        return final,count
    except Exception as e:
        print('VERIFY_ERR',url,repr(e)); return url,0
    finally:
        await p.close()

async def publish(browser,domain,url,mode):
    pg=await browser.new_page(); content=article(mode)
    try:
        await pg.goto(url,wait_until='domcontentloaded',timeout=45000); await pg.wait_for_timeout(2000)
        # Some apps need an initial create/start action.
        for pat in ['Start writing','Create note','New note','Create','Paste HTML','Paste Code']:
            loc=pg.get_by_text(re.compile(pat,re.I))
            if await loc.count():
                try: await loc.first.click(timeout=2500); await pg.wait_for_timeout(900); break
                except: pass
        # optional title field
        titles=pg.locator('input[placeholder*="title" i]:visible,input[name*="title" i]:visible,input[placeholder*="name" i]:visible')
        if await titles.count():
            try: await titles.first.fill('أفضل شركة تنظيف في الرياض')
            except: pass
        filled=False
        tas=pg.locator('textarea:visible')
        if await tas.count():
            best=tas.first; area=-1
            for i in range(await tas.count()):
                e=tas.nth(i)
                try:
                    b=await e.bounding_box(); a=b['width']*b['height'] if b else 0
                    if a>area: area=a; best=e
                except: pass
            await best.fill(content); filled=True
        if not filled:
            ce=pg.locator('[contenteditable="true"]:visible')
            if await ce.count():
                try: await ce.first.fill(content); filled=True
                except: pass
        if not filled:
            fi=pg.locator('input[type="file"]')
            if await fi.count():
                path='/tmp/colorful-'+domain.replace('.','-')+'.html'; open(path,'w',encoding='utf-8').write(content); await fi.first.set_input_files(path); filled=True
        if not filled:
            print(domain,'NO_INPUT'); return None
        await pg.wait_for_timeout(800)
        clicked=False
        for pat in ['Share Note','Generate Link','Generate link','Publish','Share','Create Link','Deploy','Host','Save']:
            btn=pg.get_by_role('button',name=re.compile(pat,re.I))
            if await btn.count():
                try: await btn.first.click(timeout=4500); clicked=True; break
                except: pass
            tx=pg.get_by_text(re.compile('^'+re.escape(pat)+'$',re.I))
            if await tx.count():
                try: await tx.first.click(timeout=4500); clicked=True; break
                except: pass
        await pg.wait_for_timeout(5000)
        cands=[]
        if pg.url.rstrip('/')!=url.rstrip('/'): cands.append(pg.url)
        for a in await pg.locator('a[href^="http"]').all():
            try:
                h=await a.get_attribute('href')
                if h and h not in cands:cands.append(h)
            except: pass
        body=await pg.locator('body').inner_text()
        for m in re.findall(r'https?://[^\s)\]<>"\']+',body):
            m=m.rstrip('.,')
            if m not in cands:cands.append(m)
        root=domain.replace('www.','')
        cands=sorted(cands,key=lambda x:0 if root in x.replace('www.','') else 1)
        print(domain,'CANDS',cands[:10])
        for cand in cands[:15]:
            final,n=await verify(browser,cand)
            if n>0:return final
    except Exception as e: print(domain,'ERR',repr(e))
    finally: await pg.close()
    return None

async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(headless=True); out=[]
        tasks=[publish(b,*t) for t in TARGETS]
        vals=await asyncio.gather(*tasks)
        for t,u in zip(TARGETS,vals):
            if u: out.append({'source':t[0],'url':u})
        await b.close()
        print('COLORFUL_BROWSER_RESULTS_BEGIN')
        for x in out: print(x['source']+'\t'+x['url'])
        print('COLORFUL_BROWSER_RESULTS_END')
        print('COLORFUL_BROWSER_VALID_COUNT='+str(len(out)))
        print('COLORFUL_BROWSER_RESULTS_JSON='+json.dumps(out,ensure_ascii=False))
asyncio.run(main())
