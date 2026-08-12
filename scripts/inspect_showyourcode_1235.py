import requests,re
from urllib.parse import urljoin
u='https://www.showyourcode.app/'
r=requests.get(u,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
html=r.text
for pat in [r'<form\b[^>]*action=["\']([^"\']*)',r'/api/[A-Za-z0-9_?&=./:-]+',r'https://[^"\' ]+']:
    vals=re.findall(pat,html,re.I)
    if vals: print('HTML_MATCH',pat,vals[:30])
scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',html,re.I)
print('SCRIPTS',scripts[:40])
for s in scripts:
    su=urljoin(r.url,s)
    try:
        t=requests.get(su,timeout=30).text
        print('SCRIPT',su,'LEN',len(t))
        for key in ['fetch(', '/api/', 'supabase', 'insert(', 'share', 'snippet', 'work']:
            low=t.lower(); k=key.lower(); start=0; shown=0
            while shown<8:
                i=low.find(k,start)
                if i<0: break
                print('KEY',key,t[max(0,i-250):min(len(t),i+600)].replace('\n',' '))
                start=i+len(k); shown+=1
    except Exception as e: print('ERR',su,repr(e))
