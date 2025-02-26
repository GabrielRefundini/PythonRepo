# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it.

# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
def make_shirt(size, text):
    print(f"The size is: {size} and the text is: {text}")

make_shirt(12,"Here we go!")
make_shirt(text = 'here we go again', size = 14)