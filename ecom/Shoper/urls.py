from django.urls import path
from django.contrib.auth import views as auth_views
from Shoper import views
from . import views as product
urlpatterns = [
    # path('', views.homepage.as_view(), name="home" ),
    path('base/', views.comoncode.as_view()),
    path('base2/', views.comoncode2.as_view()),
    path('footer/', views.footer.as_view()),
    path('header/', views.header.as_view()),
    path('login/', views.logPage.as_view(), name="log" ),
    path('checkout/', views.checkout.as_view(), name="checkout" ),
    path('my_cart/', views.my_cart.as_view(), name="my_cart" ),
    path('wishlist/', views.wishlist, name="wishlist_home" ),
    path('wishlist/<int:id>', views.wishlist_ditails, name="wishlist" ),
    path('category_list/', views.category_page.as_view(), name="category_list" ),
    path('comparison/', views.product_comparison.as_view(), name="comparison" ),
    path('comparison/<int:id>', views.product_comparison.as_view(), name="comparison" ),
    
    
    path('panel/', product.panel, name='panel'),
    path('panel/product/store/', product.product_store,name='product_store'),
    path('product_list/<int:id>', product.product_list,name='product_list'),
    # path('product_detail/', product.product_detail,name='product_detail'),
    path('product_detail/<int:id>', product.product_detail,name='product_detail'),
    
]
