from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import *
from django.conf import settings
from hashlib import sha1
from .models import *
from django.core.mail import send_mail
from django.http import JsonResponse
import random

# def welcome(request):
#     return HttpResponse("Testing: Hello World!")

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    # return render(request,'login.html')
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
    user.rate= 3.0
    user.contact_link = contact_link
    user.save()
    # return redirect('/login')
    # return redirect('/verification')
    return redirect('/send_code')

def skip_verify(request):
    return render(request,'login.html')
    
def verification(request):
    return render(request,'verification.html')

def search(request):
    return render(request,'search_default.html')

def send_code(request):
    return render(request,'email.html')

def send_code_handle(request):
    email = request.POST.get('email')
    verification_code = random.randint(100000, 999999)  # Generate a new 6-digit code

    # Store the latest code in the session
    request.session['verification_code'] = verification_code
    # print(f"Verification code: {verification_code}")

    # Send email
    send_mail(
        'Your Verification Code',
        f'Your verification code is: {verification_code}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    context = {'title': 'Verify', 'email': email, 'error_msg':'Wrong Code'}
    return render(request, 'verify.html')
    # return JsonResponse({'success': True, 'message': 'Verification code sent!'})

def verification_handle(request):
    usercode = request.POST.get('code')
    generated = request.session.get('verification_code')
    # print(f"stored code : {generated}")
    
    if str(usercode) == str(generated):
        return redirect('/login')
    
    context = {'title': 'Verify', 'error_msg': 'Wrong Code'}
    return render(request, 'verify.html', context)

def profile(request):
    username = request.session.get('username')

    userinfo = UserInfo.objects.filter(username=username).first()


    contact_link = userinfo.contact_link
    rate = userinfo.rate
    if username == None:
        context = { 'error_msg': 'please login first'}
        return render(request, 'profile.html', context)
    else:
        context = {'username': username, 'contact_link': contact_link, 'rate1': rate, 'rate2': int(rate*100)}
        return render(request, 'profile.html', context)