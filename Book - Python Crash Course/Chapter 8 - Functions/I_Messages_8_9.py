# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)

text_messages = [
    "Hey, how's it going?",
    "Let's catch up soon!",
    "Don't forget to bring your keys.",
    "Can you pick up some groceries?",
    "Just wanted to check in.",
    "Thanks for the help today!",
    "Have a great day!",
    "Happy birthday! Hope you have an amazing day!",
    "Are you free later this afternoon?",
    "Looking forward to the weekend!"
]

show_messages(text_messages)