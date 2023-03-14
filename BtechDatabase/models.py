from django.db import models

# Create your models here.
class CreateChapters(models.Model):
    Qualification=models.CharField(max_length=1000,default='Btech')
    Subject_Name = models.CharField(max_length=1000,default='Enter The Subject Name',blank=False)
    Chapter_Name = models.CharField(max_length=1000,default='Enter The Name',blank=False)
    Branch_Name = models.CharField(max_length=1000,default='Enter Branch Name',blank=False)
    Year = models.CharField(max_length=1000,default='Enter The Year',blank=False)
    Sem = models.CharField(max_length=1000,default='Enter The Sem',blank=False)
    Regulation=models.CharField(max_length=100,default="Enter The Regulation",blank=False)
    def __str__(self):
        return self.Chapter_Name
class Chapters_Database(models.Model):
    Chapter=models.ManyToManyField(CreateChapters)
    Subject_Name = models.CharField(max_length=1000,default='Enter The Subject Name',blank=False)
    Branch_Name = models.CharField(max_length=1000,default='Enter Branch Name',blank=False)
    Year = models.CharField(max_length=1000,default='Enter The Year',blank=False)
    Sem = models.CharField(max_length=1000,default='Enter The Sem',blank=False)
    Regulation=models.CharField(max_length=100,default="Enter The Regulation",blank=False)
    def __str__(self):
        return str(self.Chapter)
class SaveBtechMaterials(models.Model):
    Subject_Name=models.CharField(max_length=1000,default='subject name',blank=False)
    Branch_Name = models.CharField(max_length=1000,blank=False,default='branch name')
    Chapter_Name= models.CharField(max_length=1000,blank=False,default='chapter name')
    File=models.FileField(upload_to='BtechDatabase',null=True)
    Year= models.CharField(max_length=1000,default='year')
    Sem= models.CharField(max_length=1000,default='sem')
    DateTime=models.DateTimeField()
    Regulation= models.CharField(max_length=3,default="Enter The Regulation")