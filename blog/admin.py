from django.contrib import admin
from blog.models import BlogCategory, BlogTag, Post

class PostAdmin(admin.ModelAdmin):
    list_display=[
        'id', 
        'title',
        'is_active',
        'view_count',
    ]

admin.site.register(BlogCategory)
admin.site.register(BlogTag)
admin.site.register(Post, PostAdmin)