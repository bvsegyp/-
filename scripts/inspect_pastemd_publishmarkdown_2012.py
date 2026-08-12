import re,requests,json
from urllib.parse import urljoin

def inspect(base):
    try:
        h=requests.get(base,timeout=30).text
        print('BASE='+base+' LEN='+str(len(h)))
        scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',h,re.I)
        print('SCRIPTS='+json.dumps(scripts[:50]))
        for s in scripts[:80]:
            try:
                u=urljoin(base,s); t=requests.get(u,timeout=20).text
                if len(t)<100: continue
                for needle in ['/api/','createDocument','create_document','publish','share','documents','markdowns','instantdb','transact']:
                    pos=0; count=0
                    while True:
                        i=t.lower().find(needle.lower(),pos)
                        if i<0 or count>=12: break
                        z=t[max(0,i-600):min(len(t),i+1400)]
                        print('SNIP='+base+' '+z.replace('\n',' ')[:2000])
                        pos=i+len(needle); count+=1
            except Exception as e: print('SCRIPT_ERR='+repr(e))
    except Exception as e: print('BASE_ERR='+repr(e))

inspect('https://pastemd.io/')
inspect('https://publishmarkdown.com/')
