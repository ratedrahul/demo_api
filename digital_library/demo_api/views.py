from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import UserSerializer, BookSerializer, PaidUserSerializer, StudentSerializer, UserLoginSerializer, CategorySerializer
# from django.contrib.auth.models import Group, Permission


# Create your views here.
def homepage(request):
	return HttpResponse("This is Homepage")


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	

class BookList(APIView):
	def get(self,request):
		b = Book.objects.all()
		data= BookSerializer(b,many = True).data
		return Response(data)


class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class PaidUserViewSet(viewsets.ModelViewSet):
	queryset = PaidUser.objects.all()
	serializer_class = PaidUserSerializer

class StudentViewSet(viewsets.ModelViewSet):

	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	# def get_queryset(self):
	# 	queryset = Student.objects.all()
    #     # return self.request.user.accounts.all()
	# 	return queryset
# class UserLoginViewSet(viewsets.ModelViewSet):


class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer