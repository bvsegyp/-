import requests,re
pairs=[
('SWOLVY','https://swolvy.com/_next/static/chunks/037c.8q5civfh.js'),
('HTMLHOST','https://htmlhost.co/_next/static/chunks/137._jx5fg8a-.js?dpl=dpl_24G1J2HrAjb5ayYx4j4MRPVZgHbd')]
for name,u in pairs:
    print('\n===',name,'===')
    t=requests.get(u,timeout=30).text
    print('LEN',len(t))
    for needle in ['/api/upload','/api/sites']:
        low=t.lower(); k=needle.lower(); start=0
        while True:
            i=low.find(k,start)
            if i<0: break
            print('CTX',t[max(0,i-1800):min(len(t),i+3200)].replace('\n',' '))
            start=i+len(k)
