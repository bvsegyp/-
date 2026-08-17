import requests,re,json,html
TARGET='https://colorfulcloudco.com/شركة-تنظيف-منازل-في-الرياض/'
ANCHOR='أفضل شركة تنظيف في الرياض'
page=f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>دليل اختيار شركة تنظيف منازل في الرياض</title><meta name="description" content="معايير عملية لاختيار خدمة تنظيف المنازل والشقق والفلل في الرياض"></head><body><main style="max-width:900px;margin:40px auto;padding:0 24px;font-family:Arial,Tahoma,sans-serif;line-height:1.95"><h1>دليل اختيار شركة تنظيف منازل في الرياض</h1><p>اختيار خدمة تنظيف مناسبة يحتاج إلى النظر في نطاق العمل وجودة الأدوات والمنظفات وخبرة فريق التنفيذ، وليس السعر وحده. تختلف احتياجات الشقق والفلل حسب المساحة وطبيعة الأثاث وعدد الغرف ومستوى الاستخدام اليومي.</p><h2>حدد نوع التنظيف المطلوب</h2><p>قد يحتاج المنزل إلى تنظيف دوري للمحافظة على ترتيبه، أو تنظيف عميق يشمل الزوايا والنوافذ والمطابخ والحمامات والمناطق خلف الأثاث. تحديد المطلوب قبل الحجز يجعل الخدمة أوضح ويساعد على تقييم النتيجة بعد الانتهاء.</p><h2>قارن الجودة قبل اتخاذ القرار</h2><p>عند البحث عن <a href="{TARGET}">{ANCHOR}</a> من المهم مراجعة ما تتضمنه الخدمة وطريقة التعامل مع الأسطح المختلفة ومدى وضوح التواصل قبل بدء العمل.</p><h2>المطبخ والحمامات يحتاجان عناية خاصة</h2><p>تتراكم الدهون والرطوبة في هذه المناطق بسرعة، لذلك تحتاج إلى أدوات ومنظفات مناسبة مع الاهتمام بالزوايا والأرضيات والجدران والأسطح ومناطق اللمس المتكرر.</p><h2>المعدات المنظمة ترفع كفاءة العمل</h2><p>استخدام الأدوات المناسبة لكل مهمة يساعد على تحسين النتيجة وتقليل الوقت. كما أن الفصل بين أدوات المطبخ والحمامات وبقية المنزل يقلل انتقال الأوساخ ويحسن مستوى النظافة.</p><h2>راجع النتيجة</h2><p>بعد انتهاء الخدمة، من المفيد مراجعة النقاط الأساسية ومطابقتها مع ما تم الاتفاق عليه. التنظيم والوضوح في نطاق العمل يساعدان على الحصول على تجربة أفضل عند تكرار الحجز مستقبلًا.</p><p>في النهاية، الجودة الحقيقية تظهر في التفاصيل وطريقة التنفيذ والاهتمام بالأسطح والمناطق التي تحتاج إلى عناية أكبر.</p></main></body></html>'''
s=requests.Session();s.headers.update({'User-Agent':'Mozilla/5.0 ColorfulCloudSEO/4.0'})
try:
 r=s.post('https://sshgrid.com/api/v1/deploy',json={'files':[{'path':'index.html','content':page}],'label':'Riyadh Home Cleaning Guide'},timeout=45)
 print('SSHGRID_POST',r.status_code,r.text[:1000])
 d=r.json() if r.ok else {};u=d.get('url') or d.get('site_url') or d.get('public_url') or ''
 if u:
  v=s.get(u,timeout=40,allow_redirects=True)
  noindex=('noindex' in v.headers.get('x-robots-tag','').lower()) or bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex',v.text,re.I))
  anchors=len(re.findall(r'<a[^>]+href=["\'][^"\']*colorfulcloudco\.com[^"\']*["\'][^>]*>\s*أفضل شركة تنظيف في الرياض\s*</a>',v.text,re.I))
  print('VERIFY',v.status_code,v.url,'ANCHORS',anchors,'NOINDEX',int(noindex))
  if v.status_code<400 and anchors>=1 and not noindex:print('COLORFUL_SSHGRID_RESULT='+v.url)
except Exception as e:print('SSHGRID_ERR',repr(e))
