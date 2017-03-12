import random

#random 4-digit number generator
number = []
for i in range(4):
    digit = random.randrange(0,10)
    while digit in number:
        digit = random.randrange(0,10)
    number.append(digit)
    if number[0] == 0:
        number[0] = random.randrange(1,10)

# print(number)

def compare(number,guess_num):
    """ Compare the random number with the players's guess and return the bulls and cows."""
    bull_cow = [0,0] # bulls, then cowws
    for x in range(4):
        if number[x] == guess_num[x]:
            bull_cow[0] = bull_cow[0] + 1
        elif number[x] in guess_num:
            bull_cow[1] = bull_cow[1] + 1
    return bull_cow

def game_evaluator(num_of_guesses):
    """Evaluate the game."""
    if num_of_guesses < 5:
        print("That's amazing!")
    elif num_of_guesses < 10:
        print("Thats's average.")
    else:
        print("Hey bro, that's really bad. Shame on you!")

def game_score(bull_cow):
    """ Give the state of game and make distinction between singular and plural."""
    if bull_cow[0] == 1 and bull_cow[1] == 1:
        print(bull_cow[0], "bull", bull_cow[1], "cow")
    elif bull_cow[0] != 1 and bull_cow[1] == 1:
        print(bull_cow[0], "bulls", bull_cow[1], "cow")
    elif bull_cow[0] == 1 and bull_cow[1] != 1:
        print(bull_cow[0], "bull", bull_cow[1], "cows")
    else:
        print(bull_cow[0], "bulls", bull_cow[1], "cows")

# Actual game...
print ("Hi there!")
print ("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
num_of_guesses = 0

while True:
    guess_num = []
    guess = input("Enter a number:\n")
    if len(guess) != 4:
        guess = input("Your guess must be 4 digit number. Try again:\n")
    for digit in guess:
        guess_num.append(int(digit))

    bull_cow = compare(number, guess_num)
    game_score(bull_cow)
    num_of_guesses = num_of_guesses + 1

    if bull_cow[0] == 4:
        print("Correct! You've guessed the right number in", num_of_guesses, "guesses!")
        game_evaluator(num_of_guesses)
        break
    else:
        print("Try again.")
