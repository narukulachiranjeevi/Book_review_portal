from rest_framework import serializers
from .models import Reply,ReviewReply
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ReplyDeserializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewReply
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ReplyDeserializer, self).to_representation(instance)
        rep['reviewreply'] = instance.repliedUser.username
        rep['review']=instance.review.review
        return rep
