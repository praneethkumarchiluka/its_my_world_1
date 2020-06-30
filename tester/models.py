from django.db import models
from django.contrib.auth.models import User

class Details(models.Model):
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    Img = models.ImageField(upload_to='pics/')
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    
class profile1(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField()
    Img = models.ImageField(upload_to='pics/')
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    
class blog(models.Model):
    Img = models.ImageField(upload_to='pics/')
    title= models.CharField(max_length=100) 
    content= models.CharField(max_length=100) 
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    