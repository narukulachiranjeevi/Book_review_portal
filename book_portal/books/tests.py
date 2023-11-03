from django.test import TestCase
from .models import Book
from django.contrib.auth.models import User
from django.urls import reverse

class get_books_views(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        Book.objects.create(title='Python',user=user)
        Book.objects.create(title='Django',user=user,isbn='django')
    
    def test_get_books(self):
        url=reverse('get_books')
        response = self.client.get(url)
        books = response.context['books']  
        self.assertContains(response,'Python')
        self.assertEqual(books[0].title, 'Python')
    