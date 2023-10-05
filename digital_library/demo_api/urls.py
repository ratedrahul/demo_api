from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet,BookList,BookViewSet,PaidUserViewSet, StudentViewSet, CategoryViewSet, UserRegisterView,UserLoginView,UserLogoutView
from . import views

#jwt links
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

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
    path('book-list',BookList.as_view(), name = "book"),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('signup/', UserRegisterView.as_view(), name='user-register'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path("gettoken/",TokenObtainPairView.as_view(),name = 'token_obtain'),
    path('refreshtoken/',TokenRefreshView.as_view(),name = 'token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]