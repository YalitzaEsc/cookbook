from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm, IngredientFormSet

# Create your views here.

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/add_recipe.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs) 
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST)
        else:
            data['ingredients'] = IngredientFormSet()
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        
        form.instance.author = self.request.user
        
        if form.is_valid() and ingredients.is_valid():
            self.object = form.save()
            ingredients.instance = self.object
            ingredients.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))