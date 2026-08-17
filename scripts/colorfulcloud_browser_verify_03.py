import asyncio,json
from playwright.async_api import async_playwright
ANCHOR='أفضل شركة تنظيف في الرياض'
TARGET='colorfulcloudco.com'
URLS=[
 ('xdr.no','https://0tp3bqnc3j.xdr.no/'),
 ('draftlet.io','https://ivory-meadow-1977.draftlet.io/'),
 ('draftmark.app','https://draftmark.app/share/t7PCHdXS'),
 ('pastebox.ai','https://pastebox.ai/oB7KbFO5'),
 ('showyourcode.app','https://www.showyourcode.app/share/9bvs2gmswmlgqp')
]
async def verify(browser,name,url):
 p=await browser.new_page()
 try:
  await p.goto(url,wait_until='domcontentloaded',timeout=45000)
  await p.wait_for_timeout(2500)
  matches=0
  for fr in [p]+list(p.frames):
   try:
    loc=fr.locator(f'a[href*="{TARGET}"]')
    for i in range(await loc.count()):
     if ANCHOR in ((await loc.nth(i).inner_text()) or ''):matches+=1
   except:pass
  robots=''
  try:
   if await p.locator('meta[name="robots"]').count():robots=(await p.locator('meta[name="robots"]').first.get_attribute('content')) or ''
  except:pass
  noindex='noindex' in robots.lower()
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
  for n,u in URLS:
   r=await verify(b,n,u)
   if r:out.append(r)
  await b.close()
  print('COLORFUL_BROWSER3_RESULTS_BEGIN')
  for x in out:print(x['source']+'\t'+x['url'])
  print('COLORFUL_BROWSER3_RESULTS_END')
  print('COLORFUL_BROWSER3_VALID_COUNT='+str(len(out)))
  print('COLORFUL_BROWSER3_RESULTS_JSON='+json.dumps(out,ensure_ascii=False))
asyncio.run(main())
