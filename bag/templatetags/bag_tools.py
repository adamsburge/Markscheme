from django import template

# Bag tools template tag was taken from Code Institute's
# Boutique Ado project
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
