from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','password','last_name', 'email']

class BookSerializer(serializers.ModelSerializer):
	category_name = serializers.ReadOnlyField(source='category.category')
	class Meta:
		model = Book
		fields = '__all__'

class PaidUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = PaidUser
		fields = ['password','username','email','subscription_start_date','subscription_end_date']

class EliteUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = EliteUser
		# fields = ['password','username','email','subscription_start_date','subscription_end_date']
		fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['username','password','student_id','university']


class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only= True)

	# def validate(self,data):
	# 	username = data.get('username')
	# 	password = data.get('password')

	# 	user = authenticate(username=username,password= password)

	# 	if not user:
	# 		raise serializers.ValidationError('Invalid Credentials')

	# 	data['user'] = user
	# 	return data

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username','email','password']
		extra_kwargs = {'password':{'write_only':True}}






class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'





