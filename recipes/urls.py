from django.urls import path
from .views import RecipeCreateView, RecipeDetailView


urlpatterns = [
    path("add-recipe", RecipeCreateView.as_view(), name="recipe_create"),
    path("detail/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail")
]
