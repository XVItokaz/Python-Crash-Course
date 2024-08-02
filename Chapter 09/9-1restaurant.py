class Restaurant():


    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a cozy and Serbian restaurant.")
        print(self.restaurant_name.title() + " serves home cooking food.")

    def open_restaurant(self):
        print(self.cuisine_type.title() + " is open between 08 am to 23 pm.")
              
the_restaurant = Restaurant('kravljans', 'open time')
print("Name of the restaurant is " + the_restaurant.restaurant_name.title() + ".")
print("Restaurant Kravljans have " + the_restaurant.cuisine_type.title() + " between 08 am to 23 pm." )



the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()




