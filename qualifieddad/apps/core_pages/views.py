from django.shortcuts import render
from apps.product_catalogue.models import ProductPost

# Create your views here.

def home(request, template_name = 'core_pages/home.html'):
    product_posts = ProductPost.objects.all()

    args = {'product_posts':product_posts,}
    return render(request,template_name,args)

def about_us(request):
    args = {}
    template = 'core_pages/about_us.html'
    return render(request,template,args)
