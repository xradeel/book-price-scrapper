from celery import shared_task
from .scrapers import ReadingsScraper, KitaabNowScraper, VanguardBooksScraper, GlobalBooksScraper, BookBerryScraper, LibertyBooksScraper
from .scrape_web_urls import readings_urls, liberty_urls
@shared_task
def readings(category):
    # category = {'fiction': 'https://readings.com.pk/category/level1/73/A'}
    scraper = ReadingsScraper(category)
    return scraper.scrape()


@shared_task
def kitabnow(category):
    scraper = KitaabNowScraper(category)
    return scraper.scrape()

@shared_task
def vanguard(category):
    scraper = VanguardBooksScraper(category)
    return scraper.scrape()


@shared_task
def globalbook(category):
    scraper = GlobalBooksScraper(category)
    return scraper.scrape()


@shared_task
def bookberry(category):
    scraper = BookBerryScraper(category)
    return scraper.scrape()


@shared_task
def liberty(category):
    scraper = LibertyBooksScraper(category)
    return scraper.scrape()

@shared_task
def scrape_urls():
    readings_urls()
    liberty_urls()
    