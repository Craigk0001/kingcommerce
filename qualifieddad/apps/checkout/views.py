from django.shortcuts import render

from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings

from apps.addresses.forms import AddAddressForm

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def checkout(request, template_name='checkout/checkout.html'):
    user = request.user

    form = AddAddressForm(request.POST or None, initial={'user':user.pk})
    if form.is_valid():
        new_address = form.save(commit=False)
        new_address.user = request.user
        new_address.save()
        form.save_m2m()
        return redirect('user_account:user_address')

    args = {'form': form, 'user':user}
    return render(request, template_name, args)

def test(request):
    args = {}
    template = 'checkout/untitled.html'
    return render(request,template,args)
