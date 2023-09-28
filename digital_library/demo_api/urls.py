from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet,BookList,BookViewSet,PaidUserViewSet, StudentViewSet, CategoryViewSet
from . import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'book', BookViewSet)
router.register(r'paiduser',PaidUserViewSet)
router.register(r'student',StudentViewSet)
router.register(r'category',CategoryViewSet)

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('book-list',BookList.as_view(), name = "book")
]