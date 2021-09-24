from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
# Create your models here.

class Category(models.Model):
    name = models.CharField("Category Name", max_length=150)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField("news Site", max_length=150)
    logo = models.ImageField("Site Logo", upload_to='site')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class NewsDetails(models.Model):
    title = models.CharField("News Title", max_length=250)
    content = models.TextField("News Content")
    image_url = models.CharField("Image Url", max_length=250)
    category = models.ForeignKey(Category, related_name='news_category', on_delete=models.CASCADE)
    #site = models.CharField("Site Name", max_length=150)
    site = models.ForeignKey(Site, related_name='news_site', on_delete=models.CASCADE)
    url = models.CharField("Site Url", max_length=250)
    author = models.CharField("Author Name", max_length=150, null=True, blank=True)
    uploaded = models.CharField("Time Uploaded", max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def get_comment(self):
        return self.comment.all.count

    def __str__(self):
        return f'{self.title} - {self.category.name}'

    class Meta:
        
        verbose_name = 'NewsDetails'
        verbose_name_plural = 'NewsDetailss'

class NewsComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(NewsDetails, related_name='comment', on_delete=models.CASCADE)
    comment = models.TextField("Comment")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.news.id} - {self.comment}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'



class Author(models.Model):
    name = models.CharField("Author Name", max_length=50)
    address = TextField("Author Address")

    

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


