from operator import mod
from django.contrib import admin
from Ssc_Database import models
# Register your models here.


class chapter_information(admin.ModelAdmin):
    list_display=['Qualification','Chapter_Name','Subject_Name','Medium']
admin.site.register(models.CreateChapters,chapter_information)

class display(admin.ModelAdmin):
    list_display=['Subject_Name','Medium']
admin.site.register(models.Chapters_Database,display)

class MaterialInformaton(admin.ModelAdmin):
    list_display=['Subject_Name','Chapter_Name','Medium','DateTime','File']
admin.site.register(models.SaveSscMaterials,MaterialInformaton)