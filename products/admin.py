from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, \
    PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import Category, Product, Workshop, DigitalProduct, Updates


class ModelAChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Product  # Optional, explicitly set here.


@admin.register(Workshop)
class ProductAdmin(ModelAChildAdmin):
    base_model = Workshop  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site


@admin.register(DigitalProduct)
class ProductAdmin(ModelAChildAdmin):
    base_model = DigitalProduct  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site


@admin.register(Product)
class ProductAdmin(PolymorphicParentModelAdmin):
    base_model = Product  # Optional, explicitly set here.
    child_models = (Workshop, DigitalProduct)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class UpdatesAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'product',
        'created_on',
        'major_update',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Updates, UpdatesAdmin)
