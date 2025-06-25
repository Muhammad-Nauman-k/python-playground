# Silent Bid Competition

import os

def clear_screen():
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:  # For Mac, Linux, etc.
        os.system('clear')

print("---- Welcome to the Silent Bid Competition ----\n")
bidders = {}
checkpoint = True

while checkpoint:
    name = input("What is your name: ").title()
    bid = int(input("Enter your bid amount: $"))
    bidders[name] = bid

    another_one = input("Is there another bidder? (y/n): ").lower()
    
    clear_screen()  # Clear the screen so next bidder can't see

    if another_one == 'n':
        checkpoint = False

highest_bidder_bid = 0
highest_bidder = "No one"

for key in bidders:
    if bidders[key] > highest_bidder_bid:
        highest_bidder_bid = bidders[key]
        highest_bidder = key

print("\nAll Bids Recorded ")
print(f"\nThe competition is won by {highest_bidder} with a highest bid of ${highest_bidder_bid}.")
