from django.shortcuts import render
from DiplomaDatabase.models import Chapters_Database,SaveDiplomaMaterials
# Create your views here.
import datetime
def SendSubjects(request):
    
    data=Chapters_Database.objects.filter(Year=request.POST['Year'],Sem=request.POST['Sem'],Regulation=request.POST['Regulation'],Branch_Name=request.POST['Branch'])

    return render(request,'diploma/diploma.html',{'data':data,'title':'Upload Diploma Materials'})
def upload_materials(request):
    if request.method=='post'or'POST':
        if request.FILES.get("file"):
            save_data=SaveDiplomaMaterials.objects.create(Regulation=request.POST['Regulation'],Subject_Name=request.POST['subject'],Chapter_Name=request.POST['chapter'],File=request.FILES['file'],Branch_Name=request.POST['branch'],DateTime=datetime.datetime.now(),Year=request.POST['year'],Sem=request.POST['sem'])
            save_data.save()

            return render(request,'diploma/diploma.html',{'success':'upload success..thanks for help to each other'.title(),'title':'Thanks For Upload Diploma Materials','action':'/SendDiplomaSubjects/'})
        else:
            return render(request,'diploma/diploma.html',{'upload_fail':'upload fail..!!please select the file...pres the back button'.title(),'title':'Error Happend..Please Check Once','action':'/SendDiplomaSubjects/'})
    else:
        return render(request,'diploma/diploma.html',{'method_fail':'method has been failed..!!please contact the admin'.title()})

def download_materials(request):

    return render(request,'diploma/diploma.html',{'action':'/SendDiplomaMaterials/','title':'Diploma Materials Download'})
def SendDiplomaMaterials(request):
    sendind_data=SaveDiplomaMaterials.objects.filter(Branch_Name=request.POST['Branch'],Year=request.POST['Year'],Sem=request.POST['Sem'],Regulation=request.POST['Regulation']).order_by('Chapter_Name')
    return render(request,'diploma/diploma.html',{'sending_data':sendind_data,'action':'/SendDiplomaMaterials/','title':'Thanks For Download Diploma Materials'})