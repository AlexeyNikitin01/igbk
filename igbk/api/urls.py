from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CreateTextViewSet, CreateImgViewSet

router = DefaultRouter()
router.register(r'tasks/gen_img', CreateImgViewSet)
router.register(r'tasks', CreateTextViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
