print "Hi, welcome to Menu creator. Lets begin ..."

menu = {}

end = ""
while end.upper() != "N":
    try:
        name = raw_input("Please enter item name: ")
        price = float(raw_input("Please enter price for " + name + ": "))
        menu[name] = price
        end = raw_input("Continue [Y/N]: ")
    except ValueError:
        print "Wrong value, try again ... "

with open("menu.txt", "w+") as menu_file:
    for item in menu:
        menu_file.write(item + " " + str(menu[item]) + "\r")

