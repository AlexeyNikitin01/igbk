from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

from django.views import View
from django.views.generic import TemplateView

from django.shortcuts import render, redirect


from .forms import UserSignUpForm, UserSignInForm


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
    context = {
        'user': user
    }
    return render(request, template_name='users/profile.html', context=context)
