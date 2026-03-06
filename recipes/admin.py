from django.contrib import admin
from .models import Recipe, RecipeIngredient, Category

# Register your models here.
    
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Category)

    

