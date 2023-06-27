from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce import models as tinymce_models



class BlogCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
         return reverse(
            'blog:category_view', 
            kwargs={
            'category_slug': self.slug
             }
         )

class BlogTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', blank=True,)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'blog:tag_view',
            kwargs={
                "tag_slug":self.slug
            }
        )

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(BlogTag)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(upload_to='post')
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = tinymce_models.HTMLField(blank=True, null=True)
    is_active = models.BooleanField(default=False) 
    view_count = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={
            'category_slug': self.category.slug,
            'post_slug':self.slug
            }
        )
    
