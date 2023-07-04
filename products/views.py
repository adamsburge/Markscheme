import os
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Workshop, DigitalProduct, Product, Updates
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.conf import settings
from django.db.models import Q
from .forms import WorkshopForm, DigitalProductForm, ProductNewsUpdateForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
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
    productupdates = Updates.objects.filter(product=workshop)
    user_exists = workshop.attendance.filter(
        username=request.user.username).exists()
    if request.user.is_authenticated:
        not_authenticated = False
    else:
        not_authenticated = True
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
        'productupdates': productupdates,
        'user_exists': user_exists,
        'not_authenticated': not_authenticated,
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
    productupdates = Updates.objects.filter(product=digital_product)
    user_exists = digital_product.owners.filter(
        username=request.user.username).exists()
    if 'USE_AWS' in os.environ:
        filelink = 'https://markscheme.s3.amazonaws.com/media/' + str(
            digital_product.file)
    else:
        filelink = "http://127.0.0.1:8000/media/" + str(digital_product.file)
    if request.user.is_authenticated:
        not_authenticated = False
    else:
        not_authenticated = True
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
        'productupdates': productupdates,
        'filelink': filelink,
        'user_exists': user_exists,
        'not_authenticated': not_authenticated,
    }

    return render(request, 'products/digital_product_detail.html', context)


@login_required
def add_workshop(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('workshop_detail', args=[product.slug]))
        else:
            messages.error(
                request, 'Failed to add product. Please\
                      ensure the form is valid.')
    else:
        form = WorkshopForm()
    template = 'products/add_workshop.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_digital_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DigitalProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(
                reverse('digital_product_detail', args=[product.slug]))
        else:
            messages.error(
                request, 'Failed to add product. \
                    Please ensure the form is valid.')
    else:
        form = DigitalProductForm()
    template = 'products/add_digital_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_workshop(request, slug):
    """ Edit a workshop in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product_form = WorkshopForm(
            request.POST, request.FILES, instance=product)
        update_form = ProductNewsUpdateForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            update_form.save()
            if update_form.cleaned_data['major_update']:
                print('Success! The box was checked!')
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('workshop_detail', args=[product.slug]))
        else:
            messages.error(
                request, 'Failed to update product. \
                    Please ensure the form is valid.')
    else:
        product_form = WorkshopForm(instance=product)
        update_form = ProductNewsUpdateForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_workshop.html'
    context = {
        'product_form': product_form,
        'update_form': update_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_digital_product(request, slug):
    """ Edit a digital product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product_form = DigitalProductForm(
            request.POST, request.FILES, instance=product)
        update_form = ProductNewsUpdateForm(request.POST, request.FILES)
        if product_form.is_valid() and update_form.is_valid():
            product_form.save()
            update_form.save()
            if update_form.cleaned_data['major_update']:
                # A further development could be to add an email
                # sent to all attendees of the workshop or owners
                # of the product.
                print('This is a major update')
            messages.success(request, 'Successfully updated product!')
            return redirect(
                reverse('digital_product_detail', args=[product.slug]))
        else:
            messages.error(request, 'Failed to update product. \
                           Please ensure the form is valid.')
    else:
        product_form = DigitalProductForm(instance=product)
        update_form = ProductNewsUpdateForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_digital_product.html'
    context = {
        'product_form': product_form,
        'update_form': update_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, slug):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, slug=slug)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
