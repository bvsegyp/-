import asyncio,json
from urllib.parse import urlparse

src=open('scripts/bvs_money_counting_domains_03.py',encoding='utf-8').read()
src=src.rsplit('asyncio.run(main())',1)[0]
ns={}
exec(src,ns)

TARGETS=ns['TARGETS']
publish=ns['publish']
async_playwright=ns['async_playwright']

async def fast_main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True)
        sem=asyncio.Semaphore(4)
        out=[]
        async def one(i,t):
            async with sem:
                u=await publish(browser,i,*t)
                if u:
                    host=urlparse(u).hostname or t[0]
                    out.append({'source':t[0],'domain':host,'url':u})
        await asyncio.gather(*[one(i,t) for i,t in enumerate(TARGETS)])
        await browser.close()
        print('BVS3FAST_RESULTS_BEGIN')
        for x in out: print(x['domain']+'\t'+x['url'])
        print('BVS3FAST_RESULTS_END')
        print('BVS3FAST_VALID_COUNT='+str(len(out)))
        print('BVS3FAST_RESULTS_JSON='+json.dumps(out,ensure_ascii=False))

asyncio.run(fast_main())
