import random

while(True):
    print("---Welcome to Rock Paper Scissors Game---")
    print("Press 0 for Rock, 1 for Paper, 2 for Scissors")
    Your_Choice = int(input("Your Choice:  "))
    Computer_Choice = random.randint(0,2)
    
    #-------------- Simple Logic ---------------
   
    # if Your_Choice == 0:
    #     if Computer_Choice == 0:
    #         print("Computer chose Rock\n")
    #         print("Draw")
    #     elif Computer_Choice == 1:
    #         print("Computer chose Paper\n")
    #         print("You lose")
    #     else:
    #         print("Computer chose Scissors\n")
    #         print("You win")
    
    # elif Your_Choice == 1:
    #     if Computer_Choice == 0:
    #         print("Computer chose Rock\n")
    #         print("You win")
    #     elif Computer_Choice == 1:
    #         print("Computer chose Paper\n")
    #         print("Draw")
    #     else:
    #         print("Computer chose Scissors\n")
    #         print("You lose")
   
    # elif Your_Choice == 2:
    #     if Computer_Choice == 0:
    #         print("Computer chose Rock\n")
    #         print("You lose")
    #     elif Computer_Choice == 1:
    #         print("Computer chose Paper\n")
    #         print("You win")
    #     else:
    #         print("Computer chose Scissors\n")
    #         print("Draw")
    # else:
    #     print("Wrong choice")
    
    # ---------- Logic with List/Dict ----------
    
    winning_pairs = {(0,2),(1,0),(2,1)}
    pairs = {0: "Rock", 1: "Paper", 2: "Scissors"}
    
    if Your_Choice == Computer_Choice:
        print(f"-----Draw-----\nYou chose {pairs[Your_Choice]} Computer chose {pairs[Computer_Choice]}")
          
    elif (Your_Choice,Computer_Choice) in winning_pairs:
        print(f"------You win------\nYou chose {pairs[Your_Choice]} Computer chose {pairs[Computer_Choice]}")
    else:
        print(f"------You lose------\nYou chose {pairs[Your_Choice]} Computer chose {pairs[Computer_Choice]}")
    
    
        
    play_again = int(input("Do you want to play again?     (Press 0 for No) (Press 1 for Yes) "))
    
    if play_again == 0:
        break
    elif play_again == 1:
        continue
    else:
        break
