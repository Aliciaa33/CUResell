from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from user.models import UserInfo
from product.models import ProductInfo
from transaction.models import Transaction
from django.conf import settings
from hashlib import sha1
from django.http import JsonResponse
import random
import sqlite3
from django.views.decorators.http import require_http_methods
from django.contrib import messages

# Create your views here.
def update_user_rate(username):
    all_rate=0
    rate_number=0
    all_records = Transaction.objects.all()
    for record in all_records:
        if record.product.seller.username == username:
            all_rate += record.rate
            rate_number += 1
    rate=all_rate/rate_number
    user = UserInfo.objects.get(username=username)
    user.rate = rate
    user.rate_number = rate_number
    user.save()