from operator import mod
from django.contrib import admin
from IntermediateDatabase import models
# Register your models here.


class chapter_information(admin.ModelAdmin):
    list_display=['Qualification','Chapter_Name','Subject_Name','Branch_Name','Year','Medium']
admin.site.register(models.CreateChapters,chapter_information)

class display(admin.ModelAdmin):
    list_display=['Subject_Name','Branch_Name','Year','Medium']
admin.site.register(models.Chapters_Database,display)

class MaterialInformaton(admin.ModelAdmin):
    list_display=['Subject_Name','Branch_Name','Chapter_Name','Year','Medium','DateTime','File']
admin.site.register(models.SaveIntermediateMaterials,MaterialInformaton)