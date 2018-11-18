from django.contrib.auth.models import User
from django.db import models

from apps.product_catalogue.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name=("Owner"), related_name='cart')
    #cart_selection = REVERSE OF CartSelection
    OPEN, MERGED, SAVED, FROZEN, SUBMITTED = (
        "Open", "Merged", "Saved", "Frozen", "Submitted")
    STATUS_CHOICES = (
        (OPEN, ("Open - currently active")),
        (MERGED, ("Merged - superceded by another basket")),
        (SAVED, ("Saved - for items to be purchased later")),
        (FROZEN, ("Frozen - the basket cannot be modified")),
        (SUBMITTED, ("Submitted - has been ordered at the checkout")),
    )
    status = models.CharField(
        ("Status"), max_length=128, default=OPEN, choices=STATUS_CHOICES)
    # coupon = models.ManyToManyField(Coupon, verbose_name=("Coupons"), blank=True)
    created = models.DateTimeField(("Date created"), auto_now_add=True)
    date_merged = models.DateTimeField(("Date merged"), null=True, blank=True)
    date_submitted = models.DateTimeField(("Date submitted"), null=True, blank=True)

    def _get_sub_total(self):
        sub_total = 0
        for item in self.cart_selection.all():
            sub_total += (item.product.regular_price * item.quantity)
        return sub_total
    sub_total = property(_get_sub_total)

    def _get_discount_total(self):
        discount_total = 0
        for item in self.cart_selection.all():
            if item.product.sale_price:
                discount_total += (item.product.regular_price - item.product.sale_price) * (item.quantity)
        return discount_total
    discount_total = property(_get_discount_total)

    def _get_grand_total(self):
        grand_total = 0
        for item in self.cart_selection.all():
            if item.product.sale_price:
                grand_total += (item.product.sale_price * item.quantity)
            elif item.product.regular_price:
                grand_total += (item.product.regular_price * item.quantity)
        return grand_total
    grand_total = property(_get_grand_total)

    def _get_item_count(self):
        quantity_count = 0
        for item in self.cart_selection.all():
            quantity_count += item.quantity
        return quantity_count
    item_count = property(_get_item_count)

class CartSelection(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_selection',
        verbose_name=("Cart"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_selection',
        verbose_name=("Product"))
    quantity = models.PositiveIntegerField(('Quantity'), default=1)

    def _get_total_cost(self):
        if self.product.sale_price:
            return self.product.sale_price * self.quantity
        else:
            return self.product.regular_price * self.quantity
    total_cost = property(_get_total_cost)

    def _get_total_savings(self):
        if self.product.sale_price:
            return (self.product.regular_price - self.product.sale_price) * (self.quantity)
        else:
            return 0
    total_savings = property(_get_total_savings)

    def _get_recommended_retail(self):
        if self.product.sale_price:
            return self.product.regular_price * self.quantity
    recommended_retail = property(_get_recommended_retail)
