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
    
    link = ShortURL(original_url=original_url, short_url=short_url)

    link.save()

    messages.add_message(request, messages.constants.SUCCESS, 'Link criado com sucesso!!')
    messages.add_message(request, messages.constants.INFO, 'Seu link é http://127.0.0.1:8000/'+short_url)
    return redirect('/')

def redirecionar(request, link):
    url = ShortURL.objects.filter(short_url=link)
    if len(url) == 0:
        messages.add_message(request, messages.constants.ERROR, 'Ja não existe esse link')
        return redirect('/')
    else:
        return redirect(url[0].original_url)
    