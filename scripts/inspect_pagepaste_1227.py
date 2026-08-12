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
        for pat in [r'https://[^"\' ]+',r'/api/[A-Za-z0-9_?&=./:-]+',r'fetch\([^)]{0,300}\)',r'axios\.[a-z]+\([^)]{0,300}\)']:
            vals=re.findall(pat,t,re.I)
            if vals:
                print('MATCHES',pat,vals[:30])
    except Exception as e:
        print('ERR',su,repr(e))
