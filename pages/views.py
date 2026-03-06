from django.views.generic import ListView
from recipes.models import Recipe

# Create your views here.

class HomePageView(ListView):
    model = Recipe
    template_name = "pages/home.html"
    context_object_name = "recipes"
    paginate_by = 6
    ordering = ['-date_of_post']