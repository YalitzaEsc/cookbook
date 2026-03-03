from django import forms
from .models import Recipe, RecipeIngredient
from django.forms import inlineformset_factory

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cooking_time', 'instructions']
        
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Type the steps here...'}),
        }

IngredientFormSet = inlineformset_factory(
    Recipe,                                 #Modelo padre
    RecipeIngredient,                       #Modelo Hijo
    fields=('ingredient', 'quantity'),      #Campos a llenar
    extra=3,                                #Filas extra
    can_delete=True                         #Permite borrar ingredientes
)