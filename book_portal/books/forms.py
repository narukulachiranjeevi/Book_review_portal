from django import forms
from .models import Comment,Reply,Book,Review

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
    
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply']

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','isbn','genre','cover_image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=['review','rating']

