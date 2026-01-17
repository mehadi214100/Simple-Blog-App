from django.db import models

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