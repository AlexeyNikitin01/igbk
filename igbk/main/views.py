import io

from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import KeysWordsForm
from .models import TextToCreateImg, UploadGenerateImageModel

from image_generation.main import gen_img


@login_required
def index(request):
    user = request.user
    if request.method == 'POST':
        form = KeysWordsForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, 'main/done.html', {'form': form.cleaned_data.values()})
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = KeysWordsForm()
    return render(request, template_name='main/index.html', context={'form': form})


class Index(View):
    def get(self, request, *args, **kwargs):
        kwf = KeysWordsForm()
        if request.user.is_authenticated:
            data = UploadGenerateImageModel.objects.filter(user=request.user)
            print(list(data.values())[0]['description_id'])
            que = TextToCreateImg.objects.filter(pk=list(data.values())[0]['description_id'])
            contex = {
                'que': que,
                'data': data,
                'form': kwf,
            }
        else:
            contex = {
                'form': kwf,
            }
        return render(request, 'main/index.html', contex)

    def post(self, request):
        kwf = KeysWordsForm(request.POST)
        if kwf.is_valid():
            t2c = TextToCreateImg.objects.create(
                client=self.request.user,
                gender=request.POST['gender'],
                skin_color=request.POST['skin_color'],
                age=request.POST['age'],
                hair=request.POST['hair'],
                eyes=request.POST['eyes'],
                eyebrows=request.POST['eyebrows'],
                jaw=request.POST['jaw'],
                nose=request.POST['nose'],
            )
            # image to model
            img = gen_img(list(request.POST.values()), realize=True)
            buf = io.BytesIO()
            img.save(buf, format='JPEG')
            img_model = UploadGenerateImageModel.objects.create(
                user=self.request.user,
                description=t2c,
            )
            img_model.generate_img_by_user.save("generate_img.jpg", content=ContentFile(buf.getvalue()))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        contex = {
            'kwf': kwf,
        }
        return render(request, 'main/index.html', contex)


def about(request):
    return render(request, template_name='main/about.html', context={})
