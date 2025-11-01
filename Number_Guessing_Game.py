#Number Guessing Game
#Welcome the player
print("Welcome to Brooklyn's Number Guessing Game")
#Randomize the numbers from 1-100
import random
mixed = [1, 100]
#The player gets 5 attempts to guess the number
max_guesses = 5
#The player decides whether to play or exit the game
while True:
#If the player decides to exit the game. The game ends.
    game = input("Enter 'Play'to start game or 'Exit' to leave game: \n")
    if game == "Exit": 
        print("End of game")
        break
#If the player decides to play the game. The guessing game begins.
    elif game == "Play":
        guess_number = random.randint(mixed [0], mixed [1])
        guess_count = 0
#Tell the player the rules of the game.
        print(f"I have a number in mind. This number ranges from 1-100. Can you guess this number?")
        print(f"You have {max_guesses} guesses remaining.\n")
        while guess_count < max_guesses: 
#The player is told to guess the number
            user_guess = int(input("Enter your guess: "))
#After every guess the guess count goes up by 1
            guess_count += 1
#If the guess is greater than the random number, the player is told to try again.
            if user_guess > guess_number :
                print("Too high. Try again.\n")
#If the guess is less than the random number, the player is told to try again.
            elif  user_guess < guess_number:
                print("Too low. Try again.\n")
#If the guess is correct, then player wins the game
            else:
                print (f"Congrats, {user_guess} is the correct number.")
                print(f"You got it in {guess_count} attempts!")
                print (f"End of session")
                break
#if the player uses up all his guesses, then the game comes to an end.
        else: 
            print(f"You are out of guesses.")
            print(f"The correct number was {guess_number}")
#Once the game is over the session ends.
    break        


        
