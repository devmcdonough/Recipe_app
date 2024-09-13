# Recipe App (CLI Version)

The Recipe App is a Python-based command-line application that allows users to manage and view recipes directly through the terminal. Each recipe contains information such as the name, cooking time, list of ingredients, and difficulty level (calculated based on cooking time and number of ingredients).

## Features

- Create and manage recipes with a name, cooking time, and ingredients.
- Difficulty level is automatically calculated based on the number of ingredients and cooking time.
- Full test coverage for key components (e.g., recipe name, cooking time, ingredients, and difficulty calculation).

## Technologies Used

- **Python** (version 3.8+)
- **Django** (for data management)
- **SQLite** (default database)
- **Git** (for version control)

## Installation

To run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/devmcdonough/recipe_app.git

2. **Navigate to the project directory:**
    cd Recipe_app

3. **Set up a virtual environment**
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. **Install dependencies**
    pip install -r requirements.txt

5. **Apply migrations**
    python manage.py migrate

6. **Running the CLI Application**
    python manage.py shell

