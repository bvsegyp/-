import requests,re,json,time
URL='https://shy-dove-5245.sshgrid.com'
STATUS='https://sshgrid.com/api/v1/sites/shy-dove-5245'
ANCHOR='أفضل شركة تنظيف في الرياض'
for attempt in range(8):
    try:
        sr=requests.get(STATUS,timeout=15,headers={'User-Agent':'Mozilla/5.0 ColorfulCloudVerifier/1.0'})
        print('STATUS',attempt,sr.status_code,sr.text[:700].replace('\n',' '))
        if sr.ok:
            try:
                d=sr.json(); live=d.get('url_live') or d.get('url') or URL
            except Exception:
                live=URL
        else: live=URL
        r=requests.get(live,timeout=20,allow_redirects=True,headers={'User-Agent':'Mozilla/5.0 ColorfulCloudVerifier/1.0'})
        noindex=('noindex' in r.headers.get('x-robots-tag','').lower()) or bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex',r.text,re.I))
        anchors=len(re.findall(r'<a[^>]+href=["\'][^"\']*colorfulcloudco\.com[^"\']*["\'][^>]*>\s*أفضل شركة تنظيف في الرياض\s*</a>',r.text,re.I))
        print('VERIFY',attempt,r.status_code,r.url,'ANCHORS',anchors,'NOINDEX',int(noindex))
        if r.status_code<400 and anchors>=1 and not noindex:
            print('COLORFUL_SSHGRID_FINAL='+r.url)
            raise SystemExit(0)
    except SystemExit: raise
    except Exception as e:
        print('TRY_ERR',attempt,repr(e))
    time.sleep(4)
print('COLORFUL_SSHGRID_FINAL=')
