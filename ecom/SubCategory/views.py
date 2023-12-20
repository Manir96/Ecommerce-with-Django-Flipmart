from django.shortcuts import render
from django.http import HttpResponse
from . import models
from Category.models import Categories
# Create your views here.

def panel(request):
    data = Categories.objects.all()
    context = {"cat_data":data}
    return render(request,'admin_user/subcat.html',context)

def sub_store(request):
    name = request.POST.get('sub_cat_name')
    cat_id = request.POST.get('cat_id')
    sub_cat_model = models.SubCategories()
    sub_cat_model.name = name
    sub_cat_model.cat_id_id = cat_id
    sub_cat_model.save()
    return render(request,'admin_user/subcat.html')
