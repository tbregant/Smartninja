secret = 44

guess = 0

while guess != secret:
    guess = int(raw_input("Vnesi stevilo: "))
    if guess == secret:
        print "bravo, " + str(secret) + " je skrito stevilo"
    else:
        print "Stevilo " + str(guess) + " zal ni skrito stevilo"

