import random
import datetime

def welcomeMessage():
    print("Number Guessing Game")
    print("You have to guess a number between 1-100")
    print("These are the difficulty levels")
    print("1 -> Easy (10 chances)\n2 -> Medium (5 chances)\n3 -> Hard (3 chances)\n4 -> IMPOSSIBLE (1 chance ONLY)\n")

def guessInput():
    while True:
        try:
            guess = int(input("Enter your guess -> "))
            if (guess > 100) or (guess < 1):
                print("The number should be between 1-100")
                continue
            return guess
        except ValueError:
            print("That's not a number")
            continue

def checkGuess(chances, answer):
    startTime = datetime.datetime.now()
    
    for attempts in range(1, chances + 1):
        guess = guessInput()
        if guess == answer:
            endTime = datetime.datetime.now() - startTime
            print(f"Congrats, You guessed the correct number in {attempts} attempts")
            print(f"Which took you {endTime.seconds} seconds")
            return attempts
        elif guess > answer:
            print(f"WRONG! It's lower")
        else:
            print(f"INCORRECT! It's Higher")
    
def selectLevel():
    while True:
        choice = input("Choose one -> ")
        if choice not in ('1','2','3','4'):
            print("Select a valid level (1,2,3) or 4 (if you're feeling lucky)")
            continue
        return choice

def main():
    welcomeMessage()

    choice = selectLevel()
    
    play = 'yes'
    settings = {'1': ("Easy", 10), '2': ("Medium", 5), '3': ("Hard", 3), '4': ("Impossible", 1)}
    level, chances = settings[choice]
    highscore = chances

    while(play == 'yes'):
        answer = random.randint(1,100)
        attempts = checkGuess(chances, answer)
        
        if attempts == None:
            print("You ran out of chances")
            print("Good luck next time\n")
        elif attempts < highscore:
            highscore = attempts
            print(f"Congrats! You achieved a new high score!\n{attempts} attempts at {level} level!\n")
        play = input("Do you wish to try again? (yes/no): ").lower()

    print("Quitting Game ...")
    print("... see you later")


if __name__ == '__main__':
    main()