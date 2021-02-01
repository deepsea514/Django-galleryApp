from django.shortcuts import render, redirect
from controlpannel.models import Product, Comments
from authorization.models import User
# Create your views here.
def index(request):
    return render(request,'index.html', {})

def gallery(request):
    obj = Product.objects.all()
    for i in obj:
        print(i.P_id)

    return render(request,'gallery.html', {'product_images':obj})

def product_detail(request,key_id):
    print(key_id)
    product = Product
    product_obj = product.objects.get(P_id=key_id)
    comment = Comments
    obj = comment.objects.filter(P_id=product_obj)
    comment_data = []
    for i in obj:
        comment_data.append({'COMMENT': i.comment, 'NAME': i.user.name})

    if request.method == 'POST':
        message = request.POST.get('message')

        if 'email' in request.session:
            # print(message)
            new_comment = Comments
            check_user = User.objects.get(email=str(request.session['email']))
            get_product = Product.objects.get(P_id=key_id)
            try:
                query = new_comment.objects.get(user=check_user, P_id=key_id)
                print("comment already exists")
                comment = Comments
                obj = comment.objects.filter(P_id=product_obj)
                del comment_data
                comment_data = []
                for i in obj:
                    comment_data.append({'COMMENT': i.comment, 'NAME': i.user.name})

                return render(request, 'product-detail.html', {'data': comment_data, 'image': product_obj, 'error': 'You can enter only one comment' })

            except new_comment.DoesNotExist:
                Comments.objects.create(comment=message, user=check_user, P_id=get_product)
                comment = Comments
                obj = comment.objects.filter(P_id=product_obj)
                del comment_data
                comment_data = []
                for i in obj:
                    comment_data.append({'COMMENT': i.comment, 'NAME': i.user.name})

                return render(request, 'product-detail.html', {'data': comment_data, 'image': product_obj})


        else:
            comment = Comments
            obj = comment.objects.filter(P_id=product_obj)
            del comment_data
            comment_data = []
            for i in obj:
                comment_data.append({'COMMENT': i.comment, 'NAME': i.user.name})
            return render(request, 'product-detail.html', {'data': comment_data, 'image': product_obj, 'error_login':'You need to login first!'})


    #print(comment_data)


    print(product_obj.P_image)

    return  render(request,'product-detail.html', {'data': comment_data, 'image': product_obj})