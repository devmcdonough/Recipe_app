from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),  # Maps the home view to the '' URL (i.e., /recipes/)
]
