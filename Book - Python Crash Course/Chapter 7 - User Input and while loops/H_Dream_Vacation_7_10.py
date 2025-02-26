# Write a program that polls users about their dream vacation. Write a prompt similar
# to If you could visit one place in the world, 
# where would you go? Include a block of code that prints the results of the poll.

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place
    
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break
# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
