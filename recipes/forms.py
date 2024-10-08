from django import forms

DIFFICULTY_CHOICES = (
    ('', 'All'),
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard')
)

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=120, required=False)
    ingredients = forms.CharField(max_length=255, required=False)
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES, required=False)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES, required=False)