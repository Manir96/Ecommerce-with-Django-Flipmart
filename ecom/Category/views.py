from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . models import Categories
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

def panel(request):
    storage = messages.get_messages(request)
    storage.used = True
    return render(request,'admin_user/category.html')

def store(request):
    try:
        
        nam = request.POST.get('cat_name')
        if (len(nam) < 3 ):
            messages.error(request, 'minimum 3')
            return render(request,'admin_user/category.html')
        
        if models.Categories.objects.filter(name=nam).exists():
            messages.info(request, 'Category already exists.')
            return render(request,'admin_user/category.html')
        
        else:
            cat_model = models.Categories()
            cat_model.name = nam
            cat_model.save()
            messages.success(request, 'The Category hase been inserted Successfully')
            return render(request,'admin_user/category.html')
    except (IntegrityError) as e: 
        messages.error(request, 'The Category hase been inserted Successfully')
        return render(request,'admin_user/category.html')
        
