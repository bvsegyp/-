import requests,re,concurrent.futures
from urllib.parse import urljoin
u='https://www.showyourcode.app/'
r=requests.get(u,timeout=30)
print('HOME',r.status_code,len(r.text),r.url)
main=urljoin(r.url,re.findall(r'<script[^>]+src=["\']([^"\']+)',r.text,re.I)[0])
t=requests.get(main,timeout=30).text
chunks=sorted(set(re.findall(r'assets/[A-Za-z0-9_.-]+\.js',t)))
print('CHUNKS',len(chunks))
def get(c):
    cu=urljoin(r.url,c)
    try:
        z=requests.get(cu,timeout=20).text
        if '/api/works' in z or 'syc_anon_works' in z:
            return cu,z
    except Exception as e:
        return None
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
    for result in ex.map(get,chunks):
        if not result: continue
        cu,z=result
        print('\nCHUNK',cu,'LEN',len(z))
        for needle in ['/api/works','syc_anon_works']:
            low=z.lower(); k=needle.lower(); start=0; shown=0
            while shown<30:
                i=low.find(k,start)
                if i<0: break
                print('CTX',needle,z[max(0,i-1100):min(len(z),i+2400)].replace('\n',' '))
                start=i+len(k); shown+=1
