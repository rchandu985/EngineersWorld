from django.urls import path
from MtechDatabase import views
urlpatterns=[
    path('SendMtechSubjects/',views.send_subjects),
    path('MtechMaterialsUpload/',views.upload_materials),
    path('MtechMaterialsDownload/',views.download_materials),
    path('SendMtechRequiredMaterial/',views.SendRequiredMaterial),
]