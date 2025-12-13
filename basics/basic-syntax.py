#!/usr/bin/env python3

#This is Exercise One of Learning Python
#This exercise focuses on basic syntax mixed with user input

word = "One"
sentence = "This is excercise One"
paragraph = "This is a multiline paragraph featuring\ntwo lines of text"

print("Welcome to Excercise One of learning Python!")

while True:
    userChosenNumber = input("\nPlease enter a number between 1 and 3 to access the prepared variables (or press Enter to exit): ")
    
    if userChosenNumber == "":
        break
    elif userChosenNumber == "1":
        print("\n" + word)
    elif userChosenNumber == "2":
        print("\n" + sentence)
    elif userChosenNumber == "3":
        print("\n" + paragraph)
    else:
        print("\n\nYou didn't enter a valid number. Please try again.")

print("\nThank you for completing this exercise!")