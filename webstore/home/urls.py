from django.urls import path
from . import views #this one shows stuff

urlpatterns = [
    path('', views.home, name='home'),
    path('product_search', views.product_list, name='product_search')
    
]