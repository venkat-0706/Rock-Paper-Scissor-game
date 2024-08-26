#!/usr/bin/env python
# coding: utf-8

# # Rock,Paper,Scissor game (RPS)

# In[ ]:


import random

def fun_game():
  """Plays a single round of Rock, Paper, Scissor."""
  options = ["rock", "paper", "scissor"]
  user_choice = input("Choose rock, paper, or scissor: ").lower()
  computer_choice = random.choice(options)

  if user_choice not in options:
    print("Invalid choice. Please choose rock, paper, or scissor.")
    return

  print(f"You chose: {user_choice}")
  print(f"Computer chose: {computer_choice}")

  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == "rock" and computer_choice == "scissor") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissor" and computer_choice == "paper"):
    print("You win!")
  else:
    print("Computer wins!")

while True:
  fun_game()
  play_again = input("Do you want to play again? (yes/no): ").lower()
  if play_again != "yes":
    break

