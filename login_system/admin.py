from django.contrib import admin
from .models import My_Users

# Register your models here.


class show_my_users(admin.ModelAdmin):
    list_display = [  'id','email','username', 'password' ]

admin.site.register(My_Users, show_my_users)