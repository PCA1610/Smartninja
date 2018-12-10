secret = 22

while True:
    guess = int(raw_input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print "You guessed it - congratulations! It's number 22 :)"
        break
    elif guess > secret:
        print "Your guess is to height"
    elif guess < secret:
        print "Your guess is to small"
    else:
        print "Sorry, your guess is not correct... Secret number is not " + str(guess)
