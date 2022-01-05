from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
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
                return render(request,'register.html')
            else:
                return render(request,'home.html')
                
    else:
        return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def general(request):
    if request.method=='POST':
        return render(request,'form.html')
    
    return render(request,'general.html')

def upload(request):
    if request.method == 'POST' and 'docfile' in request.FILES:
        print("hai")
        myfile = request.FILES
        file=myfile['docfile']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'appFee.html', {
            'uploaded_file_url': filename
        })
    print("hello")    
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