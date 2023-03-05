def describe_pet(pet_name, animal_type='Dog'):
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")


def change_dictionary(d):
    d["function_called"] = True


def make_pizza(*toppings):
    """Accepts an arbitrary number of arguments"""
    for topping in toppings:
        print(topping)


def build_profile(first, last, **user_info):
    """Accepts always a first name, a last name, and an arbitrary number of key value pairs"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet('willie', 'Cat')
describe_pet(animal_type='Bird', pet_name='Inky')

# This code shows a dictionary is passed by reference
# It can be changed inside a function
dictionary = {
    "function_called": False
}
print(dictionary["function_called"])
change_dictionary(dictionary)
print(dictionary["function_called"])

# How to call a function with an arbitrary number of arguments
make_pizza('Cheese')
make_pizza('Cheese', 'Salami', 'Peperoni')
make_pizza()

# How to call a function with an arbitrary number of key value pairs
user_profile = build_profile(
    'Albert',
    'Einstein',
    location='princeton',
    field='physics'
)
print(user_profile)
