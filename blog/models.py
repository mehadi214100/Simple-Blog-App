from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color = models.CharField(default="blue", max_length=50)
    icon = models.CharField(default="fa-icons", max_length=50)


    def __str__(self):
        return self.category_name
    
