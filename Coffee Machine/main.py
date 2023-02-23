MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def user_choice(user_selection):
    ask_end = False
    while not ask_end:
        user_selection = input("Select Your drink: 'espresso', 'latte' or 'cappuccino': ").lower()
        ingredients = MENU[user_selection]['ingredients']
        cost = MENU[user_selection]['cost']
        updated_resources = update_resources(ingredients)
    


def update_resources(selected_ingredients):
    updated_resources = {key: resources[key] - selected_ingredients.get(key,0)
                         for key in resources.keys()}
    for key in updated_resources:
        if updated_resources[key] < 0:
            print(f"Sorry, there is not enough {key}")
    return updated_resources

def calculate_money():
    cash = {quarter:,
    dime:, 
    nicke:, 
    penny:, }