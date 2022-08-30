from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

from taggit.managers import TaggableManager
# Create your models here.

#!Photo
class Photo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=False,upload_to='photos/',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    submitter = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        
        
