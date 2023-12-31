import os
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from django.http import HttpResponse
from django.contrib.auth import get_user_model,authenticate,login,logout

from .models import *
from .pagination import CustomPagination
from .serializers import UserLoginSerializer, UserSerializer, BookSerializer, PaidUserSerializer, StudentSerializer, UserRegisterSerializer, CategorySerializer, BookInfoSerializer,AddressSerializer

from rest_framework.parsers import MultiPartParser

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class BookViewSet(viewsets.ModelViewSet):

	serializer_class = BookSerializer
	# other filters also can be used
	# filter_backends = [filters.SearchFilter,filters.OrderingFilter]
	filterset_fields = ['category', 'category__name']
	search_fields = ['title']

	#pagination
	pagination_class = CustomPagination

	#parser
	parser_classes = [MultiPartParser]

# 	# added jwt authentication
	# permission_classes = (IsAuthenticated,)

	# queryset = Book.objects.all()
	#overriding default queryset
	def get_queryset(self):
		response = Book.objects.all()
		return response

# 	To show a success message overriding default
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
		
			# serializer.save(uploader=uploader, category=category)
			serializer.save()
			return Response({'message': 'Book uploaded successfully'}, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class BookCRUDView(APIView):
	def get(self,request):
		queryset = Book.objects.all()
		serializer_class = BookSerializer(queryset,many = True)
		return Response(serializer.data,status = status.HTTP_200_OK)

# Create your views here.
def homepage(request):
	token = request.COOKIES.get('access_token')
	if request.user.is_authenticated:
		current_user = request.user.username
		return HttpResponse(f'Current logged in username : {current_user} <br>Access token is = {token}')
	return HttpResponse(f'Not Logged in User<br>Login access token = {token}')


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def create(self,request,*args,**kwargs):
		serializer = UserRegisterSerializer(data = request.data)

		if serializer.is_valid():
			user = get_user_model()(
				username=serializer.validated_data['username'],
			)
			# Encrypting plain password
			user.set_password(serializer.validated_data['password'])
			user.save()
			return Response({'message':"User registered successfully"},status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookList(APIView):
	def get(self,request):
		b = Book.objects.all()
		data= BookSerializer(b,many = True).data
		return Response(data)

class PaidUserViewSet(viewsets.ModelViewSet):
	queryset = PaidUser.objects.all()
	serializer_class = PaidUserSerializer

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class AddressViewSet(viewsets.ModelViewSet):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	filterset_fields = ['user__username','street']
	filter_backends = [filters.SearchFilter]
	search_fields = ['pin_code']

class BookInfoViewSet(viewsets.ModelViewSet):
	queryset = BookAdditionalInfo.objects.all()
	serializer_class = BookInfoSerializer
	filterset_fields = ['book__title']


class UserLoginView(TokenObtainPairView):
	def post(self,request,*args,**kwargs):
		serializer = UserLoginSerializer(data = request.data)
		if serializer.is_valid():
			username = request.data['username']
			password = request.data['password']

			user = authenticate(username = username,password = password)
			if user:
				login(request,user)
				# generating jwt token here
				refresh = RefreshToken.for_user(user)
				access_token = str(refresh.access_token)

				response = Response({
					'user_id': user.id,
					'username': user.username,
					'access_token': access_token,
					'refresh_token': str(refresh),
					'message': 'Logged in successfully',
				})

				#saving token in cookie
				response.set_cookie(key='access_token', value=access_token, httponly=True)
				return response
			else:
				return Response({'error': "User Not Found"}, status=status.HTTP_401_UNAUTHORIZED)

		else:
			return Response({'error': "not valid input"}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
	def post(self,request,*args,**kwargs):
		response = Response()
		response.delete_cookie('access_token')
		logout(request)
		response.data ={'message':'Logged out successfully'}
		return response

	