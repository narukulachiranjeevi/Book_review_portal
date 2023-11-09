from django.urls import path
from . import views

urlpatterns = [
    path('',views.books_listview.as_view(),name='get_books'),
    path('<int:pk>/',views.book_detailview.as_view(),name = 'detail_book'),
    path('comment/<int:bookId>',views.commentCreateView.as_view(),name = 'post_comment'),
    path('review/<int:pk>/delete',views.ReviewDelete.as_view(),name='reviewDelete'),
    path('review/<int:pk>/getreplies',views.getReplies,name='reviewReply'),
    path('reply/',views.CreateReply,name='replycreate'),
    path('replies/create/', views.CreateReplyView.as_view(), name='create-reply'),
    path('add/',views.CreateBookView.as_view(),name='add_book'),
    path('review/<int:bookId>/',views.reviewCreate.as_view(),name='createreview'),
    path('<int:bookId>/update',views.UpdateBook.as_view(),name='update_book'),
    path('<int:pk>/delete',views.DeleteBook.as_view(),name='deleteBook'),
]