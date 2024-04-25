# Shopping

## Project Description
Shopping is a web application that allows users to register and log in. Once logged in, users can browse through different brands and select categories to see detailed product pages. The application enables users to add products to their cart, view original prices, and see discounted prices in a bar chart format.

## Installation Guide
To set up the project, follow these steps:

1. Navigate to the `Assessment3Solo` directory.
2. Set the Python version by running the command: `pyenv local 3.7.0`
3. Create a virtual environment: `python3 -m venv .venv`
4. Activate the virtual environment:
   ```bash
   source .venv/bin/activate

Install dependencies from the following list:
asgiref==3.8.1
Django==4.1
sqlparse==0.5.0
typing_extensions==4.11.0

Usage Instructions
After registration and logging in, users can view a list of brands. Clicking on a brand will show the different categories under it. Selecting a category will display detailed pages of the products within it.

Technology Stack
Django 4.1.0
Python 3.10.7
Features List
User registration and login.
Browse brands and their categories.
View detailed product pages with options to add items to the cart.
Display original and discounted prices in a bar chart.

Running Tests
Run tests for model.py and view.py using the following command:
python manage.py test
