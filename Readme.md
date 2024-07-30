
# Overview
The Django Recipe Management System is a web application that allows users to manage recipes. Users can perform CRUD (Create, Read, Update, Delete) operations on recipes. The application features both a REST API and a traditional web interface for interacting with the recipe data.

## Features
View Recipes: Users can browse a list of all recipes and view detailed information about each recipe.

Create Recipes: Users can add new recipes by providing details such as the name, ingredients, and instructions.

Edit Recipes: Users can modify existing recipes, updating details as needed.

Delete Recipes: Users can remove recipes from the system.
# Installation and Setup Instructions

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django
- Django REST Framework
- MySQL (or another supported database)

## Installation

### Clone the Repository

1. **Clone the Repository**

   ```bash
   git clone https://github.com/28vedant/RecipeapplicationwithDjango-DRF.git
   

   ```

2. **Set Up a Virtual Environment**

Create and activate a virtual environment to manage project dependencies:

```bash
python -m venv venv
```


## Install Dependencies

Install the required Python packages specified in the requirements.txt file:

```bash
pip install -r requirements.txt
```
**Ensure that requirements.txt includes:**

```bash
Django>=3.2,<4.0
djangorestframework
mysqlclient
```
**Configure the Database**

Update the settings.py file to configure your MySQL database.

Make sure the MySQL server is running and accessible:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Replace your_database_name, your_database_user, and your_database_password with your actual MySQL credentials.

**Apply Migrations**

Apply the database migrations to set up the initial schema:

```bash
python manage.py migrate
```
**Create a Superuser**

Create a superuser account for accessing the Django admin interface:

```bash

python manage.py createsuperuser
```
**Run the Development Server**

Start the development server to run the application:

```bash
python manage.py runserver
```

## Access the application at http://127.0.0.1:8000/.





# Overview
The Django Recipe Management System is a web application that allows users to manage recipes. Users can perform CRUD (Create, Read, Update, Delete) operations on recipes. The application features both a REST API and a traditional web interface for interacting with the recipe data.

## Features
View Recipes: Users can browse a list of all recipes and view detailed information about each recipe.

Create Recipes: Users can add new recipes by providing details such as the name, ingredients, and instructions.

Edit Recipes: Users can modify existing recipes, updating details as needed.

Delete Recipes: Users can remove recipes from the system.
# Installation and Setup Instructions

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django
- Django REST Framework
- MySQL (or another supported database)

## Installation

### Clone the Repository

1. **Clone the Repository**

   ```bash
   git clone https://github.com/28vedant/RecipeapplicationwithDjango-DRF.git
   

   ```

2. **Set Up a Virtual Environment**

Create and activate a virtual environment to manage project dependencies:

```bash
python -m venv venv
```


## Install Dependencies

Install the required Python packages specified in the requirements.txt file:

```bash
pip install -r requirements.txt
```
**Ensure that requirements.txt includes:**

```bash
Django>=3.2,<4.0
djangorestframework
mysqlclient
```
**Configure the Database**

Update the settings.py file to configure your MySQL database.

Make sure the MySQL server is running and accessible:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Replace your_database_name, your_database_user, and your_database_password with your actual MySQL credentials.

**Apply Migrations**

Apply the database migrations to set up the initial schema:

```bash
python manage.py migrate
```
**Create a Superuser**

Create a superuser account for accessing the Django admin interface:

```bash

python manage.py createsuperuser
```
**Run the Development Server**

Start the development server to run the application:

```bash
python manage.py runserver
```

## Access the application at http://127.0.0.1:8000/.




