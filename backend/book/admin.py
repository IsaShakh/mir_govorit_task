from django.contrib import admin
from .models import ProductRecipe, Product, Recipe


# Register your models here.
class ProductRecipeInline(admin.TabularInline):
    model = ProductRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [ProductRecipeInline]


admin.site.register(Product)
admin.site.register(Recipe, RecipeAdmin)
