from django.shortcuts import render
#from datetime import datetime
from home.models import Contact

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method =="POST":
        name = request.POST['Name']
        email = request.POST['Email']
        phone = request.POST['phone'] 
        desc = request.POST['desc']
        print(name,email,phone,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc);
        contact.save()
   
    return render(request,'contact.html')

# Create your views here.
