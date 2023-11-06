from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/profile_pics')
    bio = models.TextField(blank=True)
    favorite_genres = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username