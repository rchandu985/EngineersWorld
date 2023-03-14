from django.urls import path
from DegreeDatabase import views
urlpatterns=[
    path('SendDegreeSubjects/',views.send_subjects),
    path('DegreeMaterialsUpload/',views.upload_materials),
    path('DownloadDegreeMaterials/',views.download_materials),
    path('SendDegreeRequiredMaterial/',views.SendRequiredMaterial),
]