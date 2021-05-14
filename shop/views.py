from django.shortcuts import render , HttpResponse
from datetime import datetime
from shop.models import Contact
# Create your views here.
def index(request) :
    content = {
        'var'  : "Abhishek Sharma"
    }
    return render(request , 'index.html' , content)

def services(request) : 
    return HttpResponse("This is our Services")

def contact(request) : 
    if request.method == "POST" : 
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        contact = Contact(name = name , email = email , number = number , desc = desc , date = datetime.today())
        contact.save()

    return render(request , 'contact.html')
