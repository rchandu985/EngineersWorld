from django.shortcuts import render,redirect
from DegreeDatabase.models import Chapters_Database,SaveDegreeMaterials
# Create your views here.
import datetime

#sending the subject and chapters for uploading the materials
def send_subjects(request):
    data=Chapters_Database.objects.filter(Year=request.POST['Year'],Sem=request.POST['Sem'],Branch_Name=request.POST['Branch'])
    return render(request,'degree/degree.html',{'data':data,'action':'/SendDegreeSubjects/'})

#uploading the materials
def upload_materials(request):
    if request.method=='post'or'POST':
        if request.FILES.get("file"):
            save_data=SaveDegreeMaterials.objects.create(Subject_Name=request.POST['subject'],Chapter_Name=request.POST['chapter'],File=request.FILES['file'],Branch_Name=request.POST['branch'],DateTime=datetime.datetime.now(),Year=request.POST['year'],Sem=request.POST['sem'])
            save_data.save()

            return render(request,'degree/degree.html',{'action':'/SendDegreeSubjects/','success':'upload success..thanks for help to eeachc other'.title()})
        else:
            return render(request,'degree/degree.html',{'upload_fail':'upload fail..!!please select the file...pres the back button'.title(),'action':'/SendDegreeSubjects/'})
    else:
        return render(request,'degree/degree.html',{'method_fail':'method has been failed..!!please contact the admin'.title()})

#downloading the materials
def download_materials(request):
    return render(request,'degree/degree.html',{'action':'/SendDegreeRequiredMaterial/'})
def SendRequiredMaterial(request):
    sending_data=SaveDegreeMaterials.objects.filter(Year=request.POST['Year'],Sem=request.POST['Sem'],Branch_Name=request.POST['Branch']).order_by('Chapter_Name')

    return render(request,'degree/degree.html',{'sending_data':sending_data,'action':'/SendDegreeRequiredMaterial/'})