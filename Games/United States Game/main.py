import turtle
import pandas as pd

# Set up the screen and map
screen = turtle.Screen()
screen.title("United States Guess Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)  

df = pd.read_csv("50_states.csv")


count = 0
guessed_states = []

while len(guessed_states) < len(df["state"]):
    
    answer_state = turtle.textinput(title=f"{count}/{len(df['state'])} Correct Guess", prompt="Guess the State's name") # Ask the user to guess a state name

    if answer_state is None or answer_state.lower() == "exit":   # Exit the game 
        break

    # Format the input to match the capitalization of state names
    checker = answer_state.title()

    if checker in df["state"].values and checker not in guessed_states:       # Check if the guessed state is in the dataset
        guessed_states.append(checker)
        count+= 1
        
        row = df[df["state"] == checker]    # Get the row for the guessed state
        x_cord = int(row["x"].item())
        y_cord = int(row["y"].item())

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x_cord, y_cord)
        writer.write(answer_state, font=("Arial", 8, "normal"))

screen.exitonclick()
