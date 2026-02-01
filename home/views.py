from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    context = {
           "name" : "Chandrika's Role"
    }
    # return HttpResponse("Hello,Worls!!")
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse("This is My About page")
  return render(request,'about.html')

def services(request):
    # return HttpResponse("This is My services page")
  return render(request,'services.html')

def contact(request):
     if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
     return render(request,'contact.html')