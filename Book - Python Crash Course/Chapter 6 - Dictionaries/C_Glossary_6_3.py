# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print 
# its meaning indented on a second line. Use the newline character (\n) 
# to insert a blank line between each word-meaning pair in your output.
glossary = {
    'Variable': 'A variable is a name given to a value that can be changed during program execution.',
    'Function': 'A function is a block of code that only runs when it is called.',
    'Loop': 'A loop is a control structure that repeats a block of code multiple times.',
    'Class': 'A class is a blueprint for creating objects in object-oriented programming.',
    'Dictionary': 'A dictionary is a collection of key-value pairs, where each key is unique.'
}
for name, description in glossary.items():
    print(f"{name}, {description}")

    # Printing the glossary without using .items()
#    for word in glossary:
#     print(f"{word}:\n{glossary[word]}\n")