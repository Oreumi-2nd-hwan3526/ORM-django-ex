from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    list_filter = ('title', 'content', 'created_at')

admin.site.register(Article, ArticleAdmin)