#!/usr/bin/env python3


class Recipe():
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = self.check_name(name)
        self.cooking_lvl = self.check_cooking_level(cooking_lvl)
        self.cooking_time = self.check_cooking_time(cooking_time)
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = self.check_recipe_type(recipe_type)

    def check_name(self, name):
        if not name:
            print('Name cant be empty')
            exit(1)
        else:
            return name

    def check_cooking_level(self, cooking_lvl):
        if cooking_lvl in range(1, 6):
            return cooking_lvl
        else:
            print("Cooking level must be between 1 and 5 inclusive.")
            exit(1)

    def check_cooking_time(self, cooking_time):
        try:
            time = int(cooking_time)
        except:
            ValueError
        if time < 0:
            print("Cooking time can not be negative")
            exit(1)
        else:
            return cooking_time

    def check_recipe_type(self, recipe_type):
        if recipe_type == "lunch" or recipe_type == 'dessert' or recipe_type == 'starter':
            return recipe_type
        else:
            print("[{}] Its not a valid recipe type, must be ('starter', 'lunch', 'dessert')".format(recipe_type))
            exit(1)
    def check_ingredients(self, ingredients):
        if not ingredients:
            print("no ingredients")
            exit(1)
        else:
            return ingredients

    def __str__(self):
        string = "Recype name: {}.\nDificult:   {}.\nTime to prepare:    {}.\nIngredients:    {}\nDescription:    {}.\nType of food:   {}".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return string

"""     def take_ingredients(self):
        ingredients = []
        num = input("insert the number of ingredients:\t")
        try: int(num)
        except:
            print("[{}] This is not a valid number.".format(num))
            exit(1)
        num += 1
        for i in range(1,num):
            ingredients.append(input("introduzca ingrediente\t"))
        return ingredients """

