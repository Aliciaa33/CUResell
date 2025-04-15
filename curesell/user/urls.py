from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login,name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^register_handle/$',views.register_handle),
    url(r'^login_handle/$',views.login_handle),
    url(r'^logout/$',views.logout),
    url(r'^user/homepage/$',views.homepage,name='homepage'),
    url(r'^verification/', views.verification, name='verification'),
    url(r'^verification_handle/$',views.verification_handle),
]