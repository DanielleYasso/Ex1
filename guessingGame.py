import random

def isNumber(number):
    while not number.isdigit():
        print "That's not a number.  Try again!"
        number = raw_input("Your guess? ")

    number = int(number)
    return number

name = raw_input("Hello! What's your name? ")

print (name + ", I'm thinking of number between 1 and 100.  Guess it!")

gameCount = 0

playAgain = True

while playAgain == True:
    number = random.randint(0, 100)
    gameCount += 1

    guessCount = 0
    guessRight = False
    guessList = []

    while guessRight == False:

        guess = raw_input("Your guess? ")
        
        # check if guess is Not a Number (True if not)
        guess = isNumber(guess)

        while not 0 < guess < 101:
            print "That's not between 1 and 100! Try again!"
            guess = raw_input("Your guess? ")
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


    print ("You had " + str(guessCount) + " guesses")

    print "Here are your guesses:",
    for guesses in guessList:
        print guesses,

    if gameCount == 1:
        bestScore = guessCount

    # update bestScore
    if guessCount < bestScore:
        bestScore = guessCount

    print ("\nYour current best score is " + str(bestScore))

    newGame = raw_input("Want to play again? y/n ")
    if newGame == "y":
        playAgain = True
    elif newGame == "n":
        playAgain = False
    else:
        print "You suck.  I'm starting a new game for you anyway you ass."

