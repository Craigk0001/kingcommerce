from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from apps.addresses.forms import AddAddressForm
from apps.addresses.models import Address
# Create your views here.

#CREATE
@login_required
class AddAddressView(TemplateView):
    template_name = 'addresses/add_address.html'

    def get(self, request):
        form = AddAddressForm()
        args = {'form' : form,}
        return render(request, self.template_name, args)


    def post(self, request):
        form = AddAddressForm(request.POST)
        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.user = request.user

            new_address.save()
            return redirect('core_pages:home')

        args = {'form':form,}
        return render(request, self.template_name, args)

@login_required
def add_address_to_user(request, template_name='addresses/add_address.html'):
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

@login_required
def address_delete(request, pk=None):
    address = get_object_or_404(Address, pk=pk)
    user = request.user
    if user == address.user:
        address.delete()
        return redirect('user_account:user_address')

    return redirect('core_pages:home')

@login_required
def address_update(request, pk=None, template_name='addresses/add_address.html'):
    address = get_object_or_404(Address, pk=pk)
    user = request.user
    if request.user == address.user:
        form = AddAddressForm(request.POST or None, request.FILES or None, instance=address)
        if request.POST and form.is_valid():
            form.save()
            return redirect('user_account:user_address')

        args = {'form': form, 'address':address}
        return render(request, template_name, args)

    return redirect('core_pages:home')
