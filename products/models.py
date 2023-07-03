from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel
from django.utils.text import slugify
from django.db.models.signals import pre_save


def slug_generator(sender, instance, *args, **kwargs):
    if instance.slug != slugify(instance.name):
        instance.slug = slugify(instance.name)


class Category(models.Model):
    # Category model taken from Code Institute's Boutique Ado project
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(PolymorphicModel):
    # Base of product model taken from Code Institute's Boutique Ado project,
    # but adjusted here to fit the needs of this project
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    host_creators = models.ManyToManyField(User, related_name='product_creators', blank=True)

    def __str__(self):
        return self.name


class Workshop(Product):
    location = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    total_slots = models.IntegerField()
    attendance = models.ManyToManyField(User, related_name='workshop_attendees', blank=True)


class DigitalProduct(Product):
    file = models.FileField(upload_to='media/student_resources/')
    pages = models.IntegerField()
    owners = models.ManyToManyField(User, related_name='resource_owners', blank=True)


class Updates(models.Model):
    subject = models.CharField(max_length=200, unique=True)
    update_description = models.TextField()
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    major_update = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.subject


# Autogenerates slugs if the no slug exists or
# name of page changes
pre_save.connect(slug_generator, sender=Workshop)
pre_save.connect(slug_generator, sender=DigitalProduct)
pre_save.connect(slug_generator, sender=Product)
