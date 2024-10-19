from .tasks import readings, kitabnow, bookberry, globalbook, vanguard, liberty
from .models import WebUrlsForScrape


readings_urls = WebUrlsForScrape.objects.filter(web_name='RC')
kitabnow_urls = WebUrlsForScrape.objects.filter(web_name='KN')
bookberry_urls = WebUrlsForScrape.objects.filter(web_name='BB')
globalbook_urls = WebUrlsForScrape.objects.filter(web_name='GB')
vanguard_urls = WebUrlsForScrape.objects.filter(web_name='VB')
liberty_urls = WebUrlsForScrape.objects.filter(web_name='LB')

# for r_url in readings_urls:
#     readings.delay(r_url.url)

for k_rul in kitabnow_urls:
    kitabnow.delay(k_rul.url)

for b_url in bookberry_urls:
    bookberry.delay(b_url.url)
    
for g_url in globalbook_urls:
    globalbook.delay(g_url.url)

for v_url in vanguard_urls:
    vanguard.delay(v_url.url)
    
for l_url in liberty_urls:
    liberty(l_url.url)