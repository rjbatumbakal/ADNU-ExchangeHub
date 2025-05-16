from django.shortcuts import render, redirect
from .models import WishlistItem, Item  # Make sure to import Item
from .forms import AddToWishlistForm
from ExchangeHub.models import Item
from django.views.decorators.http import require_POST

def get_user_or_session_key(request):
    return request.user if request.user.is_authenticated else request.session.session_key


def wishlist_view(request):
    if not request.session.session_key:
        request.session.create()

    user_or_session = get_user_or_session_key(request)

    if request.method == 'POST':
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            try:
                item = Item.objects.get(name__iexact=item_name)
                WishlistItem.objects.get_or_create(user=user_or_session, item=item)
            except Item.DoesNotExist:
                form.add_error('item_name', 'Item not found.')
    else:
        form = AddToWishlistForm()

    raw_items = WishlistItem.objects.filter(**get_user_or_session_filter(request)).select_related('item')

    valid_items = [entry for entry in raw_items if getattr(entry.item, 'id', None)]

    return render(request, 'wishlist/wishlist.html', {
        'form': form,
        'wishlist_items': valid_items
    })


def add_to_wishlist(request):
    if not request.session.session_key:
        request.session.create()

    user_or_session = get_user_or_session_key(request)

    if request.method == 'POST':
        form = AddToWishlistForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            try:
                item = Item.objects.get(name__iexact=item_name)
                WishlistItem.objects.get_or_create(user=user_or_session, item=item)
            except Item.DoesNotExist:
                pass  # Optionally handle this case
    return redirect('wishlist:wishlist')


def remove_from_wishlist(request, item_id):
    user_or_session = get_user_or_session_key(request)
    WishlistItem.objects.filter(user=user_or_session, item_id=item_id).delete()
    return redirect('wishlist:wishlist')


def add_wishlist_to_cart(request, item_id):
    if not request.session.session_key:
        request.session.create()

    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart

    user_or_session = get_user_or_session_key(request)
    WishlistItem.objects.filter(user=user_or_session, item_id=item_id).delete()
    return redirect('wishlist:wishlist') 

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = 0

    for item_id, quantity in cart.items():
        try:
            item = Item.objects.get(id=item_id)
            total_price = item.price * quantity
            cart_items.append({
                'item': item,
                'quantity': quantity,
                'total_price': total_price
            })
            subtotal += total_price
        except Item.DoesNotExist:
            continue

    return render(request, 'wishlist/cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal
    })

@require_POST
def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart.pop(str(item_id), None)
    request.session['cart'] = cart
    return redirect('wishlist:view_cart')

    
def get_user_or_session_filter(request):
    if request.user.is_authenticated:
        return {'user': request.user}
    else:
        return {'session_key': request.session.session_key}

