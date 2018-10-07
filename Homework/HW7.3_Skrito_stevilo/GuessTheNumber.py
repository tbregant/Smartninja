# encoding=utf-8
secret = 44

guess = int(raw_input("Vnesi poljubno število:"))

if guess == secret:
    print "Bravo, " + str(secret) + " je skrito število!"
else:
    print "Število " + str(guess) + " ni skrito število"
