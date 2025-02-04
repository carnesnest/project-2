from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Department
from .models import Product

def home(request): # request sent to urls.py
    
    mydept = Department.objects.all()  # Query all depts from the database, no filtering

    # Render the template with the context
    # Search logic
    search_term = request.GET.get('search', '')
    if search_term:
        myproduct = Product.objects.filter(ProductName__icontains=search_term)
    else:
        myproduct = Product.objects.all()

    return render(request, 'home.html', {'mydept': mydept, 'myproduct': myproduct})

def product_list(request):
    search_term = request.GET.get('search', '')
    if search_term:
        myproduct = Product.objects.filter(ProductName__icontains=search_term)
    else:
        myproduct = Product.objects.all()
    
    return render(request, 'product_list.html', {'myproduct': myproduct})     

#def home(request):
  #template = loader.get_template('home.html')
  #return HttpResponse(template.render())