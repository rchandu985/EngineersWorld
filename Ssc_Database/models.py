from django.db import models

class CreateChapters(models.Model):
    Qualification=models.CharField(max_length=1000,default='Ssc')
    Subject_Name = models.CharField(max_length=1000,default='Enter The Subject Name',blank=False)
    Chapter_Name = models.CharField(max_length=1000,default='Enter The Name',blank=False)
    Medium = models.CharField(max_length=1000,default='Enter The Medium',blank=False)
    def __str__(self):
        return self.Chapter_Name
class Chapters_Database(models.Model):
    Qualification=models.CharField(max_length=1000,default='Ssc')
    Chapter=models.ManyToManyField(CreateChapters)
    Subject_Name = models.CharField(max_length=1000,default='Enter The Subject Name',blank=False)
    Medium = models.CharField(max_length=1000,default='Enter The Medium',blank=False)
    def __str__(self):
        return str(self.Chapter)
class SaveSscMaterials(models.Model):
    Subject_Name=models.CharField(max_length=1000,default='subject name',blank=False)
    Chapter_Name= models.CharField(max_length=1000,blank=False,default='chapter name')
    File=models.FileField(upload_to='SscDatabase',null=True)
    Medium= models.CharField(max_length=1000,default='Medium')
    DateTime=models.DateTimeField()