import random

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
    chances = {1: 10, 2: 5, 3: 3}
    choice = int(input("Enter your choice -> "))

    print(f"\nGreat! You have selected the {level[choice]} difficulty level.")
    print("Let's start the game!\n")

    answer = random.randint(1,100)

    match choice:
        case 1: chances = 10
        case 2: chances = 5
        case 3: chances = 3
    
    for attempts in range(1, chances+1):
        guess = int(input("Enter your guess -> "))
        if guess == answer:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts")
            break
        elif guess > answer:
            print(f"Wrong! The number is smaller than {guess}")
        else:
            print(f"Wrong! The number is greater than {guess}")