from django.contrib import admin
from .models import Order, OrderItem
import xadmin


class OrderAdmin:
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']

xadmin.site.register(Order,OrderAdmin)