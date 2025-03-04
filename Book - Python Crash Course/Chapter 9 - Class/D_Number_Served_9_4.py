# Start with your program from Exercise 9-1 (page 162). 
# Add an attribute called number_served with a default value of 0. 
# Create an instance called restaurant from this class. 

# Print the number of customers the restaurant has served, and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again.

# Add a method called increment_number_served() that lets you increment the number of customers
# who’ve been served. Call this method with any number you like that could represent 
# how many customers were served in, say, a day of business.


class Restaurant:
        """A Restaurant model"""

        def __init__(self,name, cuisine_type):
            """Initialize"""
            self.name = name.title()
            self.cuisine_type = cuisine_type
            self.number_served = 0

        def describe_restaurant(self):
              """Display a summary of the restaurant"""
              msg = f"{self.name} serves wonderful {self.cuisine_type}."
              print(f"\n{msg}")
        
        def open_restaurant(self):
              print(f"The {self.name} is open!")
        def set_number_served(self):
              msg = f"insert the number of customers that have been served: "
              prompt = input(msg)
              prompt = int(prompt)
              self.number_served = prompt
        def increment_number_served(self, increment):
              self.number_served += increment
              print(self.number_served)

restaurant = Restaurant ('Baggio', 'pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.set_number_served()
print(restaurant.number_served)
restaurant.increment_number_served(10)
