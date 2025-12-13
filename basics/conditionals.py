#!/usr/bin/env python3

#This is Exercise Three of Learning Python
#This exercise focuses on conditionals

print("Welcome to Excercise Three of learning Python!")

product1 = float(input("\nPlease provide the price for product1 as a float with 2 decimal places (no currency symbol) or press Enter to exit: "))
product2 = float(input("\nPlease provide the price for product2 as a float with 2 decimal places (no currency symbol) or press Enter to exit: "))
product3 = float(input("\nPlease provide the price for product3 as a float with 2 decimal places (no currency symbol) or press Enter to exit: "))

totalProductCost = product1 + product2 + product3

if totalProductCost <= 50:
    print("\nThe total cost of your products is below 50. This adds 15 to your total for shipping costs.")
    print(f"\nThis brings your total with shipping to {totalProductCost + 15:.2f}")
elif 50 < totalProductCost <= 100:
    print(f"\nYour total is {totalProductCost:.2f}. Shipping is 10.")
    print(f"\nThis brings your total with shipping to {totalProductCost + 10:.2f}")
elif totalProductCost > 100:
    print(f"\nYour total is {totalProductCost:.2f}. Free shipping!")

print("\nThank you for completing this exercise!")