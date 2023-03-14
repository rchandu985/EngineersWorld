from django import forms
from Job_Database.models  import Login
from django.contrib.auth.models import User
from Job_Database.models import post_the_job

class Login_As_Company(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
        widgets={'password':forms.PasswordInput()}
class Register_As_Company_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput()}
class password_reset_form(forms.Form):
    Enter_Your_Username=forms.CharField()
    Set_New_Password=forms.CharField(widget=forms.PasswordInput())
    Confirm_Password=forms.CharField(widget=forms.PasswordInput())
class post_the_job_form(forms.ModelForm):
    class Meta:
        model=post_the_job
        fields=['company_name','company_email','designation','required_skills','required_experience']
        