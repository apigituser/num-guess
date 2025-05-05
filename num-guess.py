import random
import datetime

def checkGuess():
    startTime = datetime.datetime.now()
    for attempts in range(1, chances+1):
        guess = int(input("Enter your guess -> "))
        if guess == answer:
            endTime = datetime.datetime.now() - startTime
            print(f"Congratulations! You guessed the correct number in {attempts} attempts")
            print(f"And it only took you {endTime.seconds} seconds!")
            break
        elif guess > answer:
            print(f"Wrong! The number is smaller than {guess}")
        else:
            print(f"Wrong! The number is greater than {guess}")
    

if __name__ == '__main__':
    print('''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n
''')
    level = {1: "Easy", 2: "Medium", 3: "Hard"}
    choice = int(input("Enter your choice -> "))

    print(f"\nGreat! You have selected the {level[choice]} difficulty level.")
    print("Let's start the game!\n")
    play = 'yes'


    match choice:
        case 1: chances = 10
        case 2: chances = 5
        case 3: chances = 3

    while(play == 'yes'):
        answer = random.randint(1,100)
        checkGuess()
        play = input("Do you wish to try again? (yes/no): ").lower()
    print("Thank you for playing the game!")
    print("See you later!")