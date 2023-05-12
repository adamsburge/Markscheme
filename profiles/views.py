from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm, SuperuserProfileForm
from checkout.models import Order
from products.models import Workshop


def profile(request):
    """ Display the user's profile. """
    # Code here taken from Boutique Ado
    profile = get_object_or_404(UserProfile, user=request.user)
    workshops_i_teach = Workshop.objects.filter(host_creators=request.user)

    if request.method == 'POST':
        if request.user.is_superuser:
            form = SuperuserProfileForm(request.POST, instance=profile)
        else:
            form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        if request.user.is_superuser:
            form = SuperuserProfileForm(instance=profile)
        else:
            form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'workshops_i_teach': workshops_i_teach
    }

    return render(request, template, context)


def order_history(request, order_number):
    ''' Display order history on profile page for nonsuperuser '''
    # Code here taken from Boutique Ado
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
