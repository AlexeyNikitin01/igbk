from rest_framework.serializers import ModelSerializer

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
