import random


def main():
    country_capital_dict = {"Slovenia": "Ljublijana", "Austria": "Vienna", "Czech": "Prag", "Germany": "Berlin"}

    while True:
        rand_value = random.randint(0, 3)

        print ("Hey, Nice to see you at the awsome country quiz!")

        select_country = country_capital_dict.keys()[rand_value]
        user_input = raw_input("Do you know the capital of %s? " % select_country)

        check_guess(user_input, select_country, country_capital_dict)

        again = raw_input("Would you like to stop the game? (yes/no) ")
        if again == "yes":
            break

    print "Ende"
    print "__________________"

def check_guess(user_input, country, cc_dict):
    capital = cc_dict[country]

    if user_input == capital:
        print "Correct! The capital of %s is %s." % (country, capital)
        return True
    else:
        print "Sorry, wrong answer, the capital of %s is not %s." % (country, capital)
        return False


if __name__ == "__main__":
    main()
