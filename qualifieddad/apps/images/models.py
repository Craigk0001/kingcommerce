from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def image_upload_location(instance,filename):
    return "image/%s/%s" %(instance.id, filename)

class Image(models.Model):
    title       = models.CharField(max_length = 50, null=True, blank=True)
    alt_text    = models.CharField(max_length = 120, null=True, blank=True)
    description = models.CharField(max_length = 300, null=True, blank=True)
    slug        = models.SlugField(unique=True, max_length=250)
    #FILE MANAGEMENT
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    created     = models.DateTimeField(auto_now_add = True)
    updated     = models.DateTimeField(auto_now = True)
    #IMAGE
    image       = models.ImageField(upload_to=image_upload_location, null=True, blank=True)
    #product_post   = REVERSE OF ProductPost
    #gallery_post   = REVERSE OF GalleryImage

    def __str__(self):
        return str(self.title)
