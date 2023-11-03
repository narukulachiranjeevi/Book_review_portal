from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class UserModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/profile_pics')
    bio = models.TextField(blank=True)
    favorite_genres = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Book(models.Model):
    user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    rating = models.IntegerField(
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    isbn = models.CharField(max_length=13, unique=True)
    cover_image = models.ImageField(upload_to='images/')
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Comment(models.Model):
    commentdUser = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book,related_name='comment',on_delete=models.CASCADE)

class Reply(models.Model):
    repliedUser = models.ForeignKey(User, related_name='replies', on_delete=models.CASCADE)
    reply = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment,related_name='replies',on_delete=models.CASCADE)


'''Book -> (User ,title, author, ISBN, cover image, and genre)
Comments -> (User, Comment , Book_model_instance(foreign_key))
Reply->(User ,Reply,Likes,dislikes,Comments_model_instance(foreign_key))'''