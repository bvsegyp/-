import requests,re,concurrent.futures
from urllib.parse import urljoin
sites=['https://swolvy.com/','https://oneclicklive.app/','https://htmlhost.co/']
for u in sites:
    print('\n===',u,'===')
    try:
        r=requests.get(u,timeout=30)
        print('HOME',r.status_code,len(r.text),r.url)
        html=r.text
        forms=re.findall(r'<form\b([^>]*)>(.*?)</form>',html,re.I|re.S)
        for idx,(attrs,body) in enumerate(forms[:10],1):
            print('FORM',idx,attrs[:500].replace('\n',' '))
            for m in re.finditer(r'<(input|textarea|button)\b([^>]*)>',body,re.I|re.S):
                print(' FIELD',m.group(1),m.group(2)[:500].replace('\n',' '))
        scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',html,re.I)
        print('SCRIPTS',scripts[:30])
        for s in scripts[:20]:
            su=urljoin(r.url,s)
            try:
                t=requests.get(su,timeout=30).text
                if len(t)<100: continue
                hits=[]
                for pat in [r'/api/[A-Za-z0-9_?&=./:-]+',r'https://[^"\'` ]+',r'fetch\([^)]{0,500}\)',r'axios\.[a-z]+\([^)]{0,500}\)']:
                    vals=re.findall(pat,t,re.I|re.S)
                    vals=[v for v in vals if any(k in str(v).lower() for k in ['api','upload','deploy','publish','site','page','share'])]
                    hits.extend(vals[:20])
                if hits:
                    print('SCRIPT',su,'LEN',len(t),'HITS')
                    for h in hits[:40]: print(' ',str(h)[:1500].replace('\n',' '))
            except Exception as e: print('SCRIPT_ERR',su,repr(e))
    except Exception as e: print('HOME_ERR',repr(e))
