from .cart import Cart
def cart_total(request):
    return {'cart_item_count': len(Cart(request).cart)}
