"""curesell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

====== URL organizations ======
1. users: all the pages related to user information: register, sign in, registration, profile
2. products: all pages related to product: search, post
3. transaction: all pages related to transaction
"""
# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^',include('product.urls')),
    url(r'^',include('user.urls')),
]