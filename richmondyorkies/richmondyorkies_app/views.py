from contextlib import redirect_stderr
from email import message
from multiprocessing import context
from django.shortcuts import render, redirect

from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
from .models import Dog, Index


def error_404_view(request, exception):
    return render(request, 'errors/404.html')

def error_500_view(request):
    return render(request, 'errors/500.html')

def error_403_view(request, exception):
    return render(request, 'errors/403.html')

def error_400_view(request, exception):
    return render(request, 'errors/400.html')

def home(request):
    dogs = Dog.objects.filter(active=True)
    about = Index.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Thank you for your inquiry, {name}')
            return redirect('/')
        else:
            messages.warning(request, f'Form was not valid.')
    else:
        form = ContactForm()
    context = {'form':form, 'dogs':dogs, 'about': about}
    return render(request, 'richmondyorkies_app/index.html', context)

def dog(request, slug):
    dogs = Dog.objects.filter(active=True).exclude(slug=slug)
    dog = Dog.objects.get(slug=slug)
    context = {'dog':dog, 'dogs':dogs}
    return render(request, 'richmondyorkies_app/dog.html', context)