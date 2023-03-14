from django.urls import path
from DiplomaDatabase import views
urlpatterns=[
    path('SendDiplomaSubjects/',views.SendSubjects),
    path('DiplomaMaterialsUpload/',views.upload_materials),
    path('DownloadDiplomaMaterials/',views.download_materials),
    path('SendDiplomaMaterials/',views.SendDiplomaMaterials),
]