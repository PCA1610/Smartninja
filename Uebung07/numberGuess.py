import random


def main():

    rant_value = random.randint(1, 100)

    for x in range(0, 7):
        guess = int(raw_input("Guess the secret number (between 1 and 100): "))

        if guess == rant_value:
            print "You guessed it - congratulations! It's number %d :)" % (rant_value)
            break
        elif guess > rant_value:
            print "Your guess is to height"
        elif guess < rant_value:
            print "Your guess is to small"
    print "Game Over!!!! You only have 7 guesses."


if __name__ == "__main__":
    main()
