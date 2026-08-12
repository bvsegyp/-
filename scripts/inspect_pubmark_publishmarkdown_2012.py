import re,requests,json
from urllib.parse import urljoin

def inspect(base):
    try:
        h=requests.get(base,timeout=30).text
        print('BASE',base,'LEN',len(h))
        scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',h,re.I)
        for s in scripts[:80]:
            try:
                u=urljoin(base,s)
                t=requests.get(u,timeout=20).text
                if len(t)<100: continue
                for pat in [r'fetch\((.{0,1400})',r'axios\.(?:post|put)\((.{0,1200})',r'["\'](/api/[^"\']+)["\']',r'https://[^"\'` ]+/api/[^"\'` ]*']:
                    for m in re.findall(pat,t,re.I|re.S):
                        z=m if isinstance(m,str) else str(m)
                        zl=z.lower()
                        if any(k in zl for k in ['publish','markdown','document','page','create','api']):
                            print('CANDIDATE',base,z[:1400].replace('\n',' '))
            except Exception as e:
                print('SCRIPT_ERROR',base,repr(e))
    except Exception as e:
        print('BASE_ERROR',base,repr(e))

inspect('https://pubmark.site/editor')
inspect('https://publishmarkdown.com/')
