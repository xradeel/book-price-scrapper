from bs4 import BeautifulSoup
import requests, random
from celery import shared_task
from .models import WebUrlsForScrape

headers_list = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    },
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.55',
    },
]

        
def save_url(cat_name, cat_url, web_name):
    try:
        WebUrlsForScrape.objects.update_or_create(
            url= cat_url,
            defaults={
                'category_name': cat_name,
                'web_name': web_name
            }
        )
    except Exception as e:
        print(f"Error saving product {cat_url}: {e}")



def readings_urls():
    headers = random.choice(headers_list)
    response = requests.get('https://readings.com.pk/', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.find('div', class_='col-megamenu borderd-box')
    category_list = categories.find_all('li')
    for i in category_list:
        cat_name = i.find('a').get_text(strip=True)
        cat_url = 'https://readings.com.pk'+i.find('a').get('href')
        save_url(cat_name=cat_name, cat_url=cat_url, web_name='RC')
    return True


def liberty_urls():
    headers = random.choice(headers_list)
    response = requests.get('https://www.libertybooks.com/', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.find('ul', class_='mega-menu-upper-ul')

    category_list = categories.find_all('li')
    for i in category_list:
        if i.find('a').get_text(strip=True) == 'Gifts & Stationery' or i.find('a').get_text(strip=True) == 'New & Notable':
            continue
        else:
            cat_name = i.find('a').get_text(strip=True)
            cat_url = i.find('a').get('href')
            save_url(cat_name=cat_name, cat_url=cat_url, web_name='LB')
    return True
