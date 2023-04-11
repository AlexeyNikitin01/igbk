from django.urls import path, include

from .views import index, about, Index

app_name = 'main'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', about, name='about')
]
