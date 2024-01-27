from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Recipe, ProductRecipe, Product


def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')

        product = get_object_or_404(Product, pk=product_id)
        recipe = get_object_or_404(Recipe, pk=recipe_id)

        product_recipe, created = ProductRecipe.objects.get_or_create(recipe=recipe, product=product)
        product_recipe.weight = weight
        product_recipe.save()

        return HttpResponse('Продукт добавлен в рецепт/Вес продукта обновлен')


def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        recipe = get_object_or_404(Recipe, pk=recipe_id)

        for product_recipe in recipe.productrecipe_set.all():
            product_recipe.product.cooking_count += 1
            product_recipe.product.save()

        return HttpResponse('Блюдо по рецепту приготовлено')


def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product = get_object_or_404(Product, pk=product_id)

        recipes_without_product = Recipe.objects.exclude(productrecipe__product=product)
        recipes_with_low_quantity = Recipe.objects.filter(productrecipe__product=product,
                                                          productrecipe__weight__lt=10)

        context = {
            'recipes_without_product': recipes_without_product,
            'recipes_with_low_quantity': recipes_with_low_quantity,
        }

        return render(request, 'template.html', context)
