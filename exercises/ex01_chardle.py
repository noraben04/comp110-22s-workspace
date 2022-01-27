"""EX01 - Chardle - A step toward Wordle."""

__author__ = "730437270"

user_input: str = input("Enter a 5-character word: ")
if len (user_input)!= 5:
     print("Error: Word must contain 5 characters")
     exit()

user_char: str = input("Enter a single character: ")
user_inst: int = 0
if len (user_char) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + user_char + " in " + user_input)

if user_char == user_input[0]:
    print(user_char + " found at index 0")
    user_inst = user_inst + 1
if user_char == user_input[1]:
    print(user_char + " found at index 1")
    user_inst = user_inst + 1
if user_char == user_input[2]:
    print(user_char + " found at index 2")
    user_inst = user_inst + 1
if user_char == user_input[3]:
    print(user_char + " found at index 3")
    user_inst = user_inst + 1
if user_char == user_input[4]:
    print(user_char + "found at index 4")
    user_inst = user_inst +1

if user_inst == 0:
    print("No instances of " + user_char + " found in " + user_input)
else: 
    if user_inst == 1:
        print("1 instance of " + user_char + " found in " + user_input)
    else: 
        print( str(user_inst) + " instances of" + user_char + " found in " + user_input) 


