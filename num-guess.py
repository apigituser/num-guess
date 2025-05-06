import random
import datetime
import json

def welcomeMessage():
    print("Number Guessing Game")
    print("You have to guess a number between 1-100")
    print("These are the difficulty levels")
    print("1 -> Easy (10 chances)\n2 -> Medium (5 chances)\n3 -> Hard (3 chances)\n")

def checkGuess():
    startTime = datetime.datetime.now()
    for attempts in range(1, chances+1):
        guess = int(input("Enter your guess -> "))
        if guess == answer:
            endTime = datetime.datetime.now() - startTime
            print(f"Congrats, You guessed the correct number in {attempts} attempts")
            print(f"Which took you {endTime.seconds} seconds")
            break
        elif guess > answer:
            print(f"Not quite, The number is smaller than {guess}")
        else:
            print(f"Try again, The number is greater than {guess}")
    return attempts

if __name__ == '__main__':
    welcomeMessage()
    
    while True:
        choice = input("Choose one -> ")
        if choice not in ('1','2','3'):
            print("Select a valid level [1,2,3]")
            continue
        break
    
    play = 'yes'
    main = {'1': ["Easy", 10, 10], '2': ["Medium", 5, 5], '3': ["Hard", 3, 3]}      ## {choice : [ level , chances, highscore ]}
    level = main[choice][0]
    chances = main[choice][1]
    highscore = main[choice][2]

    print("Alright then\nLet's start the game :)\n")

    while(play == 'yes'):
        answer = random.randint(1,100)
        attempts = checkGuess()
        if attempts < highscore:
            highscore = attempts
            print(f"Congrats! You achieved a new high score!\n{attempts} attempts at {level} level!")    
        play = input("Do you wish to try again? (yes/no): ").lower()
        
    print("Thank you for playing the game!")
    print("See you later!")