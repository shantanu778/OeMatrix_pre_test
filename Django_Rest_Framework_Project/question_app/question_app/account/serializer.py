from rest_framework import serializers

from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    password2 = serializers.CharField()
    class Meta:
        model = User
        fields = ['email','username','password','password2']
        extra_kewargs = {
            'password': {'write_only': True}
        }

    # def validate_password(self, value):
    #     data = self.get_initial()
    #     password = data.get('password')
    #     password2 = value
    #     if password != password2:
    #         raise ValidationError('Password must match')
    #     return value

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )    
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':"'password don't match'"})

        user.set_password(password)
        user.save()
        return user

    


class UserGetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email','username')


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)