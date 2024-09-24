from django.test import TestCase
from .models import Recipe
from django.urls import reverse, resolve
from recipes.views import RecipeDetailView, RecipeListView

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name='Tea',
                              cooking_time='5',
                              ingredients='Water, Sugar, Tea Packet')

    # Test to see if recipe name is initialized as expected
    def test_recipe_name(self):
        # Get recipe object to test
        recipe = Recipe.objects.get(id=1)
        # Get metadata for name field
        field_label = recipe._meta.get_field('name').verbose_name
        # Compare value to expected result
        self.assertEqual(field_label, 'name')

    # Test to see if max length is working for name
    def test_recipe_name_max_length(self):
         # Get recipe object to test
        recipe = Recipe.objects.get(id=1)
        # Get metadata for name field
        max_length = recipe._meta.get_field('name').max_length
        # Compare value to expected result
        self.assertEqual(max_length, 120)

    # Test to see if cooking time is initialized as expected
    def test_cooking_time(self):
        # Get recipe object to test
        recipe = Recipe.objects.get(id=1)
        # Compare actual cooking to to the expected value
        self.assertEqual(recipe.cooking_time, 5)

    def test_recipe_ingredients(self):
        # Get recipe object to test
        recipe = Recipe.objects.get(id=1)
        # Compare value to expected result
        self.assertEqual(recipe.ingredients, 'Water, Sugar, Tea Packet')        

    def test_difficulty(self):
        # Get recipe object to test
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.difficulty(), 'Easy')

    def test_recipe_str(self):
        # Get recipe object to test
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), recipe.name)

    def test_recipe_default_img(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.pic.name, 'no_picture.png')

    def test_recipe_list_template_content(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertContains(response, 'Tea')

# Test URL patterns
class RecipeURLTests(TestCase):

    def test_list_url_resolves(self):
        url = reverse('recipes:list')
        self.assertEqual(resolve(url).func.view_class, RecipeListView)

    def test_detail_url_resolves(self):
        url = reverse('recipes:detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, RecipeDetailView)

# Test Views
class RecipeViewTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(name='Tea', cooking_time=5, ingredients='Water, Sugar, Tea Packet')

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_home.html')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipes:detail', kwargs={'pk': self.recipe.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/detail.html')

# Test get_absolute_url
class RecipeModelTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(name='Tea', cooking_time=5, ingredients='Sugar, Water, Tea Packet')

    def test_get_absolute_url(self):
        self.assertEqual(self.recipe.get_absolute_url(), reverse('recipes:detail', kwargs={'pk': self.recipe.pk}))

