import random

def isNumber(number):
    while (not number.isdigit()) or (not 0 < int(number) < 101):
        if not number.isdigit():
            print "That's not a number.  Try again!"
        else:
            print "That's not between 1 and 100! Try again!"  

        number = raw_input("Your guess? ")

    number = int(number)
    return number

name = raw_input("Hello! What's your name? ")
if name == "":
    print "Don't want to tell me your name?  Fine.  You are now Bob."
    name = "Bob"

print (name + ", I'm thinking of number between 1 and 100.  Guess it!")

gameCount = 0
playAgain = True

# Play a (new) guessing game with user
while playAgain:
    number = random.randint(0, 100)
    gameCount += 1
    guessCount = 0
    guessRight = False
    guessList = []

    # Keep getting new guesses until user guess correct number
    while guessRight == False:

        guess = raw_input("Your guess? ")
        
        # check if guess is Not a Number (True if not) or if its out of bounds 1-100
        guess = isNumber(guess)

        guessCount += 1 
        guessList.append(guess)   

        if guess < number:
            print "Your guess is too low, try again!"
        elif guess > number:
            print "Your guess is too high, try again!"
        else:
            guessRight = True
            print "you got it"

    # Print user's results
    print ("You had " + str(guessCount) + " guesses")

    print "Here are your guesses:",
    for guesses in guessList:
        print guesses,

    # initialize bestScore for first game
    if gameCount == 1:
        bestScore = guessCount

    # update bestScore
    if guessCount < bestScore:
        bestScore = guessCount

    print ("\nYour current best score is " + str(bestScore))

    # Determine if user wants to play again
    newGame = raw_input("Want to play again? y/n ")
    if newGame in ["y", "Y", "yes", "Yes", "YES", "yup", "ok", "OK", "Ok"]:
        playAgain = True
    elif newGame in ["n", "N", "no", "No", "NO", "nope"]:
        playAgain = False
    else:
        print "You suck.  I'm starting a new game for you anyway you ass."

