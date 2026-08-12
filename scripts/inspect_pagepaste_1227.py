import requests,re
from urllib.parse import urljoin
u='https://pagepaste.com/'
r=requests.get(u,timeout=30)
print('HOME_STATUS',r.status_code,'LEN',len(r.text))
html=r.text
scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',html,re.I)
print('SCRIPTS',scripts[:30])
for s in scripts:
    su=urljoin(u,s)
    try:
        t=requests.get(su,timeout=30).text
        print('SCRIPT',su,'LEN',len(t))
        if su.endswith('app.js'):
            for key in ['fetch(', 'upload', 'publish', 'shareable', 'FormData', 'POST', 'endpoint']:
                print('\nKEY',key)
                start=0
                shown=0
                low=t.lower(); k=key.lower()
                while shown<20:
                    i=low.find(k,start)
                    if i<0: break
                    print(t[max(0,i-350):min(len(t),i+700)].replace('\n',' '))
                    print('---')
                    start=i+len(k); shown+=1
    except Exception as e:
        print('ERR',su,repr(e))
