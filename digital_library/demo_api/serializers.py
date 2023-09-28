from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'

class PaidUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = PaidUser
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['username','password','student_id','university']

class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self,data):
		username = data.get('username')
		password = data.get('password')

		user = authenticate(username=username,password= password)

		if not user:
			raise serializers.ValidationError('Invalid Credentials')

		data['user'] = user
		return data

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'



