from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def sendemail(request):
    if request.method == 'POST':

        contact = ContactForm(data = request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request, 'Your submission has been received. We will reach out to you shortly!')
            return redirect('/')
        else:
            return render(request, 'PAGES/index.html', {'form': form})
