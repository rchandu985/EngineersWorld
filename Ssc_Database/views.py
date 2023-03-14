from django.shortcuts import render,redirect
from Ssc_Database.models import Chapters_Database,SaveSscMaterials
# Create your views here.
import datetime

#sending the subject and chapters for uploading the materials
def send_subjects(request):
    data=Chapters_Database.objects.filter(Medium=request.POST['Medium'],Subject_Name=request.POST['Subject'])
    return render(request,'Ssc/Ssc.html',{'data':data,'action':'/SendSscSubjects/'})

#uploading the materials
def upload_materials(request):
    if request.method=='post'or'POST':
        if request.FILES.get("file"):
            save_data=SaveSscMaterials.objects.create(Chapter_Name=request.POST['chapter'],File=request.FILES['file'],Subject_Name=request.POST['subject'],DateTime=datetime.datetime.now(),Medium=request.POST['Medium'])
            save_data.save()

            return render(request,'Ssc/Ssc.html',{'action':'/SendSscSubjects/','success':'upload success..thanks for help to eeachc other'.title()})
        else:
            return render(request,'Ssc/Ssc.html',{'upload_fail':'upload fail..!!please select the file...pres the back button'.title(),'action':'/SendSscSubjects/'})
    else:
        return render(request,'Ssc/Ssc.html',{'method_fail':'method has been failed..!!please contact the admin'.title()})

#downloading the materials
def download_materials(request):
    return render(request,'Ssc/Ssc.html',{'action':'/SendSscRequiredMaterial/'})
def SendRequiredMaterial(request):
    sending_data=SaveSscMaterials.objects.filter(Medium=request.POST['Medium'],Subject_Name=request.POST['Subject']).order_by('Chapter_Name')

    return render(request,'Ssc/Ssc.html',{'sending_data':sending_data,'action':'/SendSscRequiredMaterial/'})