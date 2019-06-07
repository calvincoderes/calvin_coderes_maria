from django.contrib import admin
from .models import HmoProvider, Plan, User, Cart, CartItem

# Register your models here.
admin.site.register(HmoProvider)
admin.site.register(Plan)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(CartItem)

