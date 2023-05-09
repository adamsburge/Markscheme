from django.conf import settings


def bag_contents(request):
    # The basis of this context comes from Code Institute's Boutique Ado
    # It has been modified here for the purpose of this project
    bag_items = []
    total = 0
    product_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
