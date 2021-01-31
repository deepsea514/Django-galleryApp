from django.shortcuts import render
from .forms import ImageForm
from .models import Product


# Create your views here.
def control_pannel(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'admin.html', {'form': form})

def test(request):
    product_obj = Product.objects.all()
    for i in product_obj:
        print(i.P_image)

    return render(request, 'test.html', {'obj': product_obj})