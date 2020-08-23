from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Store(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=254)
    description_1 = models.TextField()
    description_2 = models.TextField()
    description_3 = models.TextField()
    description_4 = models.TextField()
    before_discount = models.DecimalField(max_digits=6, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
