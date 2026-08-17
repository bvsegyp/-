import asyncio,re,json,html,os
from playwright.async_api import async_playwright

LINKS=[
 ('baby products online in Egypt','https://mommysmart.net/'),
 ('baby strollers in Egypt','https://mommysmart.net/collections/baby-transport'),
 ('baby feeding essentials','https://mommysmart.net/collections/frontpage'),
 ('baby diapering products','https://mommysmart.net/collections/diapering'),
 ('baby carriers','https://mommysmart.net/collections/baby-carriers'),
]
TARGETS=[
 ('dochost.io','https://dochost.io/','html'),
 ('htmlhost.co','https://htmlhost.co/','html'),
 ('fylo.host','https://fylo.host/','html'),
 ('pagelive.io','https://pagelive.io/','html'),
 ('pagegate.app','https://pagegate.app/','html'),
 ('htmldrop.app','https://htmldrop.app/','html'),
 ('crevioo.com','https://crevioo.com/','html'),
 ('paste.page','https://paste.page/','html'),
 ('swolvy.com','https://swolvy.com/','html'),
 ('uploadthefile.com','https://uploadthefile.com/','html'),
 ('htmlspot.com','https://htmlspot.com/','html'),
 ('htmlput.com','https://htmlput.com/','html'),
 ('pastemd.io','https://pastemd.io/','md'),
 ('noterift.com','https://noterift.com/','md'),
 ('oneclicklive.app','https://oneclicklive.app/','html'),
 ('pastes.io','https://pastes.io/','md'),
]
TITLES=[
 'Newborn Essentials Every First-Time Parent Should Consider',
 'How to Choose Baby Products for Everyday Family Life in Egypt',
 'A Practical Guide to Baby Strollers, Feeding and Diapering',
 'Smart Baby Shopping Tips for New Parents in Egypt',
 'Baby Travel Essentials for Comfortable Everyday Outings',
 'A Simple Feeding and Diapering Checklist for New Parents',
 'How to Choose Practical Baby Gear Without Overbuying',
 'Everyday Baby Care Products Parents Actually Use',
 'A Realistic Baby Essentials Checklist for the First Months',
 'Choosing Baby Strollers and Carriers for Daily Use',
 'What New Parents Need for Feeding, Diapering and Travel',
 'How to Build a Useful Baby Shopping List in Egypt',
 'Baby Products That Make Daily Routines Easier',
 'A Parent-Friendly Guide to Newborn Shopping in Egypt',
 'Essential Baby Gear for Home, Feeding and Travel',
 'How to Shop for Baby Essentials with Better Value',
]
SECTIONS=[
 ('Build your checklist around real routines','The most useful baby shopping list starts with the routines that happen every day: feeding, diaper changes, sleep, hygiene, and travel. New parents often buy too many specialized products before they know what their baby prefers. Starting with a smaller group of dependable essentials makes the first weeks easier and leaves room to add products later when a real need appears.'),
 ('Choose products that are easy to clean','Baby products are handled frequently and many need washing every day. Bottles, feeding accessories, changing items, carriers, and travel gear are more practical when they have simple designs and washable materials. Parents should think about cleaning and storage before buying because an item that looks impressive may become inconvenient if it takes too long to maintain.'),
 ('Match travel gear to your lifestyle','Strollers, car seats, and carriers should fit the way a family actually moves. Parents who use a car every day may need different features from families who walk more often or live in buildings with stairs. Folding size, weight, storage space, wheel quality, and how easy the product is to carry can matter more in daily life than decorative features.'),
 ('Buy feeding products in stages','Feeding needs change quickly during the first year. Bottles, nipples, bibs, cups, bowls, spoons, and food containers become useful at different stages, so there is rarely a reason to buy everything at once. Testing a smaller number of products first can reduce waste and help parents discover which shapes and materials work best for their child.'),
 ('Keep diapering and hygiene simple','A practical changing setup usually needs diapers, wipes, a changing mat, spare clothes, and a few gentle care products. Keeping these supplies together saves time during frequent changes. Parents should focus on fit, skin comfort, and ease of use rather than building a large collection of products before they understand the baby’s actual needs.'),
 ('Organize essentials by routine','Daily care becomes easier when feeding products, diapering supplies, bath items, and travel gear each have a clear place. Good organization reduces stress and makes it easier to notice when supplies need to be replaced. A small travel pouch can also keep the most important items ready for clinic visits, family outings, or short trips.'),
 ('Focus on safety and real value','A useful baby product should be appropriate for the child’s age and size, easy to use correctly, durable enough for frequent use, and realistic for the family’s lifestyle. Parents should compare products based on safety, convenience, and how often they will actually be used instead of choosing only by price, popularity, or the number of extra features.'),
]

def md_article(i):
    title=TITLES[i%len(TITLES)]
    out=[f'# {title}','','Shopping for a baby becomes much easier when parents focus on practical products that support real daily routines. Instead of trying to buy every item before the baby arrives, families can start with safe, useful essentials for feeding, diapering, hygiene, and travel, then add more as the baby grows.','']
    for n,(h,p) in enumerate(SECTIONS):
        out += [f'## {h}','',p,'']
        if n<5:
            a,u=LINKS[n]
            out += [f'For related options, explore [{a}]({u}) from Mommy\'s Mart.','']
    out += ['## Final thoughts','','Parents usually get better value when they shop in stages and choose products that match their baby’s current needs. A focused checklist keeps the home organized, reduces waste, and makes it easier to compare quality and safety before every purchase.']
    return '\n'.join(out)

def html_article(i):
    text=md_article(i); blocks=[]
    for b in re.split(r'\n\s*\n',text):
        b=b.strip()
        if not b: continue
        if b.startswith('# '): blocks.append('<h1>'+html.escape(b[2:])+'</h1>'); continue
        if b.startswith('## '): blocks.append('<h2>'+html.escape(b[3:])+'</h2>'); continue
        pos=0; parts=[]
        for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)',b):
            parts.append(html.escape(b[pos:m.start()])); parts.append('<a href="'+html.escape(m.group(2),quote=True)+'">'+html.escape(m.group(1))+'</a>'); pos=m.end()
        parts.append(html.escape(b[pos:])); blocks.append('<p>'+''.join(parts)+'</p>')
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(TITLES[i%len(TITLES)])+'</title><meta name="description" content="Practical baby products and newborn essentials guide for parents in Egypt"></head><body><main style="max-width:920px;margin:40px auto;padding:0 24px;font-family:Arial,sans-serif;line-height:1.85;color:#222">'+''.join(blocks)+'</main></body></html>'

async def count_links(page):
    n=0
    try: n += await page.locator('a[href*="mommysmart.net"]').count()
    except: pass
    for fr in page.frames:
        if fr==page.main_frame: continue
        try: n += await fr.locator('a[href*="mommysmart.net"]').count()
        except: pass
    return n

async def verify(browser,url):
    p=await browser.new_page(); resp=None
    try:
        resp=await p.goto(url,wait_until='domcontentloaded',timeout=40000); await p.wait_for_timeout(2200)
        n=await count_links(p)
        exact=False
        try: exact='baby products online in Egypt' in (await p.content())
        except: pass
        robots=''
        try: robots=(await p.locator('meta[name="robots"],meta[name="googlebot"]').evaluate_all("els=>els.map(e=>e.content||'').join(' ')")).lower()
        except: pass
        xrob=''
        try: xrob=(await resp.all_headers()).get('x-robots-tag','').lower() if resp else ''
        except: pass
        noindex=('noindex' in robots or 'noindex' in xrob)
        final=p.url
        print('VERIFY',url,'FINAL',final,'HREFS',n,'EXACT',int(exact),'NOINDEX',int(noindex))
        await p.close(); return final,n,exact,noindex
    except Exception as e:
        print('VERIFY_ERR',url,repr(e))
        try: await p.close()
        except: pass
        return url,0,False,True

async def publish(browser,idx,domain,url,mode):
    pg=await browser.new_page(); md=md_article(idx); ht=html_article(idx); content=md if mode=='md' else ht
    print('TRY',domain,'MODE',mode,'LINKS_IN_SOURCE',content.count('mommysmart.net'))
    try:
        await pg.goto(url,wait_until='domcontentloaded',timeout=45000); await pg.wait_for_timeout(1400)
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
                path=f'/tmp/mommysmart-{idx}.html'; open(path,'w',encoding='utf-8').write(ht)
                try: await fis.first.set_input_files(path); filled=True
                except: pass
        if not filled:
            print(domain,'NO_INPUT'); await pg.close(); return None
        await pg.wait_for_timeout(700)
        clicked=False
        for pat in ['Get my shareable link','Get shareable link','Generate link','Generate Link','Generate Live Page','Deploy Page','Deploy','Publish','Share Note','Share','Host','Upload','Generate','Create Link','Create','Save','Post']:
            btn=pg.get_by_role('button',name=re.compile(pat,re.I))
            if await btn.count():
                try: await btn.first.click(timeout=5000); clicked=True; break
                except: pass
        if not clicked:
            sub=pg.locator('button[type=submit]:visible,input[type=submit]:visible')
            if await sub.count():
                try: await sub.first.click(timeout=5000); clicked=True
                except: pass
        await pg.wait_for_timeout(4000)
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
        try:
            body=await pg.locator('body').inner_text(); candidates += re.findall(r'https?://[^\s<>]+',body)
        except: pass
        seen=set()
        for cand in candidates:
            cand=cand.rstrip('.,);]')
            if cand in seen or domain not in cand: continue
            seen.add(cand)
            if any(x in cand for x in ['/api/','/assets/','favicon','manifest','login','signup','register']): continue
            final,n,exact,noindex=await verify(browser,cand)
            if n>=5 and exact and not noindex:
                print('VALID',domain,final); await pg.close(); return final
        print(domain,'NO_VALID_CANDIDATE',candidates[:12])
    except Exception as e: print(domain,'ERR',repr(e))
    try: await pg.close()
    except: pass
    return None

async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True)
        out=[]
        for i,t in enumerate(TARGETS):
            u=await publish(browser,i,*t)
            if u: out.append((t[0],u))
        print('MOMMYSMART5_RESULTS_BEGIN')
        for d,u in out: print(d+'\t'+u)
        print('MOMMYSMART5_RESULTS_END')
        print('MOMMYSMART5_VALID_COUNT='+str(len(out)))
        print('MOMMYSMART5_RESULTS_JSON='+json.dumps([{'source':d,'url':u} for d,u in out]))
        await browser.close()

asyncio.run(main())
