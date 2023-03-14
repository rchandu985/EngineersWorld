from django.urls import path
from IntermediateDatabase import views
urlpatterns=[
    path('SendIntermediateSubjects/',views.send_subjects),
    path('IntermediateMaterialsUpload/',views.upload_materials),
    path('DownloadIntermediateMaterials/',views.download_materials),
    path('SendIntermediateRequiredMaterial/',views.SendRequiredMaterial),
]