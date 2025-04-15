from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product_info/$', views.product_info),
    url(r'^ProductPost/$',views.ProductPost),
    url(r'^search_default/$',views.search_default),
]