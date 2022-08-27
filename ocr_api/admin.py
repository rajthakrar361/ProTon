from django.contrib import admin

# Register your models here.
from .models import Document

class documentAdmin(admin.ModelAdmin):
    list_display=['docfile']

admin.site.register(Document)    