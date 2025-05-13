from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from user.models import UserInfo
from product.models import ProductInfo
from transaction.models import Transaction
from transaction.views import update_user_rate
from django.conf import settings
from hashlib import sha1
from django.core.mail import send_mail
from django.http import JsonResponse
import random
import sqlite3
from django.contrib import messages
from django.views.decorators.http import require_http_methods

def homepage(request):
    return render(request,'homepage.html')

def terms(request):
    return render(request,'terms.html')

def privacy(request):
    return render(request,'privacy.html')

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'uname' : uname}
    return render(request,'login.html',context)

def login_handle(request):
    post = request.POST
    username = post.get('username')
    password = post.get('password')
    users = UserInfo.objects.filter(username=username)
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
    errors = {}
    if UserInfo.objects.filter(username=username).exists():
        errors['username'] = "- Username already existed"

    if errors:
        context = {
            'error': errors,
            'username': username,
            'password': password,
            'password2': password2
        }
        return render(request, 'register.html', context)
    
    # update database if valid
    s1 = sha1()
    s1.update(password.encode('utf8'))
    upwd3 = s1.hexdigest()
    user = UserInfo()
    user.username = username
    user.password = upwd3
    user.save()
    request.session['username'] = username
    return redirect('/send_code')

def skip_verify(request):
    return render(request,'login.html')

def search(request):
    products = ProductInfo.product.get_unsold() # get all unsold products in current database
    return render(request,'search_default.html', {'products': products})

def send_code(request):
    return render(request,'email.html')

def check_email(request):
    email = request.POST.get('email')
    exists = UserInfo.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})

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
    
def purchase_records(request):
    username = request.session.get('username')
    userinfo = UserInfo.objects.filter(username=username).first()
    all_records = Transaction.objects.all()
    records=[]
    for index, record in enumerate(all_records):
        if record.buyer==userinfo:
            records.append({"prod":record.product,"rate":record.rate,"price":record.price,"date":record.date,"transaction_index":index})
    content={'records': records}
    return render(request, 'purchase_records.html', content)

@require_http_methods(["GET", "POST"])
def rate_purchases(request):
    if request.method == "POST":
        # Get the product ID and rating from the request
        product_id = request.POST.get("product_id")
        rating = request.POST.get("rating")

        # Validate the inputs
        if not product_id or not rating:
            return JsonResponse({"error": "Product ID and rating are required."}, status=400)

        try:
            # Convert rating to an integer
            rating = int(rating)
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5.")
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

        print(f"Rating for product {product_id}: {rating}")

        # Update the rating in the database
        all_records = Transaction.objects.all()
        the_records = all_records[int(product_id)]
        the_records.rate = rating
        the_records.save()
        seller = the_records.product.seller
        update_user_rate(seller.username)


        return JsonResponse({"success": "Rating submitted successfully."})
    
def check_verification_status(request):
    try:
        username = request.session.get('username')
        userinfo = UserInfo.objects.filter(username=username).first()
        is_verified = userinfo.email != ''
        return JsonResponse({'verified': is_verified})
    except UserInfo.DoesNotExist:
        return JsonResponse({'verified': False, 'error': 'User not found'}, status=404)