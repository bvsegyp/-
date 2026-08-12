import requests,re
u='https://sharemyhtml.com/assets/index-Cj1mIbFj.js'
t=requests.get(u,timeout=30).text
for needle in ['uploadPage','mutateAsync','mutationFn','uz(','dz(','/api/upload']:
 print('\n===',needle,'===')
 start=0
 for _ in range(12):
  i=t.find(needle,start)
  if i<0: break
  print(t[max(0,i-2500):i+3500])
  print('\n---\n')
  start=i+len(needle)
# likely object keys around file reading / FileReader
for pat in [r'FileReader.{0,4000}',r'readAsText.{0,4000}',r'\.text\(\).{0,3000}',r'uploadPage.{0,5000}']:
 for m in re.finditer(pat,t,re.I|re.S):
  z=m.group(0)
  if 'upload' in z.lower() or 'html' in z.lower(): print('REGEX',z[:6000])
