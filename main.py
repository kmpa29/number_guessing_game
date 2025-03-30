""" A simple guessing game with difficulty levels and limited chances."""

import random

answer = random.randint(1, 100)
chances = 7

print("\n----Welcome to KMP's guessing game!----\n")
print("Depeding on your difficulty, you will have chances guess the answer.\n")
print("Once you reach 0, you will have one more chance to answer.\n")
print("You will have guesses displayed after each guess\n")
print("")

difficulty = int(input("Select your difficulty!\n"
      "1. Easy (7 Chances)\n"
      "2. Normal(5 Chances)\n"
      "3. Hard(3 Chances)\n"

      "\nEnter your choice: \n"
      ))

if difficulty == 1:
    print("\nYou chose easy, good choice, safe choice.")
    chances == chances

if difficulty == 2:
    print("\nYou chose normal, very good choice, not safe, not dangerous.")
    chances = 5

if difficulty == 3:
    print("\nMan, You're crazy. If you don't get it right its game over buddy!")
    chances = 3

print("Now lets begin!")

# The game's main loop!
while True:
    print("\nWhat number am I think of?")
    player_choice = int(input("Take a guess: "))

    if chances == 0:
        print("\n----You've lost all your chances! YOU LOSE!----")
        break

    if player_choice == answer:
        print("\n----You won!----")
        break

    elif player_choice > answer:
        print("\nToo high my guy, go down!")
        chances -= 1
        print(f"\nGuess left: {chances}")
        continue

    elif player_choice < answer:
        print("\nToo low! Go higher!")
        chances -= 1
        print(f"Guesses left: {chances}")
        continue

        

print("\nThanks for playing! Come back soon!\n")