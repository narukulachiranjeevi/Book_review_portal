from django.contrib import admin
from .models import Book,Comment,Reply,UserModel
# Register your models here.
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(UserModel)