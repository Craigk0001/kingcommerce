from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.

# class CommentManager(models.Manager):
#     def filter_by_instance(self, instance):

class Comment(models.Model):

    content         = models.CharField(max_length = 300, null=True, blank=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    created         = models.DateTimeField(auto_now = True)
    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content
