from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel


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
    slug = models.SlugField(max_length=200, unique=True)
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
    available_slots = models.IntegerField()
    attendance = models.ManyToManyField(User, related_name='workshop_attendees', blank=True)


class DigitalProduct(Product):
    file = models.FileField(upload_to='media/student_resources/')
    pages = models.IntegerField()
    owners = models.ManyToManyField(User, related_name='resource_owners', blank=True)
