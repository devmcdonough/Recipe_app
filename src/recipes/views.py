from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
# To display lists
from django.views.generic import ListView, DetailView
# to access Recipe model
from .models import Recipe
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_chart


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_home.html'
    context_object_name = 'recipes'

    # Overrides get_queryset method to filter recipes
    def get_queryset(self):
        queryset = Recipe.objects.all()
        form = RecipeSearchForm(self.request.GET or None)

        if form.is_valid() and self.request.GET:
            recipe_name = form.cleaned_data.get('recipe_name')
            print(f"Search term: {recipe_name}")
            ingredients = form.cleaned_data.get('ingredients')
            difficulty = form.cleaned_data.get('difficulty')

            if recipe_name:
                queryset = queryset.filter(name__icontains = recipe_name)
            if ingredients:
                queryset = queryset.filter(ingredients__icontains = ingredients)
            if difficulty and difficulty != '':
                if difficulty == "Easy":
                    queryset = queryset.filter(cooking_time__lte=5, ingredients__regex=r'^[^,]*(,[^,]*){0,2}$')
                elif difficulty == "Medium":
                    queryset = queryset.filter(cooking_time__gt=5, ingredients__regex=r'^[^,]*(,[^,]*){0,2}$')
                elif difficulty == "Intermediate":
                    queryset = queryset.filter(cooking_time__lte=5, ingredients__regex=r'^[^,]*(,[^,]*){0,3}$')
                else:
                    queryset = queryset.filter(cooking_time__lte=10, ingredients__regex=r'^[^,]*(,[^,]*){0,2}$')


        return queryset
        
    # Override get_context_data to add Pandas DataFrame to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        recipe_df = None
        chart = None

        # Check if a search is performed (reqeust.GET is not empty)
        if self.request.GET:
            # prepare data for dataframe
            recipe_data = []
            chart_data = []
            for recipe in queryset:
                recipe_data.append({
                    'name': f'<a href="{recipe.get_absolute_url()}">{recipe.name}</a>',
                    'cooking_time': recipe.cooking_time,
                    'ingredients': recipe.ingredients,
                    'difficulty': recipe.difficulty(),
                    'url': recipe.get_absolute_url()
                })

                chart_data.append({
                    'raw_name': recipe.name,
                    'cooking_time': recipe.cooking_time,
                    'ingredients': recipe.ingredients,
                    'difficulty': recipe.difficulty()
                })


            # Convert queryset to Pandas DataFrame
            recipe_df = pd.DataFrame(recipe_data)
            if not recipe_df.empty:
                # Convert DataFrame to HTML
                recipe_df_html = recipe_df.to_html(classes='table table-striped', escape=False)
                context['recipe_df'] = recipe_df_html   

                chart_df = pd.DataFrame(chart_data)
                chart_type = self.request.GET.get('chart_type')
                if chart_type:
                    chart = get_chart(chart_type, chart_df, labels=chart_df['raw_name'].values)             

        context['chart'] = chart
        context['form'] = RecipeSearchForm(self.request.GET or None)
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'