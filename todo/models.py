from __future__ import unicode_literals

from django.db import models
import datetime 


class Todo(models.Model):
    title = models.CharField(max_length=100, unique=True) 
    description = models.TextField() 
    created = models.DateTimeField(blank=True, auto_now_add=True) 
 
    def __unicode__(self): 
        return self.title

    class Meta:
		ordering = ['-created']


# class List(models.Model): 
#   title = models.CharField(maxlength=250, unique=True) 
#   def __str__(self): 
#     return self.title 
#   class Meta: 
#     ordering = ['title'] 
#   class Admin: 
    # pass


 
# PRIORITY_CHOICES = ( 
#   (1, 'Low'), 
#   (2, 'Normal'), 
#   (3, 'High'), 
# ) 
 
# class Item(models.Model): 
#   title = models.CharField(maxlength=250) 
#   created_date = models.DateTimeField(default=datetime.datetime.now) 
#   priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
#   completed = models.BooleanField(default=False) 
#   todo_list = models.ForeignKey(List) 
#   def __str__(self): 
#     return self.title 
#   class Meta: 
#     ordering = ['-priority', 'title'] 
#   class Admin: 
#     pass 

