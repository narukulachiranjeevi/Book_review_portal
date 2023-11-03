from django.shortcuts import render,get_object_or_404,render
from .models import Book
from django.views.generic import ListView

'''
def get_books(request):
    books = Book.objects.all()
    return render(request,'books/get_books.html',{'books':books})
'''
class get_books_list_view(ListView):
    model = Book
    template_name = 'books/get_books.html'
    context_object_name = 'books'