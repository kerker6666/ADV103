from django.contrib import admin
from .models import Category, Tag, Article

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('tagName',)
    list_display = ('id', 'tagName')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('categoryName',)
    list_display = ('id','categoryName')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'content', 'publish_date')