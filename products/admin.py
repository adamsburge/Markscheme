from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import Category, Product, Workshop, StudentResource


class ModelAChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Product  # Optional, explicitly set here.


@admin.register(Workshop)
class ProductAdmin(ModelAChildAdmin):
    base_model = Workshop  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site


@admin.register(StudentResource)
class ProductAdmin(ModelAChildAdmin):
    base_model = StudentResource  # Explicitly set here!
    show_in_index = True  # makes child model admin visible in main admin site


@admin.register(Product)
class ProductAdmin(PolymorphicParentModelAdmin):
    base_model = Product  # Optional, explicitly set here.
    child_models = (Workshop, StudentResource)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Category, CategoryAdmin)
