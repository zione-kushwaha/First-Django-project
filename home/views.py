from django.shortcuts import render,HttpResponse
from home.models import contact
# Create your views here.
def home(request):
    
    return render(request,'home.html')

#function for contact
def contact_form(requerst):
    if requerst.method=="POST":
        print('this is a post ')
        name=requerst.POST['name']
        email=requerst.POST['email']
        message=requerst.POST['message']
        print(name,email,message)
        ins=contact(name=name,email=email,message=message)
        ins.save()
        print('the data have been writtten to the database')
    return render(requerst,'contact.html')

#fucntion for the about
def about(requerst):
    return render(requerst,'about.html')

#function for the project
def project(requerst):
    return render(requerst,'project.html')