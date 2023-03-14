from django.urls import path
from Job_Database import views
urlpatterns = [
    path('Register_As_Company/',views.Register_As_The_Company),
    path('Login/',views.Login),
    path('forgot_password/',views.Reset_The_Password),
    path('post_the_job/',views.create_the_job_alert),
    path('Logout/',views.user_logout),
    path('engineers_home/',views.crud_home),
    path('view_posted_jobs/',views.view_posted_jobs),
    path('update_created_jobs/<int:id>',views.update_created_jobs),
    path('delete_created_job/<int:id>',views.delete_created_jobs),
    
]
