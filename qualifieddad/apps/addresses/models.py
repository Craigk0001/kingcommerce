from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Address(models.Model):
    company_name                = models.CharField(max_length = 64, null=True, blank=True)
    address_line1               = models.CharField(max_length = 100, null=True)
    city                        = models.CharField(max_length = 64, null=True)
    state                       = models.CharField(max_length = 64, null=True)
    country                     = models.CharField(max_length = 64, null=True)
    postcode                    = models.CharField(max_length = 64, null=True)
    created                     = models.DateTimeField(auto_now_add = True)
    updated                     = models.DateTimeField(auto_now = True)
    user                        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_address")
    full_name                   = models.CharField(max_length = 64, null=True)
    phone                       = models.CharField(max_length = 64, null=True)
    additional_instructions     = models.CharField(max_length = 500, null=True, blank=True)
    call_box                    = models.CharField(max_length = 10, null=True, blank=True)


    def __str__(self):
            return self.address_line1
