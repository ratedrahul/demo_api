from django.db import models
from django.contrib.auth.models import User, AbstractUser

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
	            ("can_access","Anytime")]

	def __str__(self):
		return 'EliteUser'


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	bio = models.TextField()
	mobile_number = models.CharField(max_length = 10)

	def __str__(self):
		return self.user.username

class Address(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name = 'user_address')
	street = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	pin_code = models.IntegerField()

	def __str__(self):
		return f"{self.user.username}'s Address"

class ReadingHistory(models.Model):
	user =  models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey('Book',on_delete= models.CASCADE)
	accessed_on = models.DateTimeField(auto_now = True)

class Book(models.Model):
	title = models.CharField(max_length = 50)	
	author = models.CharField(max_length = 50 , default = "NA")
	description = models.TextField()
	poster = models.ImageField(upload_to="book_cover/",blank=True)
	file_path = models.FileField(upload_to = 'book_collection/')
	upload_date = models.DateTimeField(auto_now_add = True)
	uploader = models.ForeignKey(EliteUser, on_delete = models.CASCADE)
	category = models.ForeignKey('Category',on_delete = models.CASCADE)

	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length = 30, default = 'ALL', unique = True)

	class Meta:
		ordering = ['name']	

	def __str__(self):
		book_count = self.book_set.count()
		return f"{self.name} has {book_count} books"


class BookAdditionalInfo(models.Model):
	book = models.OneToOneField('Book',on_delete = models.CASCADE,null = True, related_name = "book_info")
	pages = models.IntegerField()
	price = models.FloatField()
	publisher = models.CharField(max_length = 30, blank = True, null = True)

	def __str__(self):
		return f'{self.book.title} is published by {self.publisher} and price {self.price}'