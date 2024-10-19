from django.db import models

# Create your models here.

class WebUrlsForScrape(models.Model):
    website_choice = {
        ('RC', 'readings.com.pk'),
        ('VB', 'vanguardbooks.com'),
        ('GB', 'globalbooks.com'),
        ('LB', 'libertybooks.com'),
        ('KN', 'kitabnow.com'),
        ('BB', 'bookberry.com'),
    }
    web_name = models.CharField(max_length=5, choices=website_choice)
    category_name = models.CharField(max_length=100, default='Books')
    url = models.TextField(default='#')

class BooksRecord(models.Model):
    category_id = models.CharField(max_length=5, default='RC')
    title = models.CharField(max_length=255)
    image = models.TextField()
    url = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=255)
    