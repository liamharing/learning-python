#!/usr/bin/env python3

# This is Exercise Seven of Learning Python
# This exercise focuses on Lists, Sets and Tuples

print("Welcome to Excercise Seven of learning Python!")

# Lists
nameList = ['alice', 'bob', 'dylan', 'jeremy']
brandList = ['apple', 'nothing', 'microsoft', 'samsung']

chosenName = int(input("\nPlease submit a number from 0-3 to see your chosen name: "))
chosenBrand = int(input("Please submit a number from 0-3 to see your chosen brand: "))

print(f"\nYour chosen name is \"{nameList[chosenName]}\" and your chosen brand is \"{brandList[chosenBrand]}\"")

# Sets
input1 = input("\n\nPlease enter 5 digits seperated by whitespace: ").split()
input2 = input("Please enter 5 digits seperated by whitespace again: ").split()

if len(input1) != 5 or len(input2) != 5 :
    print("Error: Please make sure you enter 5 digits for both inputs and don't forget whitespace")
else :
    set1 = set(input1)
    set2 = set(input2)
    intersection = set1.intersection(set2)

    if intersection :
        print(f"\nThe intersection of your digits is: {intersection}")
    else :
        print("There is no intersection between your digits")

# Tuples
coordinates = (10, 20, 35)

print(f"\n\nWe have stored 3D coordinates in a tuple: {coordinates}")

x, y, z = coordinates

print(f"The x value is {x}")
print(f"The y value is {y}")
print(f"The z value is {z}")


print("\n\nThank you for completing this exercise!")