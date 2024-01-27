from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    cooking_count = models.IntegerField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    product = models.ManyToManyField(Product, )

    def __str__(self):
        return self.name


class ProductRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.recipe.name} - {self.product.name}"
