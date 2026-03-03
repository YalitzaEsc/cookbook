from django.urls import path
from .views import RecipeCreateView


urlpatterns = [
    path("", RecipeCreateView.as_view(), name="recipe_create")
]
