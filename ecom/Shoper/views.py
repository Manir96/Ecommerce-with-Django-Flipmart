from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from Category.models import Categories
from SubCategory.models import SubCategories
from . import models
from . models import Product
# Create your views here.

class homepage(View):
    def get(self, request):
        
        return render(request, 'user/home.html')
    
class comoncode(View):
    def get(self, request):
        
        return render(request, 'base_code/base.html')
    
class comoncode2(View):
    def get(self, request):
        
        return render(request, 'base_code/base2.html')
    
class footer(View):
    def get(self, request):
        
        return render(request, 'base_code/footer.html')
    
class header(View):
    def get(self, request):
        
        return render(request, 'base_code/header.html')
    
class logPage(View):
    def get(self, request):
        
        return render(request, 'naver/login.html')

class checkout(View):
    def get(self, request):
        
        return render(request, 'naver/checkout.html')
class my_cart(View):
    def get(self, request):
        
        return render(request, 'naver/my_cart.html')
    
    
class category_page(View):
    def get(self, request ):       
        return render(request, 'naver/category.html')
    
class product_comparison(View):
    def get(self, request, id): 
        ata2 = get_object_or_404(Product, id=id)  
        context = {'prod_data': ata2,} 
        return render(request, 'body_user/product-comparison.html',context)
    
def panel(request):
    all_data = SubCategories.objects.all()
    context = {"sub_cat":all_data,}
    return render(request, 'admin_user/product.html',context)

def product_store(request):
    
    if request.method == 'POST':
        sub_cat_id = request.POST.get('sub_cat_id')
        title = request.POST.get('p_title')
        selling_price = request.POST.get('product_price')
        discount_price = request.POST.get('discount_price')
        basi_description = request.POST.get('product_basic')
        details_description = request.POST.get('product_delails')
        brand = request.POST.get('product_brand')
        tag = request.POST.get('tag')
        stock = request.POST.get('product_stock')
        product_1_image = request.FILES.get('product_1_image')
        product_2_image = request.FILES.get('product_2_image')
        product_3_image = request.FILES.get('product_3_image')
        product_4_image = request.FILES.get('product_4_image')
        model = models.Product()
        model.sub_cat_id_id = sub_cat_id
        model.title = title
        model.selling_price = selling_price
        model.discount_price = discount_price
        model.basi_description = basi_description
        model.details_description = details_description
        model.brand = brand
        model.tag = tag
        model.stock = stock
        model.product_1_image = product_1_image
        model.product_2_image = product_2_image
        model.product_3_image = product_3_image
        model.product_4_image = product_4_image
        model.save()
        return redirect('panel')
    
    else:
        return render(request,'admin_user/product.html')
    
def product_list(request, id):
    cat = Categories.objects.values('id','name').distinct()
    data = SubCategories.objects.select_related('cat_id').values('id','name','cat_id').distinct()
    subcat = Categories.objects.values('id','name').distinct()
    product_data = Product.objects.select_related('sub_cat_id').filter(sub_cat_id=id).values('id','sub_cat_id','title','selling_price','discount_price','basi_description','details_description','brand','tag','stock','product_1_image','product_2_image','product_3_image','product_4_image',)
    Special_offer_products = product_data.order_by('-discount_price')[:8]
    
    
    sale_price = []
    for data_all in product_data:
        discount = data_all['discount_price']
        discount_price = (data_all['selling_price'] * discount)/100
        sale = data_all['selling_price'] - discount_price
        sale_price.append(sale)
    all_product_data = zip(product_data,sale_price)   
    context = {
        'all_data':data,
        'all_cat':cat,
        'all_sub_cat':subcat,
        'all_productData':all_product_data,
        'allProduct_data':Special_offer_products,
        
        }
    return render(request, 'naver/product_list.html',context)

# def product_detail(request, id):
#     data = get_object_or_404(Product, id=id)  
#     context = {"product_deta": data,}
#     return render(request, 'admin_user/detail.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    data = get_object_or_404(Product, id=id)
    product_data = Product.objects.select_related('sub_cat_id').filter(sub_cat_id=id).values('id','sub_cat_id','title','selling_price','discount_price','basi_description','details_description','brand','tag','stock','product_1_image','product_2_image','product_3_image','product_4_image',)
    Special_offer_products = product_data.order_by('-discount_price')[:8]
    if product.discount_price:
        discount_amount = (product.selling_price * product.discount_price) / 100
        sale_price = product.selling_price - discount_amount
    else:
        sale_price = product.selling_price
    context = {
        "product_detail": product,
        "sale_price": sale_price,
        "product_deta": data,
        "discount_deta": Special_offer_products,
        
    }
    
    return render(request, 'admin_user/detail.html', context)

def wishlist_ditails(request, id):
    wishlist = get_object_or_404(Product, id=id) 
    data = get_object_or_404(Product, id=id)
    if wishlist.discount_price:
        discount_amount = (wishlist.selling_price * wishlist.discount_price) / 100
        sale_price = wishlist.selling_price - discount_amount
    else:
        sale_price = wishlist.selling_price
    context = {
        'wishlist_data': wishlist,
        "salleing_price": sale_price,
        "product_deta": data,
    } 
    
    return render(request, 'naver/wishlist.html', context )
def wishlist(request):
    return render(request, 'naver/wishlist.html' )
