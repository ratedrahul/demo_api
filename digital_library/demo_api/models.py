from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Guest(models.Model):
	guest_name = models.CharField(max_length = 50, default = "Guest")

class User(AbstractUser):
	pass

class Student(User):
	student_id = models.PositiveIntegerField()
	university = models.CharField(max_length = 30)

	class Meta:
		verbose_name = "Student"

class PaidUser(User):
	subscription_start_date = models.DateTimeField()
	subscription_end_date = models.DateTimeField()

	class Meta:
		verbose_name = "Paid User"

	def __str__(self):
		return 'PaidUser'

class EliteUser(User):
	company_name = models.CharField(max_length=50)
	company_description = models.TextField()
	contact_info = models.TextField()


	class Meta:
		verbose_name = "Elite User"
		permissions = [
	            ("can_upload", "Can upload books"),
	            ("can_access","Anytime")
	        ]

	def __str__(self):
		return 'EliteUser'


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	bio = models.TextField()
	mobile_number = models.CharField(max_length = 10)
	reading_history = models.ManyToManyField('Book',blank = True)

	def __str__(self):
		return self.user.username


class Book(models.Model):
	book_title = models.CharField(max_length = 50)	
	author = models.CharField(max_length = 50 , default = "NA")
	description = models.TextField()
	poster = models.ImageField(upload_to="book_cover/",blank=True)
	file_path = models.FileField()
	upload_date = models.DateTimeField(auto_now_add = True)
	uploader = models.ForeignKey(EliteUser, on_delete = models.CASCADE)
	category = models.ForeignKey('Category',on_delete = models.CASCADE)

	def __str__(self):
		return self.book_title

class Category(models.Model):
	category = models.CharField(max_length = 30, default = 'ALL')

	class Meta:
		ordering = ['category']	

	def __str__(self):
		return f"{self.category}"
