import requests
u='https://www.showyourcode.app/share/8kx6tcmspwgkol'
r=requests.get(u,timeout=30)
ok=r.status_code<400 and 'smmfansfaster.com' in r.text.lower()
print('STATUS',r.status_code,'LEN',len(r.text),'BACKLINK',ok)
if ok: print('RESULT_URL='+u)
