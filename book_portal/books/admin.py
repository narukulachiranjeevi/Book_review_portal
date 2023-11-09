from django.contrib import admin
from .models import Book,Comment,Reply,Review,ReviewReply
# Register your models here.
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Review)
admin.site.register(ReviewReply)
##admin.site.register(UserModel)