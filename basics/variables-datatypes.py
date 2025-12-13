#!/usr/bin/env python3

#This is Exercise Two of Learning Python
#This exercise focuses on learning about variables and datatypes

print("Welcome to Excercise One of learning Python!")

userInt = int(input("\nPlease type an integer: "))
userFloat = float(input("\nPlease type a float: "))
userComplex = complex(input("\nPlease type a complex: "))
userString = str((input("\nPlease type a string: ")))
userBoolean = bool((input("\nPlease type a boolean value. This will either show the previous inputs or it will not: ")))

if userBoolean == True :
    print("\n\nYou have chosen to view your inputs. Here you go: ")
    print("\n" + userInt, userFloat, userComplex, userString)

print("\nThank you for completing this exercise!")