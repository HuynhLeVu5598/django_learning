from tkinter import CASCADE
from django.db import models
from django.conf import settings

def upload_location(instance,filename):
    print(instance)
    filebase, extension = filename.split('.')
    return '%s/%s.%s'%(instance, filebase,extension)
# Create your models here.
class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    content = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,null=True,blank=True, height_field='height_field', width_field='width_field')
    height_field= models.IntegerField(default=0)
    width_field= models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-title']
