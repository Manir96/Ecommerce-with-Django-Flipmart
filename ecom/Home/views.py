from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.views import View
from Category.models import Categories
from SubCategory.models import SubCategories
from Shoper.models import Product
from Home.models import Top_Banner_Images, Midel_40_Images
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.

def index(request):
    data1 = Categories.objects.values('id','name').distinct()
    data2 = SubCategories.objects.select_related('cat_id').values('id','name','cat_id').distinct()
    # data3 = Product.objects.select_related('sub_cat_id').values('id','sub_cat_id','title','selling_price','discount_price','basi_description','details_description','brand','tag','stock','product_1_image','product_2_image','product_3_image','product_4_image').distinct()
    data3 = Product.objects.select_related('sub_cat_id').values(
        'id', 'sub_cat_id', 'title', 'selling_price', 'discount_price', 
        'basi_description', 'details_description', 'brand','tag', 'stock', 
        'product_1_image', 'product_2_image', 'product_3_image', 'product_4_image'
    ).distinct()
    latest_products = data3.order_by('-id')[:8]
    hot_deal_products = data3.order_by('-discount_price')[:8]
    
    banner = Top_Banner_Images.objects.values('id','top_brand','new_collection','description','slider',).distinct()
    medel_banner = Midel_40_Images.objects.values('id','new','new_fashion','description_40','image',).distinct()
    context = {'all_cat':data1,'sub_cat':data2,'product_data':latest_products, 'images_data':banner, 'midel_image':medel_banner,'product_hot_deals':hot_deal_products,}
    
    return render(request,'user/home.html',context)


class ima_upload(View):
    def get(self, request):
        storage = messages.get_messages(request)
        storage.used = True
        return render(request,'admin_user/images_upload.html')

def slider_img_store(request):
    top_brand = request.POST.get('top_brand')
    new_collection = request.POST.get('new_collection')
    description = request.POST.get('banner_descr')
    slider = request.FILES.get('slider')
    model = models.Top_Banner_Images()
    model.top_brand = top_brand
    model.new_collection = new_collection
    model.description = description
    model.slider = slider
    model.save()

    return render(request,'admin_user/images_upload.html')



class ima_medel(View):
    def get(self, request):
        storage = messages.get_messages(request)
        storage.used = True
        return render(request,'admin_user/img_40_upload.html')
    
def medel_img_store(request):
    new = request.POST.get('new')
    new_fashion = request.POST.get('new_fashion')
    description_40 = request.POST.get('description_40')
    image = request.FILES.get('image')
    model = models.Midel_40_Images()
    model.new = new
    model.new_fashion = new_fashion
    model.description_40 = description_40
    model.image = image
    model.save()
    
    return render(request,'admin_user/img_40_upload.html')
