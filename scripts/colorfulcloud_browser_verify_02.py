import asyncio,json,re
from playwright.async_api import async_playwright

ANCHOR='أفضل شركة تنظيف في الرياض'
TARGET='colorfulcloudco.com'
URLS=[
 ('pastebox.ai','https://pastebox.ai/oB7KbFO5'),
 ('showyourcode.app','https://www.showyourcode.app/share/9bvs2gmswmlgqp')
]

async def verify(browser,name,url):
 p=await browser.new_page()
 try:
  await p.goto(url,wait_until='domcontentloaded',timeout=45000)
  await p.wait_for_timeout(2500)
  pages=[p]+list(p.frames)
  matches=0
  noindex=False
  for fr in pages:
   try:
    loc=fr.locator(f'a[href*="{TARGET}"]')
    for i in range(await loc.count()):
     a=loc.nth(i)
     txt=(await a.inner_text()).strip()
     if ANCHOR in txt:matches+=1
   except:pass
  try:
   robots=await p.locator('meta[name="robots"]').get_attribute('content') if await p.locator('meta[name="robots"]').count() else ''
   noindex='noindex' in (robots or '').lower()
  except:pass
  print('BROWSER_VERIFY',name,p.url,'MATCHES',matches,'NOINDEX',int(noindex))
  return {'source':name,'url':p.url} if matches>=1 and not noindex else None
 except Exception as e:
  print('BROWSER_ERR',name,repr(e));return None
 finally:
  await p.close()

async def main():
 async with async_playwright() as pw:
  b=await pw.chromium.launch(headless=True)
  out=[]
  for name,url in URLS:
   r=await verify(b,name,url)
   if r:out.append(r)
  await b.close()
  print('COLORFUL_BROWSER2_RESULTS_BEGIN')
  for x in out:print(x['source']+'\t'+x['url'])
  print('COLORFUL_BROWSER2_RESULTS_END')
  print('COLORFUL_BROWSER2_VALID_COUNT='+str(len(out)))
  print('COLORFUL_BROWSER2_RESULTS_JSON='+json.dumps(out,ensure_ascii=False))

asyncio.run(main())
