from rest_framework import serializers
from .models import Reply
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ReplyDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ReplyDeserializer, self).to_representation(instance)
        rep['repliedUser'] = instance.repliedUser.username
        rep['comment']=instance.comment.comment
        return rep
