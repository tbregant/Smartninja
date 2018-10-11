import random

country_capital_dict = {
    "Slovenia": "Ljubljana",
    "Borneo": "Maribor",
    "Hrvaska": "Zagreb",
    "Hungary": "Budapest"
}


def check_guess(country, user_guess, ccd):
    if ccd[country].lower() == user_guess.lower().strip(" "):
        return True
    return False

def select_random_country(ccd):
    keys = ccd.keys()
    random_key = random.choice(keys)
    return random_key

def game():
    random_country = select_random_country(country_capital_dict)

    while True:
        user_guess = raw_input("Capital of {} is?".format(random_country))

        if check_guess(random_country, user_guess, country_capital_dict):
            print "Yout guessed, capital {} is really {}".format(random_country, user_guess.capitalize())
            break
        else:
            print "Looser"


game()

#if __name__ == '__main__':
#    print check_guess("Slovenia", "Ljubljana", country_capital_dict)
#    print select_random_country(country_capital_dict)
