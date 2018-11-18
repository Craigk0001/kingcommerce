from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Min, Max
from django.db.models.signals import pre_save
from django.utils.text import slugify

from apps.shipping.models import ShippingMethod
from apps.images.models import Image

# Create your models here.
def category_upload_location(instance,filename):
    return "category/%s/%s" %(instance.id, filename)
def variation_upload_location(instance,filename):
    return "variation/%s/%s" %(instance.id, filename)
def product_upload_location(instance,filename):
    return "product/%s/%s" %(instance.id, filename)

class ProductPost(models.Model):
    title               = models.CharField(max_length = 64, blank=True)
    description         = models.CharField(max_length = 1000, blank=True)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    created             = models.DateTimeField(auto_now = True)
    updated             = models.DateTimeField(auto_now = True)
    product_images      = models.ManyToManyField(Image, through="GalleryImage", blank=True, related_name='product_post')
    #gallery_image      = REVERSE OF GalleryImage
    #product_category   = REVERSE OF Category
    #review             = REVERSE OF Review
    #attribute          = REVERSE OF Attribute
    #attribute_value    = REVERSE OF AttributeValue
    #products           = REVERSE OF Product
    shipping_method     = models.ForeignKey(ShippingMethod, on_delete=models.CASCADE, related_name='product')
    merchant_notes      = models.CharField(max_length = 800, null=True, blank=True)
    enable_comments     = models.BooleanField(default=True)
    enable_reviews      = models.BooleanField(default=True)
    google_prohibited   = models.BooleanField(default=False)
    additional          = models.CharField(max_length = 1000, null=True, blank=True)
    staff_notes         = models.CharField(max_length = 200, null=True, blank=True)

    DRAFT, ACTIVE, PENDING, DISCONTINUED = 'Draft', 'Active', 'Pending Review', 'Discontinued'
    STATUS = (
        (DRAFT, 'Draft'),
        (ACTIVE, 'Active'),
        (PENDING, 'Pending Review'),
        (DISCONTINUED, 'Discontinued'),
        )
    status              = models.CharField(max_length = 200, choices=STATUS, default=ACTIVE)

    PUBLIC, PASSWORD = 'Public', 'Password Protected'
    VISIBILITY = (
        (PUBLIC, 'Public'),
        (PASSWORD, 'Password Protected'),
        )
    visibility          = models.CharField(max_length = 200, choices=VISIBILITY, default=PUBLIC)

    def _get_one_stars(self):
        return self.review.filter(rating=1).count()
    one_star = property(_get_one_stars)

    def _get_one_percentage(self):
        return self.review.filter(rating=1).count() / self.review.count() * 100
    one_percentage = property(_get_one_percentage)

    def _get_two_stars(self):
        return self.review.filter(rating=2).count()
    two_star = property(_get_two_stars)

    def _get_two_percentage(self):
        return self.review.filter(rating=2).count() / self.review.count() * 100
    two_percentage = property(_get_two_percentage)

    def _get_three_stars(self):
        return self.review.filter(rating=3).count()
    three_star = property(_get_three_stars)

    def _get_three_percentage(self):
        return self.review.filter(rating=3).count() / self.review.count() * 100
    three_percentage = property(_get_three_percentage)

    def _get_four_stars(self):
        return self.review.filter(rating=4).count()
    four_star = property(_get_four_stars)

    def _get_four_percentage(self):
        return self.review.filter(rating=4).count() / self.review.count() * 100
    four_percentage = property(_get_four_percentage)

    def _get_five_stars(self):
        return self.review.filter(rating=5).count()
    five_star = property(_get_five_stars)

    def _get_five_percentage(self):
        return self.review.filter(rating=5).count() / self.review.count() * 100
    five_percentage = property(_get_five_percentage)

    def _get_average_stars(self):
            return ((self.five_star*5)+(self.four_star*4)+(self.three_star*3)+(self.two_star*2)+(self.one_star*1))/(self.review.count())
    average_star_percentage = property(_get_average_stars)

    def _get_products(self):
        return self.products.count()
    number_of_products = property(_get_products)

    def _get_regular_price_range(self):
        return self.products.aggregate(min=Min('regular_price'), max=Max('regular_price'))
    regular_price_range = property(_get_regular_price_range)

    def _get_sale_price_range(self):
        return self.products.aggregate(min=Min('sale_price'), max=Max('sale_price'))
    sale_price_range = property(_get_sale_price_range)

    def _max_savings(self):
        max_savings = []
        for product in self.products.all():
            if product.sale_price:
                max_savings.append(product.regular_price-product.sale_price)
            else:
                max_savings.append(0)
        return max(max_savings)
    max_savings = property(_max_savings)

    def _max_discount(self):
        max_discount = []
        for product in self.products.all():
            if product.sale_price:
                max_discount.append((product.regular_price-product.sale_price)/(product.regular_price)*(100))
            else:
                max_discount.append(0)
        return max(max_discount)
    max_discount = property(_max_discount)

    def __str__(self):
        return self.title

class Product(models.Model):
    #EVERY PRODUCT IS A VARIANT
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    created             = models.DateTimeField(auto_now = True)
    updated             = models.DateTimeField(auto_now = True)
    slug                = models.SlugField(unique=True, max_length=40)
    name                = models.CharField(max_length = 64, blank=True)
    regular_price       = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sale_price          = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    product_post        = models.ForeignKey(ProductPost, on_delete=models.CASCADE, blank=True, null=True, related_name='products')
    product_image       = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, related_name='product')
    parent_product      = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child_product')
    #child_product      = REVERSE of parent_product
    #cart_selection     = REVERSE OF CartSelection
    #variant            = REVERSE OF Variant
    stock               = models.IntegerField(null=True, blank=True) #Leave blank if not monitored or same as parent
    weight              = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight_unit         = models.CharField(max_length = 64, null=True, blank=True) #KG or Pound
    height              = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    length              = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    width               = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    SKU                 = models.CharField(max_length = 64, null=True, blank=True) #Leave blank if not monitored or same as parent
    is_donation         = models.BooleanField(default=False)
    external_link       = models.CharField(max_length = 64, null=True, blank=True) #Affiliate products
    external_link_text  = models.CharField(max_length = 64, null=True, blank=True) #To replace 'Add to Cart'
    attribute_value     = models.ForeignKey('AttributeValue', on_delete=models.CASCADE, blank=True, null=True, related_name='product')
    purchase_limit      = models.IntegerField(null=True, blank=True) #Leave blank if no limit
    NEW_TAB, NEW_WINDOW, DIRECT = 'New Tab', 'New Window', 'Direct'
    EXTERNAL_LINK_TARGET = (
        (NEW_TAB, 'New Tab'),
        (NEW_WINDOW, 'New Window'),
        (DIRECT, 'Direct'),
        )
    external_link_target = models.CharField(max_length = 200, choices=EXTERNAL_LINK_TARGET, default=NEW_TAB)
    engraved            = models.BooleanField(default=False) #Personalised Message
    can_have_images     = models.BooleanField(default=False) #Personalised Images
    YES, NO, YES_NO = 'Allow', 'Do not allow', 'Allow, but notify customer'
    BACK_ORDERS = (
        (YES, 'Allow'),
        (NO, 'Do not allow'),
        (YES_NO, 'Allow, but notify customer'),
        )
    back_orders         = models.CharField(max_length = 200, choices=BACK_ORDERS, default=YES)

    def _get_savings(self):
        if self.sale_price:
            return int(self.regular_price - self.sale_price)
        return 0
    savings = property(_get_savings)

    def _get_discount(self):
        return self.savings / self.regular_price * 100
    discount = property(_get_discount)

    def __str__(self):
        return self.name

class Options(models.Model):
    name            = models.CharField(max_length = 64, null=True)
    staff_name      = models.CharField(max_length = 64, null=True)
    visible         = models.BooleanField(default=True)
    variations      = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Values(models.Model):
    name            = models.CharField(max_length = 64, null=True)
    option          = models.ForeignKey(Options, on_delete=models.CASCADE, related_name='option_value')
    def __str__(self):
        return self.name

class Category(models.Model):
    name            = models.CharField(max_length = 64, null=True)
    description     = models.CharField(max_length = 500, null=True, blank=True)
    image           = models.ImageField(upload_to=category_upload_location, null=True, blank=True)
    products        = models.ManyToManyField(ProductPost, blank=True, related_name='product_category')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_category')
    slug            = models.SlugField(unique=True,
                            max_length=250,
                            help_text='A "slug" is a unique URL-friendly title for an object.')

    def __str__(self):
        return str(self.name)

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_reciever, sender=Product)

class GalleryImage(models.Model):
    priority        = models.IntegerField(null=True, blank=True)
    image           = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='gallery_post')
    product         = models.ForeignKey(ProductPost, on_delete=models.CASCADE, related_name='gallery_image')

    class Meta:
        ordering = ['priority']

    def __str__(self):
        return str(self.priority)

class Review(models.Model):

    content         = models.CharField(max_length = 200, null=True, blank=True)
    detail          = models.CharField(max_length = 600, null=True, blank=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    product         = models.ForeignKey(ProductPost, on_delete=models.CASCADE, related_name='review')
    created         = models.DateTimeField(auto_now = True)
    rating          = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    help            = models.ManyToManyField(User, blank=True, through="ReviewHelpfulness", related_name='review_helpful')
    # user_review   = OTHER SIDE OF FOREIGN KEY
    verified        = models.BooleanField(default=False)
    # review_images = models.ManyToManyField(Image, through="ReviewImage", blank=True, related_name='review')
    # helpful       = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # not_helpful   = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # helpful_add   = models.PositiveIntegerField(null=True, blank=True)

    def _get_helpfulness_count(self):
        return self.user_review.filter(helpful=True).count()
    helpfulness_count = property(_get_helpfulness_count)

class ReviewHelpfulness(models.Model):
    helpful         = models.BooleanField(default=False)
    created         = models.DateTimeField(auto_now = True)
    review          = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='user_review')
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user')

    class Meta:
        ordering    = ['created']

    def __str__(self):
        return str(self.created)

class Attribute(models.Model):
    name            = models.CharField(max_length = 200, null=True, blank=True)
    slug            = models.SlugField(unique=True,
                            max_length=250,
                            help_text='A "slug" is a unique URL-friendly title for an object.')
    description     = models.CharField(max_length = 500, null=True, blank=True)
    #attribute_value = REVERSE OF AttributeValue
    #variant         = REVERSE OF Variant
    product_post    = models.ManyToManyField(ProductPost, blank=True, related_name='attribute')
    NAME = 'Name'
    PRIORITY = 'Priority'
    REVERSE_NAME = 'Reverse name'
    SORT_ORDER = (
        (NAME, 'NAME'),
        (PRIORITY, 'PRIORITY'),
        (REVERSE_NAME, 'REVERSE_NAME'),
        )
    sort_order     = models.CharField(max_length = 200, choices=SORT_ORDER, default=NAME)

    def __str__(self):
        return self.name

class AttributeValue(models.Model):
    name            = models.CharField(max_length = 200, null=True, blank=True)
    description     = models.CharField(max_length = 500, null=True, blank=True)
    slug            = models.SlugField(unique=True,
                            max_length=250,
                            help_text='A "slug" is a unique URL-friendly title for an object.')
    priority        = models.IntegerField(null=True, blank=True)
    attribute       = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True, blank=True, related_name='attribute_value')
    product_post    = models.ManyToManyField(ProductPost, blank=True, related_name='attribute_value')
    #product         = REVERSE OF Product
    #variant         = REVERSE OF Variant

    def __str__(self):
        return self.name

class Variation(models.Model):
    attribute       = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True, blank=True, related_name='variant')
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, null=True, blank=True, related_name='variant')
    product         = models.ManyToManyField(Product, blank=True, related_name='variant')


    def __str__(self):
        return str(self.attribute)
