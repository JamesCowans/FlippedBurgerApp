from django.db import models

# Create your models here.

class Menu_section(models.Model):
    name = models.Charfield(
        max_length=100,
        unique=True)

    slug = models.SlugField(
        max_length=100,
        unique = True)

        class Meta:
            order_selection('-name')

class Menu_item(models.Model):
    menu_section = models.ForeignKey(
        Menu_section, related_name = 'menu_item', 
        on_delete = models.CASCADE)

    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=100, unique = True)
    image = models.ImageField(upload_to='menu_item/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

        class Meta:
            order_selection('-name')

