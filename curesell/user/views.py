from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponseRedirect
from hashlib import sha1
from .models import *

# Create your views here.
def homepage(request):
    return render(request, 'user/homepage.html')

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'uname' : uname}
    return render(request,'user/login.html',context)

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
            red = HttpResponseRedirect('/')
            request.session['user_id'] = users[0].id
            request.session['username'] = users[0].username
            return red
        else:
            context = {'title': 'Login', 'username': username, 'password': password, 'error_msg':'Wrong Password'}
            return render(request, 'user/login.html', context)
    else:
        context = {'title': 'Login',  'number': username, 'password': password, 'error_msg':'Wrong Username'}
        return render(request, 'user/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def register(request):
    context = {}
    return render(request,'user/register.html',context)

def register_handle(request):
    username = post.get('username')
    password = post.get('password')

    errors = {}
    if UserInfo.objects.filter(username=username).exists():
        errors['username'] = "- Username already existed"

    if errors:
        context = {'errors': errors, 'preserved_username': username}
        return render(request, 'user/register.html', context)
    
    # update database if valid
    s1 = sha1()
    s1.update(password.encode('utf8'))
    upwd3 = s1.hexdigest()
    user = UserInfo()
    user.username = username
    user.password = upwd3
    user.save()
    return redirect('/user/login')

def verification(request):
    return render(request,'user/verification.html')

def verification_handle(request):
    post = request.POST
    code = post.get('code')
    
    if code == "135246":
        return redirect('/user/login')
    
    context = {'title': 'Verify',  'error_msg':'Wrong Code'}
    return render(request, 'user/verification.html', context)