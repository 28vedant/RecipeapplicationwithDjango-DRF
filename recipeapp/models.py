from django.db import models

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # photos = models.ImageField(upload_to="images")
    ingredients = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Snack', 'Snack')
    ])

    def __str__(self):
        return self.name
