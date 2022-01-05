from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    
    path('login',views.login,name='login'),
    path('register',views.register,name="register"),
    path('general',views.general,name="general"),
    path('upload',views.upload,name="file_upload"),
    path('download',views.download,name="download"),
]