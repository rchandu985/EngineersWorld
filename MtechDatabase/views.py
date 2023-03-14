from django.shortcuts import render,redirect
from MtechDatabase.models import Chapters_Database,SaveMtechMaterials
# Create your views here.
import datetime

#sending the subject and chapters for uploading the materials
def send_subjects(request):
    data=Chapters_Database.objects.filter(Year=request.POST['Year'],Sem=request.POST['Sem'],Branch_Name=request.POST['Branch'])
    return render(request,'mtech/mtech.html',{'data':data,'action':'/SendMtechSubjects/'})

#uploading the materials
def upload_materials(request):
    if request.method=='post'or'POST':
        if request.FILES.get("file"):
            save_data=SaveMtechMaterials.objects.create(Subject_Name=request.POST['subject'],Chapter_Name=request.POST['chapter'],File=request.FILES['file'],Branch_Name=request.POST['branch'],DateTime=datetime.datetime.now(),Year=request.POST['year'],Sem=request.POST['sem'])
            save_data.save()

            return render(request,'mtech/mtech.html',{'action':'/SendMtechSubjects/','success':'upload success..thanks for help to eeachc other'.title()})
        else:
            return render(request,'mtech/mtech.html',{'upload_fail':'upload fail..!!please select the file...pres the back button'.title(),'action':'/SendMtechSubjects/'})
    else:
        return render(request,'mtech/mtech.html',{'method_fail':'method has been failed..!!please contact the admin'.title()})

#downloading the materials
def download_materials(request):
    return render(request,'mtech/mtech.html',{'action':'/SendMtechRequiredMaterial/'})
def SendRequiredMaterial(request):
    sending_data=SaveMtechMaterials.objects.filter(Year=request.POST['Year'],Sem=request.POST['Sem'],Branch_Name=request.POST['Branch']).order_by('Chapter_Name')

    return render(request,'mtech/mtech.html',{'sending_data':sending_data,'action':'/SendMtechRequiredMaterial/'})