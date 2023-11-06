from django.shortcuts import render,get_object_or_404,render,reverse
from django.urls import reverse_lazy
from .models import Book,Comment,Reply
from django.views.generic import ListView,DetailView,DeleteView,CreateView
from django.views import View
from .forms import commentForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view
from .serializers import ReplyDeserializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

# views.py
from rest_framework import generics
from .models import Reply
from .serializers import ReplyDeserializer

class CreateReplyView(generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplyDeserializer


@api_view(['GET'])
def getReplies(request,pk):
    replies = get_object_or_404(Comment,id=pk)
    if(not replies):
       return Response(replies) 
    serializer = ReplyDeserializer(replies.replies,many=True)
    return Response(serializer.data)



@api_view(['POST'])
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
        print('inside the post')
        if form.is_valid():
            Comment.objects.create(commentedUser=request.user, book=book, comment=form.cleaned_data.get('comment'))
            print('created!!    ')
            return HttpResponseRedirect(reverse('detail_book',args=(book.pk,)))
        return render(request, self.template_name, {'comment_form':form})


class books_listview(ListView):
    model = Book
    template_name = 'books/get_books.html'
    context_object_name = 'books'

class book_detailview(DetailView):
    model = Book
    template_name='books/detail_book.html'
    context_object_name = 'book'
    form_class = commentForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['commentForm']=self.form_class()
        return context


class commentDeleteView(DeleteView):
    model = Comment 
    
    def get_success_url(self):
        return reverse('detail_book', args=[self.get_object().book.pk])

    def delete(self,request,*args,**kwargs):
        comment = self.get_object()
        if request.user == comment.commentedUser:
            super(CommentDeleteView,self).delete(request, *args, **kwargs)
            return self.get_success_url
        return HttpResponseRedirect(reverse('detail_book',args=(Comment.objects.book.pk,)))

def replyView(request):
    return HttpResponse('Great_done')


    
