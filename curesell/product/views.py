from django.shortcuts import render,redirect, HttpResponse
from .models import *
from django.conf import settings
from user.models import UserInfo
from product.models import ProductInfo
import random, string, os

def product_info(request):
    return render(request,'product_info.html')

def ProductPost(request):
    return render(request,'ProductPost.html')

def search_default(request):
    products = ProductInfo.product.get_all() # get all products in current database
    return render(request,'search_default.html', {'products': products})

def generate_random_string(length=8):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(length))

def prod_post_handle(request):
    post = request.POST
    title = post.get('prod_title')
    price = post.get('prod_price')
    # picture = post.get('picture')
    picture = request.FILES['prod_image']
    base_filename, ext = os.path.splitext(picture.name)
    pic_name = f"{base_filename}_{generate_random_string()}{ext}"
    fname = '%s/product/%s' % (settings.MEDIA_ROOT, pic_name)
    with open(fname, 'wb') as pic:
        for c in picture.chunks():
            pic.write(c)
    description = post.get('description')
    user_id = request.session.get('user_id')
    user = UserInfo.objects.filter(id=user_id)[0]
    ProductInfo.product.create_prod(title, description, 'product/'+pic_name, price, user)
    return redirect('/search')

def detail(request):
    title = request.GET['title']
    product = ProductInfo.product.get_title(title)[0]
    context = {'product': product}
    print(product.title)
    return render(request, 'product_info.html', context)