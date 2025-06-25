# Maze Game

print("**Welcome to Treasure Island**\nYour mission is to find the treasure.\n")
path = input("So, treasure hunter, choose your path:\nLeft or Right: ").lower()

if path == "right":
    print("Oh no... Game Over! Wrong path.")

elif path == "left":
    print("Well done, treasure hunter! You have chosen the correct path.\n")
    print("Now, do you want to wait for the boat or swim across the river to the island?")
    
    decision = input("So, what's your decision?\nSwim or Wait: ").lower()
    
    if decision == "swim":
        print("Oh no... Game Over! A shark ate you.")
    
    elif decision == "wait":
        print("The boat has arrived, and you have reached the island.\n")
        print("There are 3 doors in front of you: Red, Blue, and Yellow.")
        
        door = input("Choose the door you want to enter: ").lower()
        
        if door == "red":
            print("Oh no... Game Over! Fire burned you.")
        
        elif door == "blue":
            print("Oh no... Game Over! A snake bit you.")
        
        elif door == "yellow":
            print("\n...Congratulations, treasure hunter...\n   ***You have won!***")
        
        else:
            print("That door doesn't exist. Game Over.")
else:
    print("That path does not exist. Game Over.")
