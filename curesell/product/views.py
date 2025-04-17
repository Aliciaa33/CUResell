from django.shortcuts import render,redirect, HttpResponse
from .models import *
from django.conf import settings
from user.models import UserInfo

def product_info(request):
    return render(request,'product_info.html')

def ProductPost(request):
    return render(request,'ProductPost.html')

def search_default(request):
    return render(request,'search_default.html')

def prod_post_handle(request):
    post = request.POST
    title = post.get('prod_title')
    # type = post.get('type')
    price = post.get('prod_price')
    address = post.get('address')
    # picture = post.get('picture')
    picture = request.FILES['prod_image']
    fname = '%s/product/%s' % (settings.MEDIA_ROOT, picture.name)
    with open(fname, 'wb') as pic:
        for c in picture.chunks():
            pic.write(c)
    description = post.get('description')
    user_id = request.session.get('user_id')
    user = UserInfo.objects.filter(id=user_id)[0]
    # ProductInfo.goods.create_good(title,type,'goods/'+picture.name,price,address,description,user)
    ProductInfo.product.create_prod(title, description, picture, price, user)
    return redirect('/search')