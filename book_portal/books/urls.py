from django.urls import path
from . import views

urlpatterns = [
    path('',views.books_listview.as_view(),name='get_books'),
    path('<int:pk>/',views.book_detailview.as_view(),name = 'detail_book'),
    path('comment/<int:bookId>',views.commentCreateView.as_view(),name = 'post_comment'),
    path('comment/<int:pk>/delete',views.commentDeleteView.as_view(),name='commentDelete'),
    path('comment/<int:pk>/getreplies',views.getReplies,name='commentReply'),
    path('reply/',views.CreateReply,name='replycreate'),
    path('replies/create/', views.CreateReplyView.as_view(), name='create-reply'),
]