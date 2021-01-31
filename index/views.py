from django.shortcuts import render
from controlpannel.models import Product
# Create your views here.
def index(request):
    return render(request,'index.html', {})

def gallery(request):
    obj = Product.objects.all()



    return render(request,'gallery.html', {'product_images':obj})

def product_detail(request):
    return  render(request,'product-detail.html', {})