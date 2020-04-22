#!/usr/bin/env python3

def get_name():
    name = input("insert the name of the recipe:\n")
    if (cookbook.get(name)) != None:
        print('okey! thats it!')
        return name
    else:
        print('i have not that recipe yet!')
        menu()


def add_recipe(name, ingredients, meal, prep_time):
    recipe = {'Ingredients': ingredients, 'Meal': meal, 'Prep_time': prep_time}
    auxbook = {name: recipe}
    cookbook.update(auxbook)


def print_recipe(name):
    recipe = cookbook.get(name)
    print('The list of ingredients are:\n{Ingredients}'.format(**recipe))
    print('The type of meal is {Meal}.'.format(**recipe))
    print("The preparation time is {} mins.".format(recipe['Prep_time']))


def del_recipe(name):
    if cookbook.get(name) != None:
        cookbook.pop(name)
    else:
        print('That recipe did not exist.')


cookbook = {
    'Sandwich': {'Ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'Meal': 'lunch', 'Prep_time': 20},
    'Cake': {'Ingredients': ['flour', 'sugar', 'eggs'], 'Meal': 'dessert', 'Prep_time': 60},
    'salad': {'Ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'Meal': 'lunch', 'Prep_time': 15}
}


def menu():
    print("Please select an option:")
    print("1: Add a recipe.")
    print("2: Delete a recipe.")
    print("3: Print a recipe.")
    print("4: print all recipes.")
    print("5: Quit.")
    option = int(input("select a valid option:\n"))
    if option == 1:
        name = input("what is the name of the recipe:\n")
        num_ingredients = int(
            input("Please tell me the number of ingredients:\t"))
        ingredients = []
        for i in range(1, num_ingredients + 1):
            ingredients.append(input("Add ingredient:"))
        meal = input("What kind of meal is:")
        prep_time = int(input("How long to prepare?"))
        add_recipe(name, ingredients, meal, prep_time)
        menu()
    elif option == 2:
        del_recipe(get_name())
        menu()
    elif option == 3:
        print_recipe(get_name())
        menu()
    elif option == 4:
        for i in cookbook:
            print(i)
            print_recipe(i)
        menu()
    elif option == 5:
        exit(0)
    else:
        print("Not a valid option")
        menu()

def main():
    menu()

if __name__ == "__main__":
    main()
