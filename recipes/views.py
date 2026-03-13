from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from .models import Recipe
from .forms import RecipeForm, IngredientFormSet

# Create your views here.

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/add_recipe.html'
    
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
    
    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.object.pk})


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail_recipe.html"
    context_object_name = "recipe"
        
        
@login_required
def toggle_favorite(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
    else:
        recipe.favorites.add(request.user)
    return redirect('recipe_detail', pk=pk)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title', 'category', 'short_description', 'cooking_time', 'instructions']
    template_name = 'recipes/update_recipe.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.POST:
            context['ingredients'] = IngredientFormSet(self.request.POST, instance=self.object)
        else:
            context['ingredients'] = IngredientFormSet(instance=self.object)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        
        if form.is_valid() and ingredients.is_valid():
            self.object = form.save()
            ingredients.instance = self.object
            ingredients.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user
    
    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/delete_recipe.html'
    success_url = reverse_lazy("my_recipes")
    
    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user
    
    
class MyRecipesView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/my_recipes.html'
    context_object_name = "recipes"
    paginate_by = 6
    ordering = ['-date_of_post']
    
    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user).order_by('-date_of_post')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user_recipes =self.get_queryset()
        context['total_recipes'] = user_recipes.count()
        
        total_favorites = 0
        for recipe in user_recipes:
            total_favorites += recipe.favorites.count()
            
        context['total_favorites'] = total_favorites
        
        return context