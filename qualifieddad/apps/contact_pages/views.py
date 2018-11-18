from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from apps.contact_pages.forms import (
    contactForm,
)

# Create your views here.
def contact_us(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from Qualified Dad'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = 'Thanks for you email, speak soon!'
        confirm_message = 'We will get right back to you.'
        form = None

    args = {'title':title, 'confirm_message':confirm_message, 'form':form, }
    template = 'contact_pages/contact_us.html'
    return render(request,template,args)

def sign_up(request):
    args = {}
    template = 'contact_pages/sign_up.html'
    return render(request,template,args)
