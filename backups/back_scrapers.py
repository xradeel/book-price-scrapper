from bs4 import BeautifulSoup
import random, time, unicodedata, requests
from .models import BooksRecord

class BaseScraper:
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

    def __init__(self, category):
        self.headers = random.choice(self.headers_list)
        self.category = category

    def fetch_page(self, url):
        response = requests.get(url, headers=self.headers)
        return BeautifulSoup(response.text, 'html.parser')

    def normalize_price(self, price):
        return unicodedata.normalize('NFKD', price).replace('Rs.', '').replace('Rs', '').replace('PKR', '').replace(',', '').strip()
    
    def save_product(self, data):
        try:
            BooksRecord.objects.update_or_create(
                url=data['url'],
                defaults={
                    'title': data['name'],
                    'image': data['image'],
                    'price': data['price'],
                    'author': data.get('author', '')  # Use an empty string if author is not available
                }
            )
        except Exception as e:
            print(f"Error saving product {data['url']}: {e}")


    def scrape(self):
        raise NotImplementedError("Subclasses should implement this method")
    

class ReadingsScraper(BaseScraper):


    def scrape(self):
        # products = []
        for key in self.category:
            next_link = self.category[key]
            while next_link != '#':
                soup = self.fetch_page(next_link)
                product_items = soup.find_all('div', class_='product-blk')
                for i in product_items:
                    url = i.find('a').get('href')
                    image =i.find('div', class_='product-img').find('img').get('data-src')
                    title = i.find('div', class_='product-title').get_text(strip=True)
                    author = i.find('div', class_='author').find('a').get_text(strip=True)
                    price = self.normalize_price(i.find('span', class_='sale-price').get_text(strip=True))
                    data = {'title': title, 'web': 'readings.com.pk', 'url': url, 'author': author, 'image': image, 'price': price}
                    # products.append(data)
                    self.save_product(data)
                next_link = soup.find('ul', class_='pagination justify-content-center m-0').find_all('a', class_='page-link arrows')[-1].get('href')
                time.sleep(2)
        # return products



class KitaabNowScraper(BaseScraper):
        
    def scrape(self):
        # products = []
        for key in self.category:
            next_link = self.category[key]
            while next_link != '#':
                soup = self.fetch_page(next_link)
                product_items = soup.find_all('div', class_='t-inside no-anim')
                for i in product_items:
                    image = i.find('div', class_='t-entry-visual-cont').find('a').find('img').get('data-src')
                    url = i.find('div', class_='t-entry-visual-cont').find('a').get('href')
                    title = i.find('h3', class_='t-entry-title font-762333 fontsize-160000 title-scale').find('a').get_text(strip=True)
                    price = self.normalize_price(i.find('span', class_='woocommerce-Price-amount amount').get_text(strip=True))
                    data = {'title': title, 'web': 'kitaabnow', 'url': url,'image': image, 'price': price}
                    # products.append({'title': title, 'url': url, 'image': image, 'price': price})
                next_link = soup.find('ul', class_='pagination').find('li', class_='page-next').find('a').get('href')
                time.sleep(2)
        # return products

class VanguardBooksScraper(BaseScraper):

    def scrape(self):
        # products = []
        for key in self.category:
            next_link = self.category[key]
            while next_link != '#':
                soup = self.fetch_page(next_link)
                product_items = soup.find_all('li', class_='product')
                for i in product_items:
                    image = i.find('div', class_='woocommerce-loop-product__header').find('a').find('img').get('src')
                    url = i.find('div', class_='woocommerce-loop-product__header').find('a').get('href')
                    title = i.find('h2', class_='woocommerce-loop-product__title').get_text(strip=True)
                    author = i.find('div', class_='woocommerce-loop-product__author').find('a').get_text(strip=True)
                    price = self.normalize_price(i.find('span', class_='woocommerce-Price-amount amount').get_text(strip=True))
                    data = {'title': title, 'web': 'vanguardbooks', 'url': url, 'author': author, 'image': image, 'price': price}
                    # products.append({'title': title, 'url': url, 'author': author, 'image': image, 'price': price})
                next_link = soup.find('nav', class_='woocommerce-pagination').find_all('li')[-1].find('a').get('href')
                time.sleep(2)
        # return products
    

class GlobalBooksScraper(BaseScraper):

    def scrape(self):
        # products = []
        for key in self.category:
            next_link = self.category[key]
            while next_link != '#':
                soup = self.fetch_page(next_link)
                product_items = soup.find_all('div', class_='t4s-product-wrapper')
                for i in product_items:
                    image = 'https:'+i.find('div', class_='t4s-product-img').find('img', class_='t4s-product-main-img').get('data-src')
                    image = image.split('&')[0]
                    url = 'https://globalbooks.com.pk/'+ i.find('h3', class_='t4s-product-title').find('a').get('href')
                    title = i.find('h3', class_='t4s-product-title').find('a').get_text(strip=True)
                    author = i.find('div', class_='t4s-product-vendor').find('a').get_text(strip=True)
                    price = self.normalize_price(i.find('span', class_='money').get_text(strip=True))
                    data = {'title': title, 'web': 'globalbooks', 'url': url, 'author': author, 'image': image, 'price': price}
                    # products.append({'title': title, 'url': url, 'author': author, 'image': image, 'price': price})
                next_link = 'https://globalbooks.com.pk/'+ soup.find('div', class_='t4s-pagination-wrapper t4s-w-100').find('a').get('href')
                time.sleep(2)
        # return products
    

class BookBerryScraper(BaseScraper):

    def scrape(self):
        # products = []
        for key in self.category:
            next_link = self.category[key]
            while next_link != '#':
                soup = self.fetch_page(next_link)
                product_items = soup.find_all('li', class_='product')
                for i in product_items:
                    image = i.find('img', class_='attachment-woocommerce_thumbnail size-woocommerce_thumbnail').get('src')
                    refrence = i.find('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')
                    title = i.find('h2', class_='woocommerce-loop-product__title').get_text(strip=True)
                    author = title.split('by')[-1]
                    url = refrence.get('href')
                    price = self.normalize_price(i.find('span', class_='price').find('ins').find('span').find('bdi').get_text(strip=True))
                    data = {'title': title, 'web': 'bookberry', 'url': url, 'author': author, 'image': image, 'price': price}
                    # products.append({'title': title, 'url': url, 'author': author, 'image': image, 'price': price})
                next_link = soup.find('ul', class_='page-numbers').find_all('a')[-1].get('href')
                time.sleep(2)
        # return products
    

class LibertyBooksScraper(BaseScraper):

    def scrape(self):
        # products = []
        for key in self.category:
            next_link = self.category[key]
            while next_link != '#':
                soup = self.fetch_page(next_link)
                product_items = soup.find_all('div', class_='product-items')
                for i in product_items:
                    url = i.find('div', class_='image col-lg-5 col-md-5 col-sm-5 col-xs-5').find('a').get('href')
                    image = i.find('div', class_='image col-lg-5 col-md-5 col-sm-5 col-xs-5').find('img').get('src')
                    title = i.find('div', class_='product-details col-lg-7 col-md-7 col-sm-7 col-xs-7').find('h4').find('a').get_text(strip=True)
                    author = i.find('p', class_='author').get_text(strip=True)
                    price = i.find('p', class_='price')
                    price = price.get_text(strip=True, separator=" ").replace(price.span.get_text(strip=True), '')
                    data = {'title': title, 'web': 'libertybooks', 'url': url, 'author': author, 'image': image, 'price': price}
                    # products.append({'title': title, 'url': url, 'author': author, 'image': image, 'price': price})
                next_link = soup.find('ul', class_='pagination').find_all('a')[-1].get('href')
                time.sleep(2)
        # return products




