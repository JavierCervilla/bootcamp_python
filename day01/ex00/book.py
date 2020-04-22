#!/usr/bin/env python3
import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        self.name = self.check_name(name)
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {"starter": [], "dessert": [], "lunch": []}


    def check_name(self, name):
        if not name:
            print("Name is empty")
            exit(1)
        else:
            return name

    def add_recype(self, recipe):
        try:
            recipe(recipe)
            try:
                if recipe.recipe_type == "lunch":
                    self.recipes_list["lunch"].append(recipe)
                elif recipe.recipe_type == "starter":
                    self.recipes_list["starter"].append(recipe)
                elif recipe.recipe_type == "dessert":
                    self.recipes_list["dessert"].append(recipe)
                self.last_update = datetime.datetime.now()
            except KeyError as k:
                print("Key error {} is not a rigth type".format(k))
                exit(1)
        except:
            print("not a recipe")
            exit(1)


    def get_recipe_by_name(self, name):
        for lista in self.recipes_list:
            for rec in self.recipes_list[lista]:
                if rec.name == name:
                    print(str(rec))
                    return rec

    def get_recipe_by_type(self, type):
        l = []
        for lista in self.recipes_list:
            if lista == type:
                for rec in self.recipes_list[type]:
                    l.append(rec.name)
            else:
                print("not a valid type")
                exit(1)
        if len(l) == 0:
            print("not any recipes for this type yet")
            exit(1)
        return l

