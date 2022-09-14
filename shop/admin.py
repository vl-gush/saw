from django.contrib import admin

from shop.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "external_id")
    search_fields = ("title", "external_id")
