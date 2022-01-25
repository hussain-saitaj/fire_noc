from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    name=models.CharField(max_length=50,blank=True)
    phone_no=models.CharField(max_length=10,blank=True)
    email=models.EmailField(max_length=100,blank=True)
    aadhar=models.CharField(max_length=12,blank=True)
    site_name=models.CharField(max_length=200,blank=True)
    area=models.IntegerField(blank=True,null=True)
    APPLICATION_STATUS=[
        ("rejected","Rejected"),
        ("pending","pending"),
        ("accepted","accepted")
    ]
    status=models.CharField(max_length=10,choices=APPLICATION_STATUS,default="pending",blank=True)
    payment_status=models.BooleanField(default=False,blank=True)
    form=models.FileField(upload_to="applications")
    
    # def __str__(self):
    #     return self.id


class CustomUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no=models.CharField(max_length=10,blank=True)
    address=models.TextField(blank=True)
    aadhar=models.CharField(max_length=12,blank=True)
    application=models.ManyToManyField(Application,null=True)

    # def __str__(self):
    #     return self.user.id or " "



