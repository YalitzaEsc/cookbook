from django.urls import path
from .views import (
    RecipeCreateView, RecipeDetailView, 
    toggle_favorite, RecipeUpdateView, 
    RecipeDeleteView, MyRecipesView)


urlpatterns = [
    path('add-recipe', RecipeCreateView.as_view(), name="recipe_create"),
    path('detail/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    path('recipe/<int:pk>/favorite/', toggle_favorite, name='toggle_favorite'),
    path('update-recipe/<int:pk>', RecipeUpdateView.as_view(), name="update_recipe"),
    path('delete-recipe/<int:pk>', RecipeDeleteView.as_view(), name="delete_recipe"),
    path('my-recipes', MyRecipesView.as_view(), name="my_recipes")
]
