from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.welcome),
    url(r'^$', views.homepage),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^verification/$',views.verification),
]