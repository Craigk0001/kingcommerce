from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class EstimatedDelivery(models.Model):
    name            = models.CharField(max_length = 64, null=True)
    days_minimum    = models.IntegerField(null=True, blank=True)
    days_maximum    = models.IntegerField(null=True, blank=True)
    #shipping_delivery_method - REVERSE FOREIGN KEY to Shipping_Method

    def __str__(self):
        return self.name

class ShippingZone(models.Model):
    name            = models.CharField(max_length = 64, null=True)
    regions         = models.CharField(max_length = 64, null=True)

    def __str__(self):
        return self.name

class ShippingMethod(models.Model):
    FLAT_RATE       = 'Flat Rate' #Lets you charge a fixed rate for shipping.
    FREE_SHIPPING   = 'Free Shipping' #Free shipping is a special method which can be triggered with coupons and minimum spends.
    LOCAL_PICKUP    = 'Local Pickup' #Allow customers to pick up orders themselves. By default, when using local pickup store base taxes will apply regardless of customer address.
    TYPE = (
        (FLAT_RATE, 'Flat Rate'),
        (FREE_SHIPPING, 'Free Shipping'),
        (LOCAL_PICKUP, 'Local Pickup'),
        )
    type            = models.CharField(max_length = 200, choices=TYPE, default=FLAT_RATE)
    name            = models.CharField(max_length = 64, null=True) #This controls the name users will see during check-out
    NOTHING = 'N/A' #No exclusion to free shipping.
    COUPON = 'Free Shipping Coupon' #Free shipping coupon required.
    MINIMUM_ORDER = 'Minimum Order Amount' #Minimum order amount required to activate coupon
    MINIMUM_ORDER_OR_COUPON = 'Minimum Order Amount OR Coupon'
    MINIMUM_ORDER_AND_COUPON = 'Minimum Order Amount AND Coupon'
    FREE_SHIPPING_REQUIREMENTS = (
        (NOTHING, 'N/A'),
        (COUPON, 'Free Shipping Coupon'),
        (MINIMUM_ORDER, 'Minimum Order Amount'),
        (MINIMUM_ORDER_OR_COUPON, 'Minimum Order Amount OR Coupon'),
        (MINIMUM_ORDER_AND_COUPON, 'Minimum Order Amount AND Coupon'),
        )
    free_shipping_requirements  = models.CharField(max_length = 200, choices=FREE_SHIPPING_REQUIREMENTS, default=NOTHING)
    minimum_order               = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    NONE = 'None' #No tax required on shipping
    TAXABLE = 'Taxable' #Tax required on shipping
    TAX_STATUS = (
        (NONE, 'None'),
        (TAXABLE, 'Taxable'),
        )
    tax_status              = models.CharField(max_length = 200, choices=TAX_STATUS, default=NONE)
    local_pickup_cost       = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) #Optional cost for local pick-up
    flat_rate_calculation   = models.CharField(max_length = 200, null=True, blank=True) #Enter a cost (excl. tax) or sum, e.g. 10.00 * [qty]. Use [qty] for the number of items, [cost] for the total cost of items, and [fee percent="10" min_fee="20" max_fee=""] for percentage based fees.
    PER_ITEM = 'Per item' #Charge shipping for each shipping class
    HIGHEST = 'Most expensive shipping category' #Charge shipping for most expensize shipping class only
    CALCULATION_TYPE = (
        (PER_ITEM, 'Per item'),
        (HIGHEST, 'Most expensive shipping category'),
        )
    calculation_type        = models.CharField(max_length = 200, choices=CALCULATION_TYPE, default=PER_ITEM)
    zone                    = models.ForeignKey(ShippingZone, on_delete=models.CASCADE, related_name='shipping_method')
    estimated_delivery      = models.ForeignKey(EstimatedDelivery, on_delete=models.CASCADE, related_name='shipping_delivery_method')

    def __str__(self):
        return self.name

class ShippingClass(models.Model):
    name = models.CharField(max_length = 64, null=True) #This controls the name users will see during check-out
    slug = models.SlugField(unique=True, max_length=40)
    description = models.CharField(max_length = 100, null=True) #For admin reference
    shipping_method = models.ManyToManyField(ShippingMethod, blank=True, through='MethodClass', related_name='shipping_class')

    def __str__(self):
        return self.name

class MethodClass(models.Model):
    flat_rate_calculation = models.CharField(max_length = 200, null=True, blank=True) #Enter a cost (excl. tax) or sum, e.g. 10.00 * [qty]. Use [qty] for the number of items, [cost] for the total cost of items, and [fee percent="10" min_fee="20" max_fee=""] for percentage based fees.
    shipping_class = models.ForeignKey(ShippingClass, on_delete=models.CASCADE, related_name='method_class')
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.CASCADE, related_name='method_class')

    def __str__(self):
        return self.flat_rate_calculation
