from django.urls import path
from Ssc_Database import views
urlpatterns=[
    path('SendSscSubjects/',views.send_subjects),
    path('SscMaterialsUpload/',views.upload_materials),
    path('DownloadSscMaterials/',views.download_materials),
    path('SendSscRequiredMaterial/',views.SendRequiredMaterial),
]