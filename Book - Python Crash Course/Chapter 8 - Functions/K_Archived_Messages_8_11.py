# Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.


def show_messages(messages):
    """Print all messages in the list."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print all messages in the list and move each message to a new list."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


sent_messages =[]

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

# show_messages(text_messages)
send_messages(text_messages[:], sent_messages)
print(text_messages)