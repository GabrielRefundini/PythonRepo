# Start with your class from Exercise 9-1. 
# Create three different instances from the class, and call describe_restaurant() for each instance.
class Restaurant:
        """A Restaurant model"""

        def __init__(self,name, cuisine_type):
            """Initialize"""
            self.name = name.title()
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
              """Display a summary of the restaurant"""
              msg = f"{self.name} serves wonderful {self.cuisine_type}."
              print(f"\n{msg}")
        
        def open_restaurant(self):
              print(f"The {self.name} is open!")

restaurant = Restaurant ('Baggio', 'pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()

tug = Restaurant ('Tug', 'Sushi')
tokyo = Restaurant ('Tokyo', 'Japanese')

tug.describe_restaurant()
tokyo.describe_restaurant()