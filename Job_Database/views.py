from django.shortcuts import render,redirect
from django.http import HttpResponse
from Job_Database.forms import post_the_job_form,Register_As_Company_Form,Login_As_Company,password_reset_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages 
from Job_Database.models import post_the_job
from django.contrib.auth.decorators import login_required,permission_required

def Register_As_The_Company(request):
    RAC=Register_As_Company_Form
    
    validate_username=[]
    validate_email=[]
    for user in User.objects.all():
        validate_username.append(user.username)
        validate_email.append(user.email)
    if request.method=='POST':
        if request.POST.get('username')not in validate_username and request.POST.get('email') not in validate_email:
            form=Register_As_Company_Form(request.POST)
            if form.is_valid():
                create_account=User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
                create_account.save()
                messages.info(request,"Succesfully Registered")
        else:
            messages.info(request,"Entered Username or Enter Email Id Is All Ready Exists..Please Try Another Value")
    return render(request,'Job_Database/register_as_company.html',{'company_registration_form':RAC})

def Login(request):
    if request.user.is_authenticated :
        return redirect('/Logout/')
    else:
        form=Login_As_Company
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                
                login(request,user)
                #messages.info(request,'succes')
                return redirect('/engineers_home/')
            else:
                messages.info(request,'Check Username Or Password')
        return render(request,'Job_Database/login.html',{'login_form':Login_As_Company})
def user_logout(request):
    logout(request)
    return redirect('/Login')

def Reset_The_Password(request):
    prf=password_reset_form
    if request.method=="POST":
        username=request.POST.get('Enter_Your_Username')
        set_new_password=request.POST.get('Set_New_Password')
        confirm_password=request.POST.get('Confirm_Password')
        validate_username=[]
        for user in User.objects.all():
            validate_username.append(user.username)
        if username in validate_username:
            if set_new_password==confirm_password:
                get_username=User.objects.get(username=username)
                reset_password=get_username.set_password(set_new_password)
                get_username.save()
                messages.info(request,'succesfully updated new password'.title())
            else:
                messages.info(request,'new password and confirm password not matched'.title())
        else:
            messages.info(request,'username not found'.title())
    return render(request,'Job_Database/update_user_details.html',{'password_reset_form':prf})


@login_required(login_url='/Login/')
def create_the_job_alert(request):
    job_creation_form=post_the_job_form
    if request.method == 'POST':

            save_data=post_the_job.objects.create(company_name=request.POST.get('company_name'),company_email=request.POST.get('company_email'),required_skills=request.POST.get('required_skills'),designation=request.POST.get('designation'),required_experience=request.POST.get('required_experience'),username=request.user.username)
        
            save_data.save()
            messages.info(request,'succesfully posted the job'.title())
            return redirect('/post_the_job/')
    sync_data={'sync_data':'2','job_creation_form':job_creation_form}
    return render(request,'Job_Database/job_operations.html',sync_data)
@login_required(login_url='/Login/')
def crud_home(request):
    
    sync_data={'sync_data':'0'}
    return render(request,'Job_Database/job_operations.html',sync_data)
@login_required(login_url='/Login/')
def view_posted_jobs(request):
    get_data=User.objects.get(username=request.user.username)
    send_data=post_the_job.objects.filter(username=get_data.username)
    sync_data={'sync_data':'1','posted_jobs':send_data}
    return render(request,'Job_Database/job_operations.html',sync_data)
@login_required(login_url='/Login/')
def update_created_jobs(request,id):
    get_update_data=post_the_job.objects.get(id=id)
    get_form=post_the_job_form(instance=get_update_data)
    if request.method=="POST":
        get_update_data.company_name=request.POST.get('company_name')
        get_update_data.company_email=request.POST.get('company_email')
        get_update_data.required_skills=request.POST.get('required_skills')
        get_update_data.designation=request.POST.get('designation')
        get_update_data.required_experience=request.POST.get('required_experience')
        get_update_data.save()
        messages.info(request,'succesfully updated the data'.title())
        return redirect('/view_posted_jobs/')
    sync_data={'sync_data':'3','update_form':get_form}
    return render(request,'Job_Database/job_operations.html',sync_data)
@login_required(login_url='/Login/')
def delete_created_jobs(request,id):
    get_delete_data=post_the_job.objects.get(id=id)
    get_delete_data.delete()
    messages.info(request,'succesfully deleted the data'.title())
    return redirect('/view_posted_jobs/')
    
