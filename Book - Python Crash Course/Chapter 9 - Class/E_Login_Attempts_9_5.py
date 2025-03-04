# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly,
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:
    """User"""
    def __init__(self, first_name, last_name, password, email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"First Name: {self.first_name} {self.last_name}")
        print(f"Password: {self.password} is safe, belive us (hahaha)")
        print(f"E-mail: {self.email}")
    
    def greet_user(self):
        """Greeting, sir"""
        print(f"Greetings {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


usuario01 = User ('Gabriel', 'Oliveira', '123456', 'contato@gmail.com')
usuario02 = User ('Ted', 'Frein', 'SecretPass55', 'contatoted@gmail.com')
usuario01.describe_user()
usuario01.greet_user()

usuario02.describe_user()
usuario02.greet_user()

usuario03 = User('Rafael', 'Fraid', 'strongpass123', 'rafaelfraid@gmail.com')
usuario03.increment_login_attempts()
usuario03.increment_login_attempts()
usuario03.increment_login_attempts()
usuario03.increment_login_attempts()
print(usuario03.login_attempts)
usuario03.reset_login_attempts()
usuario03.increment_login_attempts()
print(usuario03.login_attempts)
