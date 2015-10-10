from django.db import models
from django.contrib import admin 

# Create your models here.
class List(models.Model): 
 title = models.CharField(max_length=250, unique=True) 
 def __unicode__(self): 
   return self.title 
 class Meta: 
   ordering = ['title'] 
 class Admin: 
   pass
   
import datetime 

class Item(models.Model): 
 title = models.CharField(max_length=250) 
 content = models.CharField(max_length=10240)
 created_date = models.DateTimeField(default=datetime.datetime.now) 
 completed = models.BooleanField(default=False) 
 article_list = models.ForeignKey(List) 
 def __unicode__(self): 
   return self.title 
 class Meta: 
   ordering = ['-created_date', 'title'] 
 class Admin: 
   pass
   
admin.site.register(List)
admin.site.register(Item)