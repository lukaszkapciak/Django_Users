from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def ContactView(request):
    form = ContactForm(request.POST or None)
    title = 'Contact'
    return render(request, 'contact.html', {'form':form, 'title':title})