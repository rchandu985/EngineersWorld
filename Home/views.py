from turtle import title
from django.shortcuts import render,redirect
from MtechDatabase.models import Chapters_Database
# Create your views here.
def home(request):
    return render(request,'index.html')
def mtech(request):
    return render(request,'mtech/mtech.html',{'action':'/SendMtechSubjects/'})
def btech(request):
    data={'action':'/SendBtechSubjects/','title':'Select The Btech Subjects For Upload Materials'}
    return render(request,'btech/btech.html',data)
def diploma(request):
    data={'action':'/SendDiplomaSubjects/','title':'Select The Diploma Subjects For Upload Materials'}

    return render(request,'diploma/diploma.html',data)
def degree(request):
    data={'action':'/SendDegreeSubjects/','title':'Select The Degree Subjects For Upload Materials'}
    return render(request,'degree/degree.html',data)
def inter(request):
    data={'action':'/SendIntermediateSubjects/','title':'Select The Intermediate Subjects For Upload Materials'}
    return render(request,'Intermediate/Intermediate.html',data)
def iti(request):
    data={'action':'/SendItiSubjects/','title':'Select The Iti Subjects For Upload Materials'}
    return render(request,'iti/iti.html',data)
def ApSsc(request):
    data={'action':'/SendSscSubjects/','title':'Select The Ssc Subjects For Upload Materials'}
    return render(request,'Ssc/Ssc.html',data)
def home_page(request):
    return render(request,'index.html')

