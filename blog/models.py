from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color = models.CharField(default="blue", max_length=50)
    icon = models.CharField(default="fa-icons", max_length=50)


    def __str__(self):
        return self.category_name
    
class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150,blank=True)
    email = models.EmailField()
    biography = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="profile/")

    def __str__(self):
        return f"{self.first_name} - {self.email}"
    

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Publish'),
        ('private', 'Private'),
    )
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    content = RichTextField()
    tags = models.CharField(max_length=200, blank=True,help_text="Comma separated tags")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    publish_date = models.DateTimeField(default=timezone.now)

    is_featured = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    