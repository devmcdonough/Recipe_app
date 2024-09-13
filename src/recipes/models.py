from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.PositiveBigIntegerField(help_text="Time in minutes")
    ingredients = models.TextField(help_text="List ingredients and separate with commas")

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