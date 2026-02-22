#!/usr/bin/env python3

# This is Exercise Two of Learning Python
# This exercise focuses on learning about variables and datatypes

print("Welcome to Excercise One of learning Python!")

userInt = int(input("\nPlease type an integer: "))
userFloat = float(input("\nPlease type a float: "))
userString = str((input("\nPlease type a string: ")))
userBoolean = input("\nPlease type a boolean value (true/false). This will either show the previous inputs or it will not: ")

if userBoolean.lower() == "true":
    print("\n\nYou have chosen to view your inputs. Here you go: ")
    print(f"\n {userInt, userFloat, userString}")
else:
    print("\nYou don't want to see your inputs?\nThank you for completing this exercise anyways!")