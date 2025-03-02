# 📚 Book Price Scraper (Deals of Books)  

[![Django][Django-badge]][Django-url] [![Celery][Celery-badge]][Celery-url] [![Elasticsearch][Elasticsearch-badge]][Elasticsearch-url] [![RabbitMQ][RabbitMQ-badge]][RabbitMQ-url] [![PostgreSQL][PostgreSQL-badge]][PostgreSQL-url] [![Docker][Docker-badge]][Docker-url]  

## 📖 About  

Imagine you’re searching for a book online, but every website has different prices, discounts, and deals. You spend hours comparing prices manually across multiple bookstores, wishing for a simpler solution.  

This project **solves that problem!** It automatically **scrapes book data** from the **top 10 bookstores**, including titles, authors, prices, and special deals. The collected data is stored in a **database** and updated **periodically** using automated tasks.  

When you search for a book, **Elasticsearch** provides **lightning-fast results** by efficiently scanning the database. The system then **sorts and displays the best deals**, making sure you get the most affordable option **without the hassle of manual searching**.  

With **Django for the backend**, **Celery for task management**, **RabbitMQ for message queuing**, and **Docker for seamless deployment**, this project ensures a **fast, scalable, and real-time book price aggregator**.  

---

### **Key Highlights**  

- 🔍 **Automated Web Scraping** – Fetches book details from **10+ stores**.  
- 🔁 **Scheduled Updates** – Periodically refreshes prices using **cron jobs**.  
- ⚡ **Fast Search Engine** – Uses **Elasticsearch** for real-time, **full-text search**.  
- 🎯 **Smart Sorting** – Ranks results based on price, availability, and deals.  
- 🏗️ **Scalable & Reliable** – Built using **Django, Celery, RabbitMQ, and Docker**.  

Now, instead of spending hours comparing prices, you get the **best book deals instantly!** 📚✨  


---

## 🚀 Features  

✅ **Multi-site Web Scraping** – Collects book details (title, author, price, image, deals) from **10+ bookstores**.  
✅ **Automated Cron Jobs** – Periodic execution of scrapers ensures an up-to-date book database.  
✅ **Full-Text Search with Elasticsearch** – Fast and intelligent book search using **Elasticsearch**.  
✅ **Asynchronous Task Execution** – **Celery + RabbitMQ** for high-performance background processing.  
✅ **Sorted & Filtered Results** – Books sorted by **price, availability, and popularity**.  
✅ **Containerized Deployment** – Uses **Docker** for easy setup and scalability.  

---

## 🛠️ Tech Stack  

- **Backend**: [![Django][Django-badge]][Django-url] **Django**, **Celery**  
- **Scraping**: BeautifulSoup, Requests  
- **Database**: [![PostgreSQL][PostgreSQL-badge]][PostgreSQL-url] **PostgreSQL**  
- **Search Engine**: [![Elasticsearch][Elasticsearch-badge]][Elasticsearch-url] **Elasticsearch**  
- **Message Broker**: [![RabbitMQ][RabbitMQ-badge]][RabbitMQ-url] **RabbitMQ**  
- **Containerization**: [![Docker][Docker-badge]][Docker-url] **Docker**  

---

## 🔧 Setup & Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/xradeel/deals-of-books.git
cd deals-of-books
```  

2️⃣ **Set up a virtual environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```  

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```  

4️⃣ **Run RabbitMQ and Celery**  
```bash
celery -A deals-of-books worker --loglevel=info
```  

5️⃣ **Run Django server**  
```bash
python manage.py runserver
```  

6️⃣ **Start Elasticsearch using Docker**  
```bash
docker-compose up -d
```  

7️⃣ **Apply Migrations & Create Superuser**  
```bash
python manage.py migrate
python manage.py createsuperuser
```  

---

## 🔍 How It Works  

1️⃣ **Scraping & Storage**  
- The system scrapes **10+ bookstores** for book details and deals.  
- Scraped data is stored in **MySQL**.  
- Scrapers run periodically using **cron jobs** to update the database.  

2️⃣ **Efficient Search**  
- When a user searches for a book, **Elasticsearch** provides fast & accurate results.  
- Results are **sorted by price** and displayed with book images and store links.  

---

## 📸 Screenshots  

*(Add screenshots of your UI here)*  

---

## 📌 Future Enhancements  

- [ ] **User Authentication** – Allow users to save favorite books.  
- [ ] **Advanced Filtering** – Filter books by category, author, and price range.  
- [ ] **Real-time Price Alerts** – Notify users of price drops.  

---

## 🤝 Contributions  

Contributions are welcome! Feel free to **fork the repository**, **open issues**, and **submit pull requests**.  

---

## 📝 License  

This project is open-source and available under the **MIT License**.  
 

[Django-badge]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white  
[Django-url]: https://www.djangoproject.com/  

[Celery-badge]: https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white  
[Celery-url]: https://docs.celeryq.dev/en/stable/  

[Elasticsearch-badge]: https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white  
[Elasticsearch-url]: https://www.elastic.co/elasticsearch/  

[RabbitMQ-badge]: https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white  
[RabbitMQ-url]: https://www.rabbitmq.com/  

[PostgreSQL-badge]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white  
[PostgreSQL-url]: https://www.postgresql.org/  

[Docker-badge]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white  
[Docker-url]: https://www.docker.com/  
