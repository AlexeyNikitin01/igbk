from django.urls import path, include

from .views import about, ajax

app_name = 'main'

urlpatterns = [
    path('about/', about, name='about'),
    path('', ajax, name='index')
]
