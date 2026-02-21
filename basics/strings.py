#!/usr/bin/env python3

#This is Exercise Five of Learning Python
#This exercise focuses on learning about strings and related operations

print("Welcome to Excercise Five of learning Python! \n")

name = (input("Please enter a 'name' to test out this Episodes funcionalities: "))

print()

print("Here is every character of your name on a new line: ")
for x in name :
    print(x)

print()

print("This is your name in Upper Case:\n",name.upper())
print("\nAnd this is your name in Lower Case:\n",name.lower())

print("\n\nThank you for completing this exercise!")