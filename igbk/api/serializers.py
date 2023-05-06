from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User, Group

from main.models import TextToCreateImg
from main.models import UploadGenerateImageModel


class TextToCreateImgSerializer(ModelSerializer):
    class Meta:
        model = TextToCreateImg
        fields = '__all__'


class UploadGenerateImageSerializer(ModelSerializer):
    class Meta:
        model = UploadGenerateImageModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
