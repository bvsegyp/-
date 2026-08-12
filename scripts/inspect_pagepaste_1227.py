import requests,re
from bs4 import BeautifulSoup
u='https://pagepaste.com/'
r=requests.get(u,timeout=30)
print('HOME_STATUS',r.status_code,'LEN',len(r.text))
s=BeautifulSoup(r.text,'html.parser')
for i,f in enumerate(s.find_all('form'),1):
    print('FORM',i,'action=',f.get('action'),'method=',f.get('method'),'id=',f.get('id'),'enctype=',f.get('enctype'))
    for el in f.find_all(['input','textarea','button']):
        print(' FIELD',el.name,'name=',el.get('name'),'type=',el.get('type'),'value=',el.get('value'),'id=',el.get('id'))
