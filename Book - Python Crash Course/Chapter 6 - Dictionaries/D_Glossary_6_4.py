# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) 
# by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 

# When you’re sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'Variable': 'A variable is a name given to a value that can be changed during program execution.',
    'Function': 'A function is a block of code that only runs when it is called.',
    'Loop': 'A loop is a control structure that repeats a block of code multiple times.',
    'Class': 'A class is a blueprint for creating objects in object-oriented programming.',
    'Dictionary': 'A dictionary is a collection of key-value pairs, where each key is unique.',
    'Algorithm': 'A step-by-step procedure for solving a problem or performing a task.',
    'Array': 'A collection of elements, typically of the same type, stored in a fixed-size sequence.',
    'Object': 'An instance of a class in object-oriented programming that contains data and methods.',
    'Recursion': 'A process where a function calls itself in order to solve a problem.',
    'Syntax': 'The rules that define the structure of statements in a programming language.'

}

for key, value in glossary.items():
    print(f"{key}:\n{value}\n")