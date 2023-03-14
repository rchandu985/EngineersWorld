from django.shortcuts import render,redirect
from IntermediateDatabase.models import Chapters_Database,SaveIntermediateMaterials
# Create your views here.
import datetime

#sending the subject and chapters for uploading the materials
def send_subjects(request):
    data=Chapters_Database.objects.filter(Year=request.POST['Year'],Medium=request.POST['Medium'],Branch_Name=request.POST['Branch'])
    return render(request,'Intermediate/Intermediate.html',{'data':data,'action':'/SendIntermediateSubjects/'})

#uploading the materials
def upload_materials(request):
    if request.method=='post'or'POST':
        if request.FILES.get("file"):
            save_data=SaveIntermediateMaterials.objects.create(Subject_Name=request.POST['subject'],Chapter_Name=request.POST['chapter'],File=request.FILES['file'],Branch_Name=request.POST['branch'],DateTime=datetime.datetime.now(),Year=request.POST['year'],Medium=request.POST['medium'])
            save_data.save()

            return render(request,'Intermediate/Intermediate.html',{'action':'/SendIntermediateSubjects/','success':'upload success..thanks for help to eeachc other'.title()})
        else:
            return render(request,'Intermediate/Intermediate.html',{'upload_fail':'upload fail..!!please select the file...pres the back button'.title(),'action':'/SendIntermediateSubjects/'})
    else:
        return render(request,'Intermediate/Intermediate.html',{'method_fail':'method has been failed..!!please contact the admin'.title()})

#downloading the materials
def download_materials(request):
    return render(request,'Intermediate/Intermediate.html',{'action':'/SendIntermediateRequiredMaterial/'})
def SendRequiredMaterial(request):
    sending_data=SaveIntermediateMaterials.objects.filter(Year=request.POST['Year'],Medium=request.POST['Medium'],Branch_Name=request.POST['Branch']).order_by('Chapter_Name')

    return render(request,'Intermediate/Intermediate.html',{'sending_data':sending_data,'action':'/SendIntermediateRequiredMaterial/'})