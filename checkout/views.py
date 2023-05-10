from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# The base template for this admin page came from
# Code Institute's Boutique Ado project and has been modified here


from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        # The code below could be used if I decide to add messages
        # messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
