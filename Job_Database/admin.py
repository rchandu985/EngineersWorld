from Job_Database.models import post_the_job
from django.contrib import admin
class display(admin.ModelAdmin):
    list_display=['company_name', 'company_email']
admin.site.register(post_the_job,display)