from django.db import models
import datetime
import os

# Create your models here.
# models.py

def get_file_path(request, filename):
    filename_original = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, filename_original)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

class Images(models.Model):
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField(max_length=1000,blank=True)
    image = models.ImageField(upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
