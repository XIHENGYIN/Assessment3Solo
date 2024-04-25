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
   ```
   git clone git@github.com:XIHENGYIN/Assessment3Solo.git
   ```
   
2. Navigate to the project directory:
   ```
   cd Assessment3Solo
   ```


3. Set the python version and create and activate the virtual environment：
   ```
   pyenv local 3.10.7 # this sets the local version of python to 3.10.7
   python3 -m venv .venv # this creates the virtual environment for you
   source .venv/bin/activate # this activates the virtual environment
   pip install --upgrade pip # this installs pip, and upgrades it if required.
   ```

4. Install Django:
   ```
   pip install Django==4.1.0
   ```
6. Generate migration files and apply them:
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
   •	 When you modify the model (Model) or add a new application (App) in the Django project usually involves changes to the database schema, in the future if you need to modify, for example, the following: create    a  new table, modify the fields, add indexes, etc. you need to run the above code.

7. Start the development server:
   ```
   python3 manage.py runserver 0.0.0.0:8000 
   ```
8. Open your web browser and navigate to `http://localhost:8000` to access the application.


## How to use 

- **Homepage**: Browse for an overview of available brands.
- **Brand Pages**: Click on a brand to see its categories.
- **Category Pages**: Choose a category to view its products.
- **Product Pages**: Click on a product for more detailed information, including pricing options.

## Testing

Run the following command to execute tests:
```
python3 manage.py test
```
USE
---
1. **Consumers**: Shop and explore products across various brands and categories.
2. **Market Analysts**: Study consumer trends and product popularity.
