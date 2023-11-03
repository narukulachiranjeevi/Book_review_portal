from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_books_list_view.as_view(),name='get_books')
]