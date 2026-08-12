import requests,re
from urllib.parse import urljoin
u='https://www.showyourcode.app/'
r=requests.get(u,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',r.text,re.I)
for s in scripts:
    su=urljoin(r.url,s)
    try:
        t=requests.get(su,timeout=30).text
        print('SCRIPT',su,'LEN',len(t))
        for pat in [r'["\'](/api/works[^"\']*)["\']',r'\b(?:Pt|St)\(`(/api/works[^`]*)`([^)]{0,900})\)',r'\b(?:Pt|St)\(["\'](/api/works[^"\']*)["\']([^)]{0,900})\)']:
            vals=re.findall(pat,t,re.I|re.S)
            print('PAT',pat,'COUNT',len(vals))
            for v in vals[:50]: print('MATCH',v)
        low=t.lower(); start=0
        while True:
            i=low.find('/api/works',start)
            if i<0: break
            print('CTX',t[max(0,i-700):min(len(t),i+1400)].replace('\n',' '))
            start=i+10
    except Exception as e: print('ERR',su,repr(e))
