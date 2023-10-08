from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User,UserAdmin)
admin.site.register(Student)
admin.site.register(PaidUser)
admin.site.register(EliteUser)
admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(BookAdditionalInfo)
admin.site.register(Address)


