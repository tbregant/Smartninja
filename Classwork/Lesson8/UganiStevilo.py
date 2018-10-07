secret_num = 22
guess = -1

while secret_num != guess:
    try:
        guess = int(raw_input("Ugani stevilo: "))
    except ValueError:
        print "Vnesi celostvilsko vrednost"
        continue


    if guess == secret_num:
        print "Uganil si"
    elif guess > secret_num:
        print "Ugibaj nizje"
    elif guess < secret_num:
        print "Ugibaj visje"
    else:
        pass # ukaz ki pomeni "pejt naprej"
