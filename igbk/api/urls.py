from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CreateTextViewSet, CreateImgViewSet, UserViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'tasks/gen_img', CreateImgViewSet)
router.register(r'tasks', CreateTextViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
