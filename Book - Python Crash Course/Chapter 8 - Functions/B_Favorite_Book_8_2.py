# Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as One of my favorite books is Alice in Wonderland. 
# Call the function, making sure to include a book title as an argument in the function call.
def favorite_book(book_title):
    print(f"One of my favorite books is: {book_title}")
title = input("Type the title of your favorite book! ")
favorite_book(title)
