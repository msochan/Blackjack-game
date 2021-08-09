import random
from art import logo


def calculate_score(cards):
  score = 0
  for card in cards:
    if card == 11 and score > 21:
      card = 1
      score += card
    else:
      score += card
  #checking blackjack condition
  if len(cards) == 2 and score == 21:
    score = 0
  return score

def draw_card(deck):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  deck.append(random.choice(cards))

def check_win_condition_info(player_score, computer_score):
    if player_score == computer_score:
      print("We've got DRAW!")
    elif computer_score == 0:
      print("You've lose, computer got blackjack!")
    elif player_score == 0:
      print("You've got blackjack, you win!")
    elif player_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21:
        print("Opponent went over. You win!")
    elif player_score > computer_score:
        print("You are closer to blackjack. You win!")
    else:
        print("Computer are closer to blackjack. You lose!")    

def black_jack_game():
  player_cards = []
  computer_cards = []
  for range in (0,2):
    draw_card(player_cards)
    draw_card(computer_cards)

  player_score = calculate_score(player_cards)
  computer_score =  calculate_score(computer_cards)
  
  start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if start_game == 'y':
    print(logo)
    continue_game = True
    another_card = ""
    while continue_game:
      print(f"Your cards: {player_cards}, current score: {player_score}")
      print(f"Computer's first card: {computer_cards[0]}")
      
      if player_score > 21 or player_score == 0 or computer_score == 0 or another_card == 'n':
        continue_game = False
        while computer_score <= 16:
          draw_card(computer_cards)
          computer_score =  calculate_score(computer_cards)
        player_score = calculate_score(player_cards)
    
        print(f"Your final cards: {player_cards}, final score: {player_score}")
        print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
        check_win_condition_info(player_score, computer_score)
        black_jack_game()
        return

      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card == 'y':
        draw_card(player_cards)
        player_score = calculate_score(player_cards)
##############
##############

black_jack_game()