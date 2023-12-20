from django.urls import path
from . import views as home


urlpatterns = [
    path('', home.index,name="home"),
    path('img_upload/', home.ima_upload.as_view()),
    path('img_store/', home.slider_img_store,name='slider_store'),
    path('img_medel/', home.ima_medel.as_view()),
    path('img_medel_store/', home.medel_img_store,name='img_medel_store'),
    # path('eight/', home.last_eight_products,name='eight_product'),
]
