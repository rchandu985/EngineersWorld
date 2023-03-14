from django.shortcuts import render
from BtechDatabase.models import Chapters_Database,SaveBtechMaterials
# Create your views here.
import datetime
def SendSubjects(request):
    
    data=Chapters_Database.objects.filter(Year=request.POST['Year'],Sem=request.POST['Sem'],Regulation=request.POST['Regulation'],Branch_Name=request.POST['Branch'])

    return render(request,'btech/btech.html',{'data':data,'title':'Upload Btech Materials'})
def upload_materials(request):
    if request.method=='post'or'POST':
        if request.FILES.get("file"):
            save_data=SaveBtechMaterials.objects.create(Regulation=request.POST['Regulation'],Subject_Name=request.POST['subject'],Chapter_Name=request.POST['chapter'],File=request.FILES['file'],Branch_Name=request.POST['branch'],DateTime=datetime.datetime.now(),Year=request.POST['year'],Sem=request.POST['sem'])
            save_data.save()

            return render(request,'btech/btech.html',{'success':'upload success..thanks for help to each other'.title(),'title':'Thanks For Upload Btech Materials','action':'/SendBtechSubjects/'})
        else:
            return render(request,'btech/btech.html',{'upload_fail':'upload fail..!!please select the file...pres the back button'.title(),'title':'Error Happend..Please Check Once','action':'/SendBtechSubjects/'})
    else:
        return render(request,'btech/btech.html',{'method_fail':'method has been failed..!!please contact the admin'.title()})

def download_materials(request):

    return render(request,'btech/btech.html',{'action':'/SendBtechMaterials/','title':'Btech Materials Download'})
def SendBtechMaterials(request):
    sendind_data=SaveBtechMaterials.objects.filter(Branch_Name=request.POST['Branch'],Year=request.POST['Year'],Sem=request.POST['Sem'],Regulation=request.POST['Regulation']).order_by('Chapter_Name')
    return render(request,'btech/btech.html',{'sending_data':sendind_data,'action':'/SendBtechMaterials/','title':'Thanks For Download Btech Materials'})