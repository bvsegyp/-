import json,re,requests
from urllib.parse import urljoin

home=requests.get('https://dochost.io/',timeout=30).text
scripts=re.findall(r'<script[^>]+src=["\']([^"\']+)',home,re.I)
print('DOCHOST_SCRIPTS='+json.dumps(scripts))
seen=set()
for s in scripts:
    if s.startswith('http') and 'dochost.io' not in s: continue
    try:
        u=urljoin('https://dochost.io/',s)
        t=requests.get(u,timeout=20).text
        if len(t)<50: continue
        for pat in [r'https://[^"\'` ]+', r'["\'`](/api/[^"\'` ]+)["\'`]', r'fetch\((.{0,1200})', r'axios\.(?:post|put)\((.{0,1000})']:
            for m in re.findall(pat,t,re.I|re.S):
                z=m if isinstance(m,str) else str(m)
                zl=z.lower()
                if any(k in zl for k in ['api','publish','upload','document','page','markdown','html']):
                    z=z[:1200]
                    if z not in seen:
                        seen.add(z); print('CANDIDATE='+z.replace('\n',' ')[:1200])
    except Exception as e:
        print('SCRIPT_ERROR='+repr(e))
