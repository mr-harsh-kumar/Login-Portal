from django.db import models

# Create your models here.

class My_Users(models.Model):
    
    id = models.AutoField(primary_key=True)
    email=models.CharField(max_length=100,default='no-email')
    username=models.CharField(max_length=100,default='no-username')
    password=models.CharField(max_length=100,default='no-password')
    
    
    def __str__(self):
        return self.username