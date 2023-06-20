from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.views import View
from django.views.generic import TemplateView

from django.shortcuts import render, redirect

from .models import ProfileUser
from .forms import UserSignUpForm, UserSignInForm, ProfileUserForm

from main.models import UploadGenerateImageModel
from main.models import TextToCreateImg


class UserSignUpView(View):
    def get(self, request, *args, **kwargs):
        form = UserSignUpForm()
        context = {
            'form': form,
        }
        return render(request, 'users/SignUp.html', context=context)

    def post(self, request, *args, **kwargs):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {
            'form': form,
        }
        return render(request, 'users/SignUp.html', context=context)


class UserSignInView(View):
    def get(self, request, *args, **kwargs):
        form = UserSignInForm()
        context = {
            'form': form,
        }
        return render(request, 'users/login.html', context)

    def post(self, request, *args, **kwargs):
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {
            'form': form,
        }
        return render(request, 'users/login.html', context)


class LogOut(LogoutView):
    template_name = 'users/LogOut.html'


class SignUpDone(TemplateView):
    template_name = 'users/SignUpDone.html'


@login_required
def profile(request):
    user = request.user
    pu = ProfileUser.objects.filter(user=user)
    data = UploadGenerateImageModel.objects.filter(user=user)
    context = {
        'pu': pu,
        'data': data,
        'user': user,
    }
    return render(request, template_name='users/profile.html', context=context)


class ProfileSettingsViews(View):
    def get(self, request, *args, **kwargs):
        puf = ProfileUserForm()
        user = request.user
        if request.user.is_authenticated:
            contex = {
                'prof_set': puf,
            }
        else:
            return render(request, 'users/profile_settings.html')
        return render(request, 'users/profile_settings.html', contex)

    def post(self, request):
        puf = ProfileUserForm(request.POST, request.FILES)
        print(request.FILES.items)
        if puf.is_valid():
            if ProfileUser.objects.filter(user=request.user):
                pu = ProfileUser.objects.get(user=request.user)
                pu.phone = request.POST['phone']
                pu.country = request.POST['country']
                pu.city = request.POST['city']
                pu.bio = request.POST['bio']
                pu.ava = request.FILES['ava']
                pu.save()
            else:
                ProfileUser.objects.create(
                    user=request.user,
                    phone=request.POST['phone'],
                    country=request.POST['country'],
                    city=request.POST['city'],
                    ava=request.FILES['ava'],
                    bio=request.POST['bio'],
                )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        contex = {
            'prof_set': puf,
        }
        return render(request=request, template_name='users/profile_settings.html', context=contex)
