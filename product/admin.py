from django.contrib import admin
from .models import Product, Category, Variation
# Register your models here.
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(Category)