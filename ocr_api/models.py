
import os
from django.db import models
# from django.db.models.fields import UUIDField

# Create your models here.


def content_file_name(instance, filename):
    
    directory = instance.name

    print(os.path)
    path = os.path.join('uploads', directory)
  
    #print(path)
    #os.mkdir(path)
    filename = "%s_%s" % (instance.name, filename)
    return os.path.join(path, filename)    
    #return filename

class Document(models.Model):
    name=models.CharField(max_length=50,blank=True)
    docfile = models.FileField(upload_to=content_file_name,blank=False) 


