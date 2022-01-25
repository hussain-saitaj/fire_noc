from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from .models import *
import os
import mimetypes

# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                return render(request,'admin.html')
            else:
                auth.login(request,user)
                return render(request,'home.html')
                
    else:
        return render(request,'index.html')

def register(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('pass')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        aadhar=request.POST.get('aadhar')
        if len(CustomUser.objects.filter(aadhar=aadhar))!=0:
            return HttpResponse("User already registered")
        else:
            #print(password)
            user_object=User.objects.create_user(username=email,password=password)
            user_object.save()
            custom_user_object=CustomUser()
            custom_user_object.user=user_object
            custom_user_object.phone_no=phone
            custom_user_object.address=address
            custom_user_object.aadhar=aadhar
            custom_user_object.save()
            return redirect(reverse('login'))

    return render(request,'register.html')

def general(request):
    if request.method=='POST':
        name=request.POST['name']
        phone_no=request.POST['phone_no']
        email=request.POST['email']
        aadhar=request.POST['aadhar']
        site_name=request.POST['site_name']
        area=request.POST['area']
        application_object=Application()
        application_object.name=name
        application_object.phone_no=phone_no
        application_object.email=email
        application_object.aadhar=aadhar
        application_object.site_name=site_name
        application_object.area=area
        application_object.save()
        current_user=request.user
        print(current_user)
        custom_user=CustomUser.objects.get(user=current_user)
        custom_user.application.add(application_object)
        custom_user.save()
        return render(request,'form.html')
    
    return render(request,'general.html')

def upload(request):
    if request.method == 'POST' and 'docfile' in request.FILES:
        myfile = request.FILES
        file=myfile['docfile']
        # fs = FileSystemStorage()
        # filename = fs.save(file.name, file)
        # uploaded_file_url = fs.url(filename)
        current_user=request.user
        print(current_user)
        custom_user=CustomUser.objects.get(user=current_user)
        recent_application=custom_user.application.all().order_by('-id')[0]
        recent_application.form=file
        recent_application.save()
        return render(request, 'appFee.html', {
            'uploaded_file_url': recent_application.form.url
        })
      
    return render(request, 'form.html')



def download(request):
    # Define Django project base directory
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'front.pdf'
    # Define the full file path
    value=os.path.join(str(settings.BASE_DIR), "templates/")
    filepath =  value+ filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def AppPayment(request):
    
    return render(request,"areaFee.html")
    