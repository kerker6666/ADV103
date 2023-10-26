from django.db import models
from datetime import datetime

 
# Create your models here. 



class Tag(models.Model):
    tagName = models.CharField(max_length=50)

    def __str__(self):
        return self.tagName
    
class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName   
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    publish_date = models.DateTimeField(default = datetime.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title