from django.db import models
# Create your models here.


'''class Person(models.Model):
    user_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    full_name = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pic')'''

class Profile_Picture(models.Model):
    image = models.ImageField(upload_to='pic')
    file_name = models.CharField(max_length=100)

class Comments(models.Model):
    text = models.CharField(max_length=2000)
    posted_by = models.CharField(max_length=200)
    time_posted = models.TimeField()