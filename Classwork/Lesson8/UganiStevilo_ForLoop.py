import random

secret_num = random.randint(1, 10)
guess = -1

for x in range(5):
    try:
        guess = int(raw_input("Ugani stevilo: "))
    except ValueError:
        print "Vnesi celostvilsko vrednost"
        continue

    if guess == secret_num:
        print "Uganil si"
        break # break zakljuci samo eno zanko
    elif guess > secret_num:
        print "Ugibaj nizje, imas se " + str(5-x-1) + " poizkusov"
    elif guess < secret_num:
        print "Ugibaj visje, imas se " + str(5-x-1) + " poizkusov"
    else:
        pass # ukaz ki pomeni "pejt naprej" in najveckrat sluzi samo za placeholder
