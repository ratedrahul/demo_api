from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet,BookList,BookViewSet,PaidUserViewSet, StudentViewSet, CategoryViewSet,UserLoginView,UserLogoutView, BookInfoViewSet, AddressViewSet

#swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Digital Library API World",
      default_version="v1",
      description="Your API description",
      terms_of_service="https://example.com/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
)


#jwt links
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'paiduser',PaidUserViewSet)
router.register(r'student',StudentViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'book',BookViewSet, basename = 'book')
router.register(r'book_info',BookInfoViewSet)
router.register(r'user-address',AddressViewSet)

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('api/', include(router.urls)),
    path('book-list/',BookList.as_view(), name = "book"),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path("gettoken/",TokenObtainPairView.as_view(),name = 'token_obtain'),
    path('refreshtoken/',TokenRefreshView.as_view(),name = 'token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)