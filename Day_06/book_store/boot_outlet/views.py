from audioop import avg
from tracemalloc import get_object_traceback
from django.shortcuts import get_object_or_404, render
from django.http import Http404
import math
from . models import Book
from django.db.models import Avg, Max, Min
# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-rating")
    total_books = books.count()
    avg_rating = books.aggregate(Avg("rating")) 
    for book in books:
        autor=book
        rating=book.rating
        is_bestselling=book.is_bestselling
    
    
    return render(request,'index.html',{
        "books":books,
        "total_books":total_books,
        "avg_rating":avg_rating,
        "author":autor,
        "rating":rating,
        "is_bestselling":is_bestselling,
        
    })

def book_detail(request, slug):
    
    book = get_object_or_404(Book,slug=slug)
    return render(request, "book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestselling": book.is_bestselling,
    })