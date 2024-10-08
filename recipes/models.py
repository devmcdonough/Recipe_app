from django.db import models
from django.shortcuts import reverse
# To protect class based view
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your models here.
class Recipe(models.Model, LoginRequiredMixin):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveBigIntegerField(help_text="Time in minutes")
    ingredients = models.TextField(help_text="List ingredients and separate with commas")
    pic = models.ImageField(upload_to='recipes', default='no_picture.png')


    def difficulty(self):
        num_ingredients = len(self.ingredients.split(", "))
        if self.cooking_time <= 5 and num_ingredients <= 3:
            return "Easy"
        elif self.cooking_time >= 5 and num_ingredients <= 3:
            return "Medium"
        elif self.cooking_time >= 5 and num_ingredients >= 3:
            return "Intermediate"
        else:
            return "Hard" 

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})