from django.urls import path
from ITI_Database import views
urlpatterns=[
    path('SendItiSubjects/',views.send_subjects),
    path('ItiMaterialsUpload/',views.upload_materials),
    path('DownloadItiMaterials/',views.download_materials),
    path('SendItiRequiredMaterial/',views.SendRequiredMaterial),
]