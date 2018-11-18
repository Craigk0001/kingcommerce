from django.shortcuts import render, redirect, get_object_or_404
from apps.product_catalogue.models import ProductPost, Product, Category, Review, Attribute
from apps.comments.models import Comment
from apps.cart.forms import AddItemForm
from apps.product_catalogue.forms import ReviewForm, ReviewHelpfulnessForm
from django.contrib.contenttypes.models import ContentType
from django.views.generic import RedirectView
from django.core.paginator import Paginator
from django.db.models import Min, Max

# Create your views here.
def product_overview(request, pk=None, template_name='product_catalogue/product.html'):
    product_post = get_object_or_404(ProductPost, pk=pk)
    products = product_post.products.all()
    user = request.user
    form = AddItemForm(request.POST or None)
    if form.is_valid():
        new_cart_item = form.save(commit=False)
        new_cart_item.save()
        form.save_m2m()
        return redirect('cart:cart')


    savings_price_min = product_post.products.order_by('sale_price')


    #COMMENTS
    content_type_comment = ContentType.objects.get_for_model(ProductPost)
    obj_id_comment = product_post.pk
    comments = Comment.objects.filter(content_type=content_type_comment, object_id=obj_id_comment).order_by('-created')

    ##REVIEWS PAGINATOR
        ##STAR RATING FILTER
    star_rating = request.GET.get('star_rating')
    if star_rating:
        reviews = product_post.review.all().filter(rating=star_rating)
    else:
        reviews = product_post.review.all()
    paginator = Paginator(reviews, 3)
    page = request.GET.get('review_page')
    reviews = paginator.get_page(page)

    attributes = Attribute.objects.all()

    args = {'savings_price_min':savings_price_min, 'product_post':product_post,
    'products':products, 'comments':comments, 'reviews':reviews,
    'star_rating':star_rating, 'attributes':attributes, 'form':form,}
    return render(request,template_name,args)

def category(request, pk=None, template_name='product_catalogue/category.html'):
    category = get_object_or_404(Category, pk=pk)
    args = {'category':category,}
    return render(request,template_name,args)

# def helpful(request, pk=None):
#     new_like, created = Like.objects.get_or_create(user=request.user, pk=product)
#     if not created:
#         # the user already liked this picture before
#     else:
#         # oll korrekt

def review(request, pk=None, template_name='product_catalogue/review.html'):
    review = get_object_or_404(Review, pk=pk)
    form = ReviewForm(request.POST or None, request.FILES or None, instance=review)
    if request.POST and form.is_valid():
        form.save()
        return redirect('core_pages:home')
    args = {'review':review, 'form':form}
    return render(request,template_name,args)

def review_helpfulness(request, pk=None, template_name='product_catalogue/review_helpfulness.html'):
    review = get_object_or_404(Review, pk=pk)
    form = ReviewHelpfulnessForm(request.POST or None, request.FILES or None, instance=review, initial={'review':review.pk, 'user':request.user, 'helpful':True})
    if request.POST and form.is_valid():
        form.save()
        return redirect('core_pages:home')
    args = {'review':review, 'form':form}
    return render(request,template_name,args)
