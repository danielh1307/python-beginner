class Restaurant:
    """This is a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name is {self.restaurant_name} and the cuisine type is {self.cuisine_type}")

    @staticmethod
    def open():
        print("The restaurant is now open")


r1 = Restaurant('Barone', 'Italiener')
print(r1.restaurant_name)
print(r1.cuisine_type)
r1.describe_restaurant()
r1.open()
Restaurant.open()
