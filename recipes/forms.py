from django import forms
from .models import Recipe, RecipeIngredient
from django.forms import inlineformset_factory

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'short_description', 'cooking_time', 'instructions']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Choose a category"
        
        
IngredientFormSet = inlineformset_factory(
    Recipe,                                 #Modelo padre
    RecipeIngredient,                       #Modelo Hijo
    fields=('ingredient', 'quantity'),      #Campos a llenar
    extra=1,                                #Filas extra
    can_delete=True,                        #Permite borrar ingredientes
    widgets={
        'ingredient': forms.TextInput(attrs={'placeholder': 'E.g. Flour', 'required': 'required'}),
        'quantity': forms.TextInput(attrs={'placeholder': 'E.g. 500g', 'required': 'required'})
    }
)