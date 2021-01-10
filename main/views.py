from django.shortcuts import render, reverse

# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from .forms import ContactForm


def NewProfileView(request):
    print("recieved")
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            #now the data is good
            Contact.objects.create(**form.cleaned_data) 
            print("recieved 21")
            # try:
        
            
        else:
            
            print(form.errors)
        form = ContactForm()

    qs = Contact.objects.all()

    return render(request, 'index.html', {
       "form": form,
       "qs":qs,
  
    })


def index(request):
    try:
        send_mail("testing subject",
        "testing message",
        "j.meimar111@gmail.com",
        ["tikifa8504@nonicamy.com"],
        fail_silently=False)
        print("yes")
    except:
        print("no")

    return render(request, "send.html")