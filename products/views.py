from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Workshop, DigitalProduct, Product
from django.conf import settings
from django.db.models import Q


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def workshops(request):
    """ A view to show all workshops | The basic structure of this came from
    Code Institute's Boutique Ado Project and has been modified here to fit
     this project """

    workshops = Product.objects.filter(Q(instance_of=Workshop))

    context = {
        'workshops': workshops,
    }

    return render(request, 'products/workshops.html', context)


def workshop_detail(request, slug):
    """ A view to show all workshops | The basic structure of this came from
    Code Institute's Boutique Ado Project and has been modified here to fit
     this project """

    workshop = get_object_or_404(Product, slug=slug)

    context = {
        'workshop': workshop,
    }

    return render(request, 'products/workshop_detail.html', context)


def digital_products(request):
    """ A view to show all workshops | The basic structure of this came from
    Code Institute's Boutique Ado Project and has been modified here to fit
     this project """

    digital_products = Product.objects.filter(Q(instance_of=DigitalProduct))

    context = {
        'digital_products': digital_products,
    }

    return render(request, 'products/digital_products.html', context)


def digital_product_detail(request, slug):
    """ A view to show all workshops | The basic structure of this came from
    Code Institute's Boutique Ado Project and has been modified here to fit
     this project """

    digital_product = get_object_or_404(Product, slug=slug)

    context = {
        'digital_product': digital_product,
    }

    return render(request, 'products/digital_product_detail.html', context)
