from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from user.models import UserInfo
from product.models import ProductInfo
from django.conf import settings
from hashlib import sha1
from django.core.mail import send_mail
from django.http import JsonResponse
import random
import sqlite3

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'uname' : uname}
    return render(request,'login.html',context)

def login_handle(request):
    post = request.POST
    username = post.get('username')
    password = post.get('password')
    users = UserInfo.objects.filter(username=username)
    print(username)
    if len(users) == 1:
        s1 = sha1()
        s1.update(password.encode('utf8'))
        if s1.hexdigest() == users[0].password:
            red = HttpResponseRedirect('/search')
            request.session['user_id'] = users[0].id
            request.session['username'] = users[0].username
            return red
        else:
            context = {'title': 'Login', 'username': username, 'password': password, 'error_msg':'Wrong Password'}
            return render(request, 'login.html', context)
    else:
        context = {'title': 'Login',  'number': username, 'password': password, 'error_msg':'Wrong Username'}
        return render(request, 'login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def register(request):
    return render(request,'register.html')

def register_handle(request):
    post = request.POST
    username = post.get('username')
    password = post.get('password')
    password2 = post.get('password2')
    contact_link = post.get('contact_link')
    errors = {}
    if UserInfo.objects.filter(username=username).exists():
        errors['username'] = "- Username already existed"

    if errors:
        context = {
            'error': errors,
            'username': username,
            'password': password,
            'password2': password2,
            'contact_link': contact_link
        }
        return render(request, 'register.html', context)
    
    # update database if valid
    print(contact_link)
    s1 = sha1()
    s1.update(password.encode('utf8'))
    upwd3 = s1.hexdigest()
    user = UserInfo()
    user.username = username
    user.password = upwd3
    user.contact_link = contact_link
    user.save()
    request.session['username'] = username
    return redirect('/send_code')

def skip_verify(request):
    return render(request,'login.html')
    
# def verification(request):
#     return render(request,'verification.html')

def search(request):
    products = ProductInfo.product.get_all() # get all products in current database
    return render(request,'search_default.html', {'products': products})

def send_code(request):
    return render(request,'email.html')

def send_code_handle(request):
    email = request.POST.get('email')
    verification_code = random.randint(100000, 999999)  # Generate a new 6-digit code

    # Store the latest code in the session
    request.session['verification_code'] = verification_code
    request.session['user_email'] = email

    # Send email
    send_mail(
        'Your Verification Code',
        f'Your verification code is: {verification_code}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return render(request, 'verify.html')

def verification_handle(request):
    usercode = request.POST.get('code')
    generated = request.session.get('verification_code')
    
    if str(usercode) == str(generated):
        username = request.session.get('username')
        user_email = request.session.get('user_email')
        user = UserInfo.objects.filter(username=username).first()
        if user:
            user.email = user_email
            user.save()
        request.session.flush()
        return redirect('/login')
    
    context = {'title': 'Verify', 'error_msg': 'Wrong Code'}
    return render(request, 'verify.html', context)

def profile(request):
    username = request.session.get('username')

    userinfo = UserInfo.objects.filter(username=username).first()

    # contact_link = userinfo.contact_link
    rate = userinfo.rate
    if username == None:
        context = { 'error_msg': 'please login first'}
        return render(request, 'profile.html', context)
    else:
        context = {'username': username, 'rate1': rate, 'rate2': int(rate*100)}
        return render(request, 'profile.html', context)
    
def release_records(request):
    username = request.session.get('username')
    userinfo = UserInfo.objects.filter(username=username).first()
    if userinfo == None:
        context = { 'error_msg': 'please login first'}
        return render(request, 'release_records.html', context)
    else:
        all_products = ProductInfo.product.get_all() 
        user_products=[]
        for product in all_products:
            if product.seller==userinfo:
                user_products.append(product)
        content={'products': user_products}
        return render(request, 'release_records.html', content)