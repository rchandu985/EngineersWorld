from operator import mod
from django.contrib import admin
from ITI_Database import models
# Register your models here.


class chapter_information(admin.ModelAdmin):
    list_display=['Qualification','Chapter_Name','Subject_Name','Branch_Name','Year','Sem']
admin.site.register(models.CreateChapters,chapter_information)

class display(admin.ModelAdmin):
    list_display=['Subject_Name','Branch_Name','Year','Sem']
admin.site.register(models.Chapters_Database,display)

class MaterialInformaton(admin.ModelAdmin):
    list_display=['Subject_Name','Branch_Name','Chapter_Name','Year','Sem','DateTime','File']
admin.site.register(models.SaveItiMaterials,MaterialInformaton)