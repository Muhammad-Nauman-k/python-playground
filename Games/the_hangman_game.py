# The Hangman Game
import random

list_of_animals = ['cow', 'sheep', 'buffalo', 'snake', 'zebra', 'cat']

print("Guess the animal name: ", end='')
len_of_animals = len(list_of_animals) - 1

the_name = []
tries = 7

randomize = random.randint(0, len_of_animals)
random_animal = list_of_animals[randomize]     # Choose a random name from the list
dashes_list = []

for i in random_animal:   # Put dashes in place of the name's letters for the user to guess
    the_name.append(i)
    dashes_list.append('-')
    print('-', end='')

while tries > 0:       # While tries are not zero
    counter = 0
    guess = input("\nGuess: ")

    for i in the_name:
        if i == guess:
            dashes_list[counter] = i
        counter += 1

    print(''.join(dashes_list))  # Join the dashes to show the user the current progress

    if guess not in the_name:
        tries -= 1
        print(f"Wrong guess! {tries} tries left")

    # Check if the player has guessed all letters
    if dashes_list == the_name:
        print("\nCongratulations! You guessed the word correctly 🎉")
        break

if dashes_list != the_name and tries == 0:
    print(f"\nGame Over! The correct word was: {random_animal}")
