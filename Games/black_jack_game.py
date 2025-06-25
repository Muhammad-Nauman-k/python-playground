# ----- Welcome to Blackjack Game -----
import random

Deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # The 3 extra 10's are for Jack,Queen,King and 11 is for ACE
You_1 = []
Computer_2 = []

n = len(Deck_of_cards) - 1

# -------- Draw a Card Function --------
def draw_a_card(player):
    randomize = random.randint(0, n)
    player.append(Deck_of_cards[randomize])

# -------- Check Total Score Function --------
def get_score(player_cards):
    return sum(player_cards)

# -------- First Draw: 2 Cards Each --------
for _ in range(2):
    draw_a_card(You_1)
    draw_a_card(Computer_2)

# -------- Print Initial State --------
print(f"Player has: {You_1}")
print(f"Computer shows: {Computer_2[0]}")

# -------- Computer draws a third card if score < 16 --------
if get_score(Computer_2) < 16:
    draw_a_card(Computer_2)

# -------- Player turn: Draw more cards --------
while True:
    draw_again = input("Do you want to draw another card? (y/n): ").lower()
    if draw_again == 'y':
        draw_a_card(You_1)
        print(f"After another card, you now have: {You_1}")
    elif draw_again == 'n':
        break

# -------- Handle ACE as 1 if score > 21 --------
def adjust_aces(cards):
    while sum(cards) > 21 and 11 in cards:
        cards[cards.index(11)] = 1

adjust_aces(You_1)
adjust_aces(Computer_2)

# -------- Final Scores --------
Final_score_Player_1 = get_score(You_1)
Final_score_Player_2 = get_score(Computer_2)

# -------- Determine Winner --------
if Final_score_Player_1 > 21:
    print(f"----- You lost! Score over 21 -----   Your Score: {Final_score_Player_1}")
elif Final_score_Player_2 > 21:
    print(f"----- Computer lost! Score over 21 -----   Computer Score: {Final_score_Player_2}")
elif Final_score_Player_1 == Final_score_Player_2:
    print("The game is a draw!")
elif Final_score_Player_1 > Final_score_Player_2:
    print(" You won the game!")
else:
    print(" Computer won the game!")

# -------- Final Output --------
print(f"\nPlayer Final Score: {Final_score_Player_1}")
print(f"Computer Final Score: {Final_score_Player_2}")

print(f"Player Cards: {You_1}")
print(f"Computer Cards: {Computer_2}")
