# A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; 
# and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, 
# and then tell them the cost of their movie ticket.
while True:
    person_age = input("Enter the ages ")
    if person_age == 'finish':
        break
 
    person_age = int(person_age)


    if person_age < 3:
        print("You get in free!")
    elif 3 <= person_age < 12:
        print("Your ticket is $10!")
    elif person_age > 12:
        print("Your ticket is $15!")
        
