from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product_info/$', views.product_info),
    url(r'^ProductPost/$',views.ProductPost),
    url(r'^search_default/$',views.search_default),
    url(r'^after_search/$',views.after_search),
    url(r'^prod_post_handle/$',views.prod_post_handle),
    url(r'^detail/$',views.detail),
]