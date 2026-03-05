from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    date_of_post = models.DateTimeField(auto_now=True)
    cooking_time = models.PositiveIntegerField() 
    instructions = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    favorites = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="favorite_recipes",
        blank=True
    )
    
    def __str__(self):
        return self.title[:50]
    
    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"pk": self.pk})
    

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=150)
    quantity = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.quantity} of {self.ingredient}.'

    