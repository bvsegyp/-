import requests,re
u='https://pagepaste.com/'
r=requests.get(u,timeout=30)
print('HOME_STATUS',r.status_code,'LEN',len(r.text))
html=r.text
forms=re.findall(r'<form\b([^>]*)>(.*?)</form>',html,re.I|re.S)
print('FORM_COUNT',len(forms))
for i,(attrs,body) in enumerate(forms,1):
    def attr(name):
        m=re.search(r'\b'+re.escape(name)+r'\s*=\s*["\']([^"\']*)',attrs,re.I)
        return m.group(1) if m else ''
    print('FORM',i,'action=',attr('action'),'method=',attr('method'),'id=',attr('id'),'enctype=',attr('enctype'))
    for m in re.finditer(r'<(input|textarea|button)\b([^>]*)>',body,re.I|re.S):
        tag=m.group(1).lower(); a=m.group(2)
        def aval(name):
            x=re.search(r'\b'+re.escape(name)+r'\s*=\s*["\']([^"\']*)',a,re.I)
            return x.group(1) if x else ''
        print(' FIELD',tag,'name=',aval('name'),'type=',aval('type'),'value=',aval('value'),'id=',aval('id'))
