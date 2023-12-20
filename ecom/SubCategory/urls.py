from django.urls import path
from . import views as subcat

urlpatterns = [
    path('panel/', subcat.panel),
    path('store/', subcat.sub_store,name='sub_cat_store'),
]
