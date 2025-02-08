from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable":"AZ"
    }
    return render(request,"index.html",context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request,"about.html")
    # return HttpResponse("this is about")

def services(request):
    return render(request,"services.html")
    # return HttpResponse("this is services")

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        textarea = request.POST.get('textarea')
        contact = Contact(name=name,email=email,textarea=textarea,date=datetime.today())
        contact.save()
        messages.success(request, "Profile details submitted.")
    return render(request,"contact.html")