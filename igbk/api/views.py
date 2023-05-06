import io
import time

from django.core.files.base import ContentFile
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from image_generation.main import gen_img

from main.models import TextToCreateImg
from main.models import UploadGenerateImageModel

from main.forms import KeysWordsForm


from .serializers import TextToCreateImgSerializer
from .serializers import UploadGenerateImageSerializer


class TextToCreateImgViewSet(ModelViewSet):
    queryset = TextToCreateImg.objects.all()
    serializer_class = TextToCreateImgSerializer


class CreateTextViewSet(ModelViewSet):
    queryset = TextToCreateImg.objects.all()
    serializer_class = TextToCreateImgSerializer

    def create(self, request):
        form = KeysWordsForm(request.POST)
        if not form.is_valid():
            return Response({'errors': form.errors}, status=400)
        t2c = TextToCreateImg.objects.create(
                client=request.user,
                gender=request.POST['gender'],
                skin_color=request.POST['skin_color'],
                age=request.POST['age'],
                hair=request.POST['hair'],
                eyes=request.POST['eyes'],
                eyebrows=request.POST['eyebrows'],
                jaw=request.POST['jaw'],
                nose=request.POST['nose'],
            )
        t2c.save()
        # image to model
        time.sleep(10)
        img = gen_img(list(request.POST.values()), realize=True)
        buf = io.BytesIO()
        img.save(buf, format='JPEG')
        img_model = UploadGenerateImageModel.objects.create(
            user=self.request.user,
            description=t2c,
        )
        img_model.generate_img_by_user.save("generate_img.jpg", content=ContentFile(buf.getvalue()))
        img_model.save()
        return Response({'repair_order_id': t2c.id})

    def list(self, request, *args, **kwargs):
        solutions = TextToCreateImgSerializer(TextToCreateImg.objects.all(), many=True)
        return Response(solutions.data)


class CreateImgViewSet(ModelViewSet):
    queryset = UploadGenerateImageModel.objects.all()
    serializer_class = UploadGenerateImageSerializer

    def list(self, request, *args, **kwargs):
        solutions = UploadGenerateImageSerializer(UploadGenerateImageModel.objects.all(), many=True)
        return Response(solutions.data)
