from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.welcome),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^login/$',views.login, name='login'),
    url(r'^login_handle/$',views.login_handle),
    url(r'^logout/$',views.logout),
    url(r'^register/$',views.register, name='register'),
    url(r'^register_handle/$',views.register_handle),
    url(r'^skip_verify/$',views.skip_verify, name='skip_verify'),
    url(r'check_email/', views.check_email, name='check_email'),
    url(r'^send_code/$',views.send_code),
    url(r'^send_code_handle/$',views.send_code_handle),
    url(r'^verification_handle/$',views.verification_handle),
    url(r'^search/$',views.search),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^release_records/$',views.release_records, name='release_records'),
    url(r'^purchase_records/$',views.purchase_records, name='purchase_records'),
]