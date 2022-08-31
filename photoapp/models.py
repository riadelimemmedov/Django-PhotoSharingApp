from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

from taggit.managers import TaggableManager
# Create your models here.

#!Photo
class Photo(models.Model):
    title = models.CharField(max_length=50,unique=True,null=True)
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=False,upload_to='photos/',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    submitter = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,unique=True,db_index=True)
    tags = TaggableManager()
    
    def __str__(self):
        return str(self.title)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Photo,self).save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        
        