from django.contrib import admin
# from . import category
from django.urls import path
from . import views as cat

urlpatterns = [
    path('', cat.panel),
    path('store/', cat.store,name='cat_store'),
]