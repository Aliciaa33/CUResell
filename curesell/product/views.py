from django.utils import timezone
from django.shortcuts import render,redirect, HttpResponse
from .models import *
from django.conf import settings
from user.models import UserInfo
from product.models import ProductInfo
from transaction.models import Transaction
import random, string, os
from django.contrib import messages


def product_info(request):
    return render(request,'product_info.html')

def ProductPost(request):
    username = request.session.get('username')
    userinfo = UserInfo.objects.filter(username=username).first()

    if userinfo and userinfo.email != '':
        return render(request, 'ProductPost.html')
    else:
        return redirect('/send_code')

def search_default(request):
    # get all unsold products in current database
    products = ProductInfo.product.get_unsold() 
    return render(request,'search_default.html', {'products': products})

def after_search(request):
    search_title = request.POST.get('query')
    if search_title == '':
        return redirect('/search_default')
    products = ProductInfo.product.filter(title__contains=search_title).exclude(isSold=True)
    context = {'products':products, 'search_title':search_title}
    return render(request, 'after_search.html', context)

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
    prod_id = request.GET['prod_id']
    product = ProductInfo.product.get_prod(prod_id)[0]
    context = {'product': product}
    return render(request, 'product_info.html', context)

def make_transaction(request):
    post = request.POST
    user_id = request.session.get('user_id')
    buyer = UserInfo.objects.get(id=user_id)
    product_id = post.get('product_id')
    product = ProductInfo.product.filter(id=product_id)[0]

    if not buyer.email.strip():
        return redirect(f'/product_info/?product_id={product_id}&error=unverified')

    if product.isSold:
        return redirect(f'/product_info/?product_id={product_id}&error=sold')
    
    if product.seller.id == buyer.id:
        return redirect(f'/product_info/?product_id={product_id}&error=own')

    Transaction.objects.create(
        buyer=buyer,
        product=product,
        price=product.price,
        date=timezone.now(),
        rate=5
    )
    product.isSold = True
    product.save()

    seller = product.seller
    old_score = seller.rate
    old_count = seller.rate_number
    new_score = (old_score * old_count + 5) / (old_count + 1)
    seller.rate = new_score
    seller.rate_number = old_count + 1
    seller.save()

    return redirect('/search_default')

