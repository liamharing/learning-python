#!/usr/bin/env python3

# This is Exercise Four of Learning Python
# This exercise focuses on loops

print("Welcome to Excercise Four of learning Python!")

coffeeInStock = int(input("\nHow many coffees do you want to put in stock? Enter an integer: "))

print(f"You have put {coffeeInStock} coffees in stock.\n")

while True:
    userCoffee = input("Do you want to order a coffee? Type yes or no (or press Enter to exit): ")
    
    if userCoffee == "":
        break
    elif userCoffee == "yes":
        if coffeeInStock > 0:
            coffeeInStock = coffeeInStock - 1
            print(f"\nOne coffee has been subtracted from stock. Remaining coffees are {coffeeInStock}")
        else:
            print("\nStock is empty already? Have you drunk all the coffee again??")
            break
    elif userCoffee == "no":
        print("\nYou don't want coffee?? Stock will remain the same.")
    else:
        print("\nYou didn't supply a valid string.")

print("\nThank you for completing this exercise!")