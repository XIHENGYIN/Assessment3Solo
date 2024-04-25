# Shopping

This web application allows users to register and log in to access a variety of brands and their categories, offering a detailed view of products, including options to add them to the cart and view pricing details. Users can explore brands, choose categories, and purchase products with an interface that provides both original and discounted prices.

## Features

- **User Registration and Login**: Secure access to the application with individual user accounts.
- **Brand Exploration**: Users can view a list of all available brands.
- **Category Browsing**: Navigate through different categories within each brand.
- **Product Details**: Access detailed information about each product, including options to add items to the shopping cart.
- **Price Visualization**: View original and discounted prices in a bar chart format.

How to start it
----------------
1. Clone the repository:
2. Navigate to the project directory:
   cd Assessment3Solo
  
3. Set the python version and create and activate the virtual environment：
  
pyenv local 3.10.7
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

4. Install Django:
   pip install Django==4.1.0

5. Generate migration files and apply them:
python3 manage.py makemigrations
python3 manage.py migrate
6. Start the development server:
 python3 manage.py runserver 0.0.0.0:8000 
7. Access the application by navigating to `http://localhost:8000` on your web browser.

## How to use 

- **Homepage**: Browse for an overview of available brands.
- **Brand Pages**: Click on a brand to see its categories.
- **Category Pages**: Choose a category to view its products.
- **Product Pages**: Click on a product for more detailed information, including pricing options.

## Testing

Run the following command to execute tests:
python3 manage.py test
USE
---
1. **Consumers**: Shop and explore products across various brands and categories.
2. **Market Analysts**: Study consumer trends and product popularity.
