secret_num = 22
guess = -1

while True:
    try:
        guess = int(raw_input("Ugani stevilo: "))
    except ValueError:
        print "Vnesi celostvilsko vrednost"
        continue
    if guess == secret_num:
        print "Uganil si"
        break # break zaključi samo eno zanko
    elif guess > secret_num:
        print "Ugibaj nizje"
        break
    elif guess < secret_num:
        print "Ugibaj visje"
        break
    else:
        pass # ukaz ki pomeni "pejt naprej"
