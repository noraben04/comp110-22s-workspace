"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("what is your guess? "))

if guess == SECRET: 
    print("you guessed correctly!!!")
    print("Have a wonderful day!!!")
else:
    print("sorry, you guessed incorrectly :(")
    print("try try try again")

print("Game over.")