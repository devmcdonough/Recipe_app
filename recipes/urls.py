from django.urls import path
from .views import RecipeDetailView, RecipeListView

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='list'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail')
]
