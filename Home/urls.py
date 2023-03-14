from django.urls import path

from Home import views
urlpatterns=[
    path('',views.home),
    path('mtech/',views.mtech),
    path('btech/',views.btech),
    path('diploma/',views.diploma),
    path('degree/',views.degree),
    path('inter/',views.inter),
    path('iti/',views.iti),
    path('ssc/',views.ApSsc),
    path('home/',views.home),
]