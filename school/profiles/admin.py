from django.contrib import admin

from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display=('id','stu_name','stu_code')

admin.site.register(Profile,ProfileAdmin)