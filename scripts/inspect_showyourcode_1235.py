import requests,re
from urllib.parse import urljoin
u='https://www.showyourcode.app/'
r=requests.get(u,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
main=urljoin(r.url,re.findall(r'<script[^>]+src=["\']([^"\']+)',r.text,re.I)[0])
t=requests.get(main,timeout=30).text
chunks=sorted(set(re.findall(r'assets/[A-Za-z0-9_.-]+\.js',t)))
print('CHUNKS',len(chunks))
for c in chunks:
    if not any(x in c.lower() for x in ['route','work','editor','home','index']):
        continue
    cu=urljoin(r.url,c)
    try:
        z=requests.get(cu,timeout=30).text
        hits=[]
        for needle in ['/api/works','syc_anon_works','localStorage.setItem','uuid','html']:
            if needle.lower() in z.lower(): hits.append(needle)
        if not hits: continue
        print('\nCHUNK',cu,'LEN',len(z),'HITS',hits)
        for needle in ['/api/works','syc_anon_works']:
            low=z.lower(); k=needle.lower(); start=0; shown=0
            while shown<20:
                i=low.find(k,start)
                if i<0: break
                print('CTX',needle,z[max(0,i-900):min(len(z),i+1800)].replace('\n',' '))
                start=i+len(k); shown+=1
    except Exception as e: print('ERR',cu,repr(e))
