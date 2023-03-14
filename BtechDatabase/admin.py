from django.contrib import admin
from BtechDatabase import models
# Register your models here.
class display(admin.ModelAdmin):
    list_display=['Qualification','Chapter_Name','Subject_Name','Branch_Name','Year','Sem','Regulation']
admin.site.register(models.CreateChapters,display)

class display(admin.ModelAdmin):
    list_display=['Subject_Name','Branch_Name','Year','Sem','Regulation']
admin.site.register(models.Chapters_Database,display)

class display(admin.ModelAdmin):
    list_display=['Subject_Name','Branch_Name','Year','Sem','Regulation','File','DateTime']
admin.site.register(models.SaveBtechMaterials,display)
