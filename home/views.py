from django.shortcuts import render
from profiles.models import UserProfile

# Create your views here.


def index(request):
    """ Returns Index page """
    return render(request, 'home/index.html')


def about(request):
    """ Returns about page """
    return render(request, 'home/about.html')


def staff(request):
    """ A view to show all the staff bios """

    staff = UserProfile.objects.all()

    context = {
        'staff': staff,
    }

    return render(request, 'home/staff.html', context)
