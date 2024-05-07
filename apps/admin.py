from django.contrib import admin
from apps.models import Product, Degree


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ("name", "degree")
