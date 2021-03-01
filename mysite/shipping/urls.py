from django.urls import path

from . import views
from .views import *

app_name = 'shipping'
urlpatterns = [
    path('', index, name='index'),

    # path('branches/', branch, name='branch'),
    #
    # path('washers/', washers_list, name='washer'),
    #
    # path('coupons/', coupon, name='coupon'),
    #
    # path('cars/', car, name='car'),
    #
    # path('orders/', order, name='order'),
]
