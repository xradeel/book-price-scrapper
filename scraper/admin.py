from django.contrib import admin
from .models import WebUrlsForScrape, BooksRecord

# Register your models here.

class WebUrlsForScrapeAdmin(admin.ModelAdmin):
    list_display = ('web_name', 'category_name', 'url')
    
    
admin.site.register(WebUrlsForScrape, WebUrlsForScrapeAdmin)


class BooksRecordAdmin(admin.ModelAdmin):
    list_display = ('category_id','title', 'price', 'url')

admin.site.register(BooksRecord, BooksRecordAdmin)