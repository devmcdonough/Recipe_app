from django.shortcuts import render
# To display lists
from django.views.generic import ListView, DetailView
# to access Recipe model
from .models import Recipe

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_home.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'