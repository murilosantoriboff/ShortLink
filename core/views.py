from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortURL
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def valida_link(request):
    original_url = request.POST.get('original_url')
    short_url = request.POST.get('short_url')

    links = ShortURL.objects.filter(short_url=short_url)
    if len(links) > 0:
        messages.add_message(request, messages.constants.ERROR, 'Ja existe um link com esse nome!!')
        return redirect('/')
    
    
    