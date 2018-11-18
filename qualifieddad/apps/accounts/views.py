from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from apps.accounts.forms import ChangeNameForm
from apps.addresses.models import Address

@login_required
def user_profile(request):
    user = request.user
    args = {'user':user}
    template = 'profile/profile.html'
    return render(request,template,args)


class UserAddressView(TemplateView):
    template_name = 'profile/addresses.html'

    def get(self, request):
        user = request.user

        args = {'user':user,}
        return render(request, self.template_name, args)

class UserSecurityView(TemplateView):
    template_name = 'profile/security.html'

    def get(self, request):
        user = request.user

        args = {'user':user,}
        return render(request, self.template_name, args)

def change_name_view(request, template_name = 'profile/change_name.html'):
    if request.method == 'POST':
        form = ChangeNameForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('user_account:security')
    else:
        form = ChangeNameForm(instance=request.user)
        args = {'form':form}
        return render(request, template_name, args)
