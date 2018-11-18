from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from apps.cart.models import Cart, CartSelection
from apps.product_catalogue.models import ProductPost

# Create your views here.

# def cart(request, pk=None, template_name='cart/cart.html'):
#     cart = get_object_or_404(Cart, pk=pk)
#     args = {'cart':cart,}
#     return render(request,template_name,args)

# @login_required
def cart(request, template_name='cart/cart.html'):
    user = request.user
    cart = user.cart.order_by('created').first()
    product_posts = ProductPost.objects.all()

    args = {'user':user, 'product_posts':product_posts, 'cart':cart}
    return render(request,template_name,args)


def add_item_to_cart(request, pk=None):
    user = request.user

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
        print("something")

    request.session['cart_id']

    form = AddItemForm(request.POST or None, initial={'cart':the_id})
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.user = request.user
        new_item.save()
        form.save_m2m()
        return redirect('cart:cart')

    args = {'form': form, 'user':user}
    return render(request, template_name, args)


def item_delete(request, pk=None):
    item = get_object_or_404(CartSelection, pk=pk)
    user = request.user
    if user == item.cart.user:
        item.delete()
        return redirect('cart:cart')
    return redirect('core_pages:home')
