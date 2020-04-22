#!/usr/bin/env python3

from recipe import Recipe
from book import Book

libro = Book("libro")
print (libro)
cake = Recipe("cake", 5, 15, ["sal","aceite","harina"], "Un pastel muy rico", "dessert")
cake2 = Recipe("cake2", 5, 15, ["aceite","harina"], "Un pastel muy rico", "dessert")
pizza = Recipe("pizza", 2, 30, ["pasta", "aceite", "tomate"], "una rica piizza", "lunch")
pizza2 = Recipe("pizza2", 2, 30, ["pasta", "aceite", "tomate"], "una rica piizza", "lunch")
libro.get_recipe_by_name("cakee")

