from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import KeysWordsForm
from .models import TextToCreateImg

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
        que = TextToCreateImg.objects.filter(client=request.user)
        kwf = KeysWordsForm()
        contex = {
            'que': que,
            'form': kwf,
        }
        return render(request, 'main/index.html', contex)

    def post(self, request):
        kwf = KeysWordsForm(request.POST)
        if kwf.is_valid():
            kw = []
            for k, v in request.POST.items():
                kw.append(f'{k} {v}')
            u = gen_img(kw)
            t2img = TextToCreateImg.objects.create(
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
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        contex = {
            'kwf': kwf,
        }
        return render(request, 'main/index.html', contex)


def about(request):
    return render(request, template_name='main/about.html', context={})
