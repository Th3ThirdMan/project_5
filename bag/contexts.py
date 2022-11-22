from django.conf import settings
from decimal import Decimal


def bag_contents(request):
    
    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_SHIPPING_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE/100)

    else:
        delivery = 0


    grand_total = delivery + total


    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context


