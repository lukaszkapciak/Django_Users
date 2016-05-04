from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def ContactView(request):
    form = ContactForm(request.POST or None)
    title = 'Contact'
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        print ("Name: "+ name)
        print ("Email: " + email)
        print ("Message: " + message)
        #send_mail('New message from '+name+' via '+email, message, settings.EMAIL_HOST_USER,
                  #['to someone'], fail_silently=False)
        return redirect('/books')
    return render(request, 'contact.html', {'form':form, 'title':title})