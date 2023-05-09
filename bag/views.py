from django.shortcuts import render


def view_bag(request):
    """ A view that renders the bag contents page | This view was taken
    from Code Institute's Boutique Ado project """

    return render(request, 'bag/bag.html')
