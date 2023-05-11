from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Workshop, DigitalProduct, Product
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from .forms import WorkshopForm, DigitalProductForm


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
    workshop_id = str(workshop.id)
    in_bag = False
    if request.session.get('bag', {}):
        bag = list(request.session['bag'])
    else:
        bag = ''
    if workshop_id in bag:
        in_bag = True

    context = {
        'workshop': workshop,
        'in_bag': in_bag,
        'bag': bag,
        'workshop_id': workshop_id,
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
    product_id = str(digital_product.id)
    in_bag = False
    if request.session.get('bag', {}):
        bag = list(request.session['bag'])
    else:
        bag = ''
    if product_id in bag:
        in_bag = True

    context = {
        'digital_product': digital_product,
        'in_bag': in_bag,
    }

    return render(request, 'products/digital_product_detail.html', context)


def add_workshop(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_workshop'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = WorkshopForm()
    template = 'products/add_workshop.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_digital_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = DigitalProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_digital_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = DigitalProductForm()
    template = 'products/add_digital_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
