from django.conf.urls import url
from . import views
app_name = 'transaction'
urlpatterns = [
    url(r'^rate-purchases/$',views.rate_purchases, name='rate_purchases'),
]