#Tip and Fare Calculator
print("Welcome to Tip and Fare Calculator")
Tbill = float(input("What is the total Bill?\n$"))
Tip = int(input("How much would you like to Tip: <10,12,15>\n$"))
Tpeeps = int(input("How many people are there to split the Bill:\n"))

TTip = Tbill / 100 * Tip

Bill = (Tbill + TTip) / Tpeeps

print(f"Fare on each person is: {round(Bill, 2)}$ ")
