from typing import Any
from django.shortcuts import render,get_object_or_404,render,reverse
from django.urls import reverse_lazy
from .models import Book,Comment,Reply,Review,ReviewReply
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.views import View
from .forms import commentForm,BookForm,ReviewForm
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view
from .serializers import ReplyDeserializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # Correct the import


# views.py
from rest_framework import generics
from .models import Reply
from .serializers import ReplyDeserializer

class CreateReplyView(generics.CreateAPIView):
    queryset = ReviewReply.objects.all()
    serializer_class = ReplyDeserializer


@api_view(['GET'])
def getReplies(request,pk):
    replies = get_object_or_404(Review,id=pk)
    if(not replies):
       return Response(replies) 
    serializer = ReplyDeserializer(replies.reply,many=True)
    return Response(serializer.data)



@api_view(['POST'])
@login_required
def CreateReply(request):
    if request.method == 'POST':
        serializer = ReplyDeserializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



'''
def get_books(request):
    books = Book.objects.all()
    return render(request,'books/get_books.html',{'books':books})
'''
class commentCreateView(LoginRequiredMixin,View):
    template_name = 'books/detail_book.html'
    def get(self,request,bookId):
        print('inside the get')
        comment_form = commentForm()
        return render(request, self.template_name, {'comment_form':comment_form})
    
    def post(self,request,bookId):
        book = Book.objects.get(id=bookId)
        form = commentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(commentedUser=request.user, book=book, comment=form.cleaned_data.get('comment'))
            print('created!!    ')
            return HttpResponseRedirect(reverse('detail_book',args=(book.pk,)))
        return render(request, self.template_name, {'comment_form':form})


class books_listview(ListView):
    model = Book
    template_name = 'books/get_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            return Book.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(genre__icontains=query)
            )

        return Book.objects.all()

class book_detailview(DetailView):
    model = Book
    template_name='books/detail_book.html'
    context_object_name = 'book'
    form_class = commentForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['commentForm']=self.form_class()
        return context


def replyView(request):
    return HttpResponse('Great_done')


class CreateBookView(LoginRequiredMixin,CreateView):
    model = Book
    template_name='books/postbook.html'
    form_class = BookForm
    success_url='books/'

    def form_valid(self, form):
        # Automatically set the user and book for the comment
        form.instance.user = self.request.user
        return super().form_valid(form)

class reviewCreate(LoginRequiredMixin,View):
    template_name = 'books/detail_book.html'
    def post(self,request,bookId):
        try:
            review = Review.objects.get(reviewedUser__id = request.user.id ,book__id = bookId)
            form = ReviewForm(request.POST,instance=review)
            form.save()
            return HttpResponseRedirect(reverse('detail_book',args=(bookId,)))
        except Review.DoesNotExist:
            form=ReviewForm(request.POST)
            if form.is_valid():
                data = form.save(commit=False)  # Create a Review instance but don't save it yet
                data.reviewedUser = request.user
                data.book_id = bookId  # Assuming you have a 'book' field in your Review model
                data.save()
                return HttpResponseRedirect(reverse('detail_book', args=(bookId,)))
            else:
                return HttpResponseRedirect(reverse('detail_book', args=(bookId,)))  # Handle form validation errors

class SuperuserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have superuser privileges.")
        return super().dispatch(request, *args, **kwargs)



class UpdateBook(SuperuserRequiredMixin,View):
    form_class=BookForm
    template_name = 'book/get_books.html'
    def post(self,request,bookId):
        print('calling')
        book=Book.objects.get(id=bookId)
        form = BookForm(request.POST,instance=book)
        print(form.errors)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('get_books'))

class DeleteBook(SuperuserRequiredMixin,DeleteView):
    model=Book
    success_url = reverse_lazy('get_books')

class ReviewDelete(SuperuserRequiredMixin,DeleteView):
    model = Review  
    def get_success_url(self):
        return reverse('detail_book', args=[self.get_object().book.pk])

    def delete(self,request,*args,**kwargs):
        obj = self.get_object()
        obj.delete()
        return HttpResponseRedirect(self.success_url)

