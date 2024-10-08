from collections import Counter
from src.recipes.models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_ingredient_count():
    data = {
        'recipes': [],
        'ingredient_count': []
    }

    for recipe in Recipe.objects.all():
        count = len(recipe.ingredients.split(', '))
        data['recipes'].append(recipe.name)
        data['ingredient_count'].append(count)

    return data


def get_graph():
    # create a BytesIO buffer for image
    buffer = BytesIO()
    # Create a plot with a bytesIO object as a file like object. Set format to png
    plt.savefig(buffer, format='png')
    # set cursor to the beginning of the stream
    buffer.seek(0)
    # retrive the content of the file
    image_png = buffer.getvalue()
    # encode the bytes-like object
    graph = base64.b64encode(image_png)
    # decode to get the string as output
    graph = graph.decode('utf-8')
    # free up the memory of buffer
    buffer.close()
    # return image/graph
    return graph

# chart_type: user input or type of chart
# data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
    # switch plot backend to AGG (Anti-Grain Geometry) - to write a file
    # AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')

    # specify figure size
    fig = plt.figure(figsize=(6, 3))

    if chart_type == '#1':  # Bar chart
        # Split and count ingredients like in the pie chart
        all_ingredients = []
        for ingredient_list in data['ingredients']:
            all_ingredients.extend(ingredient_list.split(", "))  # Split the comma-separated ingredients

        ingredient_counts = Counter(all_ingredients)  # Count each ingredient's frequency
        ingredients = list(ingredient_counts.keys())  # Ingredient names (x-axis)
        counts = list(ingredient_counts.values())     # Their counts (y-axis)

        plt.bar(ingredients, counts)  # Plot ingredient names vs their counts
        plt.xlabel('Ingredients')
        plt.ylabel('Frequency')
        plt.title('Top Ingredients by Frequency')
        plt.xticks(rotation=45, ha="right")  # Rotate the labels for better readability

    if chart_type == '#2':  # Pie chart
        # Count how often each ingredient appears across all recipes
        all_ingredients = []
        for ingredient_list in data['ingredients']:
            all_ingredients.extend(ingredient_list.split(", "))  # Split and aggregate all ingredients

        ingredient_counts = Counter(all_ingredients)  # Count each ingredient's frequency
        labels = ingredient_counts.keys()  # The labels (ingredient names)
        sizes = ingredient_counts.values()  # The sizes (counts of each ingredient)

        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Ingredient Usage Distribution')

    elif chart_type == '#3':  # Line chart with dots (markers)
        # Calculate the number of ingredients for each recipe
        num_ingredients = [len(ingredient_list.split(", ")) for ingredient_list in data['ingredients']]
        cooking_time = data['cooking_time']

        # Plot a line with markers (dots) at each data point
        plt.plot(num_ingredients, cooking_time, marker='o', linestyle='-', color='b')
        plt.xlabel('Number of Ingredients')
        plt.ylabel('Cooking Time (mins)')
        plt.title('Cooking Time vs Number of Ingredients')
        plt.grid(True)  # Optional: add grid for better readability

    else:
        print('unknown chart type')

    # specify layout details
    plt.tight_layout()

    # render the graph to file
    chart = get_graph()
    return chart

