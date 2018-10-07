import random

secret_num = random.randint(1, 10)
guess = -1

while True:
    try:
        guess = int(raw_input("Ugani stevilo: "))
    except ValueError:
        print "Vnesi celostvilsko vrednost"
        continue
    if guess == secret_num:
        print "Uganil si"
        break # break zakljuci samo eno zanko
    elif guess > secret_num:
        print "Ugibaj nizje"
    elif guess < secret_num:
        print "Ugibaj visje"
    else:
        pass # ukaz ki pomeni "pejt naprej"
