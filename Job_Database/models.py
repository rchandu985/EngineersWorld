from django.db import models
# Create your models here.
class Login(models.Model):
    username= models.CharField(max_length=1000,default='enter the username'.title(),blank=False)
    password= models.CharField(max_length=1000,default='enter the password'.title(),null=False,blank=False)
class post_the_job(models.Model):
    company_name= models.CharField(max_length=1000,default=None,blank=False,null=False)
    company_email= models.CharField(max_length=1000,default=None,blank=False,null=False)
    designation= models.CharField(max_length=1000,default=None,blank=False,null=False)
    required_skills= models.CharField(max_length=1000,default=None,blank=False,null=False)
    required_experience= models.CharField(max_length=1000,default=None,blank=False,null=False)
    username= models.CharField(max_length=1000,default=None,blank=False,null=False)