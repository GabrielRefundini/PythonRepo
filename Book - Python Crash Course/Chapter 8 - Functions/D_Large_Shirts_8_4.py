# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt( text = 'I love Python', size = 'large'):
    print(f"The size is: {size} and the text is: {text}")

make_shirt("Here we go!",'medium')
make_shirt(text = 'here we go again')