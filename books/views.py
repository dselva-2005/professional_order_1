from django.views.generic import ListView
from books.models import Book
    
class Books(ListView):
    model = Book
    