# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 4 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
hand_value = draw_starting_hand("your turn")
while hand_value < 21:
    user_input = input(f"You have {hand_value}. Hit (y/n)? ")
    if user_input == "y":
        hand_value += draw_card()
    elif user_input == "n":
        break
    else:
        print("Sorry I didn't get that.")
print_end_turn_status(hand_value)
d_hand_value = draw_starting_hand("dealer turn")
while d_hand_value < 17:
    print(f"Dealer has {d_hand_value}.")
    d_hand_value += draw_card()
print_end_turn_status(d_hand_value)

print_end_game_status(hand_value, d_hand_value)
