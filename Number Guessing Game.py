#Number Guessing Game
import random
def game():
    secret = random.randint(1,100)
    guess = 0
    turns = 0
    max_turns = 10

    while True:
        print("Guess a whole number between 1 and 100.")
        guess = int(input())
        turns += 1
        if turns == max_turns:
            print("You lose, max attempts reached. Good effort though, try again!")
            break
        elif guess < secret:
            print("Too low. You are at %d /10 turns" % turns)
        elif guess > secret:
            print("Too high. You are at %d /10 turns" % turns)
        else:
            print("You got it!")
            break  # exit the loop
       
    #endwhile
    print("Done with game.")
    print("It took %d turns" % turns)

if __name__ == "__main__":
    game()
