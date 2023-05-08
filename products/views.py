from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Workshop, StudentResource, Product
from django.conf import settings
from django.db.models import Q


def workshops(request):
    """ A view to show all workshops | The basic structure of this came from
    Code Institute's Boutique Ado Project and has been modified here to fit
     this project """

    workshops = Product.objects.filter(Q(instance_of=Workshop))

    context = {
        'workshops': workshops,
    }

    return render(request, 'products/workshops.html', context)
