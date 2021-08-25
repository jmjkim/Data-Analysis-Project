# Guessing a random number
from random import randint

def game_start():
    """Guess a random number between 1 - 30. Enter '999' to quit the game. Enter '9999' to reveal the hidden number"""

    print("\nGuess a random number between 1 - 30\n*** Enter '999' to quit the game ***\n*** Enter '9999' to reveal the hidden number ***\n")
    x = randint(1, 30)
    count = 0

    while True:
        try:
            guess = int(input(("\nEnter your guess here: ")))
            count += 1

            if guess == int(str('999')):
                print("\nThank you for playing!\n")
                break

            if guess == int(str('9999')):
                print(f"\nThe hidden number was {x}.\n")
                break

            if guess == x:
                print(f"\nYou have guessed the hidden number! The number was {x}.\n*** You took {count} times to guess the number ***\n")

                cont = input("Try again? Y / N: ")

                if cont == 'Y'.lower():
                    return myfunction()

                else:
                    print("\nThank you for playing!\n")
                    break

            if guess < x:
                print(f"Try guess higher!")

            if guess > x :
                print(f"Try guess lower!")

            if x - 3 <= guess <= x + 3:
                print(f"Your guessing is close!")

        except ValueError:
            print("Your guess must be a number!")

game_start()