from django.db import models

# Create your models here.

class Course(models.Model):
    sku = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=254)
    description_1 = models.TextField()
    description_2 = models.TextField()
    description_3 = models.TextField()
    description_4 = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
