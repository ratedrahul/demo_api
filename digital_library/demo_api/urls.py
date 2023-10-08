from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet,BookList,BookViewSet,PaidUserViewSet, StudentViewSet, CategoryViewSet,UserLoginView,UserLogoutView, HorrorBookViewSet, TechBookViewSet, EducationBookViewSet, CodingBookViewSet
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
router.register(r'horror-books',HorrorBookViewSet)
router.register(r'coding-books',CodingBookViewSet)
router.register(r'education-books',EducationBookViewSet)
router.register(r'tech-books',TechBookViewSet)


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('book-list/',BookList.as_view(), name = "book"),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path("gettoken/",TokenObtainPairView.as_view(),name = 'token_obtain'),
    path('refreshtoken/',TokenRefreshView.as_view(),name = 'token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)