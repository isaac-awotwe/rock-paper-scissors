#! /usr/bin/python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rps_choice_list = ["Rock", "Paper", "Scissors"]
ascii_arts = [rock, paper, scissors]

computer_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))


try:

    print(f"You chose {rps_choice_list[user_choice]}:")
    print(ascii_arts[user_choice])

    print(f"Computer chose {rps_choice_list[computer_choice]}:")
    print(ascii_arts[computer_choice])

    if user_choice == 0:
        if computer_choice == 0:
            print("It's a draw!")
        elif computer_choice == 1:
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You win!")
        elif computer_choice == 1:
            print("It's a draw!")
        else:
            print("You lose!")
    elif user_choice == 2:
        if computer_choice == 0:
            print("You lose!")
        elif computer_choice == 1:
            print("You win!")
        else:
            print("It's a draw!")

except:
    print("You typed an invalid number; you lose!)")

