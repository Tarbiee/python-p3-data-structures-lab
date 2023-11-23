spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    names = [food for food in spicy_foods if food["heat_level"] > 5]
    return names
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level =food["heat_level"]
        heat_emoji= " 🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level:{heat_emoji}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level =food["heat_level"]
            heat_emoji= " 🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level:{heat_emoji}")
    


def get_average_heat_level(spicy_foods):
    sum = 0
    count = len(spicy_foods)
    for food in spicy_foods:
        sum += food["heat_level"]
    average = sum/count
    return average

    
def create_spicy_food(spicy_foods, spicy_food):
    spicy_food = {"name":"Griot", "cuisine":"Haitian", "heat_level": 10}
    spicy_foods.append(spicy_food)
    return spicy_foods
    
