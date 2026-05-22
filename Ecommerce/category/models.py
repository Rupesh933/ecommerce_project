from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photo/categories', blank=True)

    class Meta:
        verbose_name = 'category'  # Singular name for the model shown in the admin interface
        verbose_name_plural = 'categories' # Plural name for the model 

    def __str__(self):
        return self.category_name