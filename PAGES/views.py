from django.shortcuts import render
from sendemail.forms import ContactForm

def index(request):
    form = ContactForm()
    return render(request, 'PAGES/index.html', {'form': form})
