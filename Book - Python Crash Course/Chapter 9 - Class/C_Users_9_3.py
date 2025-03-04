# Make a class called User. 
# Create two attributes called first_name and last_name, and then create several
# other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.

# Create several instances representing different users, and call both methods for each user.
class User:
    """User"""
    def __init__(self, first_name, last_name, password, email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
    
    def describe_user(self):
        print(f"First Name: {self.first_name} {self.last_name}")
        print(f"Password: {self.password} is safe, belive us (hahaha)")
        print(f"E-mail: {self.email}")
    
    def greet_user(self):
        """Greeting, sir"""
        print(f"Greetings {self.last_name}!")

usuario01 = User ('Gabriel', 'Oliveira', '123456', 'contato@gmail.com')
usuario02 = User ('Ted', 'Frein', 'SecretPass55', 'contatoted@gmail.com')
usuario01.describe_user()
usuario01.greet_user()

usuario02.describe_user()
usuario02.greet_user()
