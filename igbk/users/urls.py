from django.urls import path

from .views import SignUpDone
from .views import UserSignUpView
from .views import UserSignInView
from .views import LogOut
from .views import profile
from .views import ProfileSettingsViews

app_name = 'users'

urlpatterns = [
    path('SignUpDone/', SignUpDone.as_view(), name='SignUpDone'),
    path('SignUp/', UserSignUpView.as_view(), name='SignUp'),
    path('login/', UserSignInView.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/settings/', ProfileSettingsViews.as_view(), name='profile_settings'),
]
