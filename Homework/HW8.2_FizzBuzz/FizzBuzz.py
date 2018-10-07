input = -1

# loop until user's input is correct
while input < 0:
    try:
        input = int(raw_input("Please enter a whole number greater than 0: "))
    except:
        print "Incorrect value! Try again."
        continue

for number in range(1, input+1):
    retval = ""

    if number % 3 == 0:
        retval = "fizz"

    if number % 5 == 0:
         retval += "buzz"

    if len(retval) == 0:
        retval = str(number)

    print retval
