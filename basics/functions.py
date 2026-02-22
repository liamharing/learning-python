#!/usr/bin/env python3

# This is Exercise Six of Learning Python
# This exercise focuses on Functions

print("Welcome to Excercise Six of learning Python!")

def greeting(name) :
    print(f"\nHello, {name}!")

def calculateCost(item, quantity, cost) :
    print(f"\n\n{quantity} of \"{item}\" cost ${quantity * cost:.2f}")

def findUser(username, userList) :
    for user in userList :
        if user["username"] == username :
            return user
    return None
    
users = [
    {"username" : "alice"},
    {"username" : "bob"},
    {"username" : "jeremy"},
    {"username" : "dylan"},
]

# Function greeting
userName = input("Type your name to be greeted: \n")

greeting(userName)

# Function calculateCost
userItem = str(input("\nWhat item do you want to calculate the cost of? \n"))
userQuantity = int(input(f"How many \"{userItem}\" do you have? \n"))
userCost = float(input(f"How much does {userItem} cost? \n"))

calculateCost(userItem, userQuantity, userCost)

# Function findUser
suppliedUsername = str(input("\n\nType the username to search for: "))

foundUser = findUser(suppliedUsername, users)

if foundUser:
    print(f"Found user: {foundUser}")
else:
    print("User not found.")

print("\n\nThank you for completing this exercise!")