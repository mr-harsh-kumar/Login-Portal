from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log/',log),
    path('login/',login),
    path('register/',register),
    path('user-registeration/',user_registeration),
    path('home/',home),
    path('user_authentication/',user_authentication),
    path('logout/',logout),
]
