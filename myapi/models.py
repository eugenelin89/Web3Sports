from django.db import models
from mybusiness.models import *

# Create your models here.
# File Upload based on:
# https://blog.vivekshukla.xyz/uploading-file-using-api-django-rest-framework/
# Used by FileViewSerializer (myproject/myapi/serializer.py) and FileViewSet (myproject/myaip/views.py)
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    business = models.ForeignKey(MyBusiness, on_delete=models.CASCADE, blank=True, null=True, related_name='files')