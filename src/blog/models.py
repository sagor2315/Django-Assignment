from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Category.objects.filter(slug = self.slug).exists():
                self.slug = f'{(slugify(self.title))}-{get_random_string(4)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):

    STATUS = [('draft', 'Draft'), ('publish', 'Publish')]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank = True, null = True)
    content = RichTextUploadingField()
    created_post = models.DateTimeField(auto_now_add = True)
    update_post = models.DateField(auto_now = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    featured = models.ImageField(upload_to='blogs/', blank=True, null=True)
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_des = models.TextField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Post.objects.filter(slug = self.slug).exists():
                self.slug = f'{(slugify(self.title))}-{get_random_string(4)}'
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'All Post'

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.image.url

# Comment Section
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=260)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name) 

