from django.urls import path
from .views import RecipeCreateView, RecipeDetailView, toggle_favorite, RecipeUpdateView


urlpatterns = [
    path('add-recipe', RecipeCreateView.as_view(), name="recipe_create"),
    path('detail/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    path('recipe/<int:pk>/favorite/', toggle_favorite, name='toggle_favorite'),
    path('update-recipe/<int:pk>', RecipeUpdateView.as_view(), name="update_recipe")
]
