print "Hi, welcome to Menu creator. Lets begin ..."

end = ""
while end.upper() != "N":
    try:
        name = raw_input("Please enter item name: ")
        price = float(raw_input("Please enter price for " + name + ": "))

        with open("menu.txt", "a") as menu_file:
            menu_file.write(name + " " + str(price) + "\r")

        end = raw_input("Continue [Y/N]: ")

    except ValueError:
        print "Wrong value, try again ... "