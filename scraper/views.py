from django.shortcuts import render
from .documents import BookDocument


# Create your views here.

def index(request):
    query = request.GET.get('query')
    if query:
        books = BookDocument.search().query("match", title=query)
        return render(request, 'scraper/index.html', {'books': books})
        
    else:
        return render(request, 'scraper/index.html')
    # return render(request,'scraper/index.html')

def search(request):
    query = request.GET.get('q')
    if query:
        books = BookDocument.search().query("match", title=query)
    else:
        books = BookDocument.search().all()
    return render(request, 'scraper/index.html', {'books': books})