from django.urls import path
from BtechDatabase import views
urlpatterns=[
    path('SendBtechSubjects/',views.SendSubjects),
    path('BtechMaterialsUpload/',views.upload_materials),
    path('DownloadBtechMaterials/',views.download_materials),
    path('SendBtechMaterials/',views.SendBtechMaterials),
]