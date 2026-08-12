import requests,re
u='https://sharemyhtml.com/assets/index-Cj1mIbFj.js'
t=requests.get(u,timeout=30).text
print('LEN',len(t))
for needle in ['/api/upload','FormData','append(']:
    print('\n===',needle,'===')
    start=0
    count=0
    while True:
        i=t.find(needle,start)
        if i<0: break
        print(t[max(0,i-1800):i+2600])
        print('\n---SNIP---\n')
        count+=1
        if count>=8: break
        start=i+len(needle)
# Also regex likely formData append names near upload call
for m in re.finditer(r'\.append\((.{0,250})',t):
    z=m.group(0)
    if any(k in z.lower() for k in ['file','html','upload','content']):
        print('APPEND',z[:500])
