

tasks = {}

while True:
    task = raw_input("Pleas inpute task [q - to quit]: ")
    if task.lower() == "q":
        break

    while True:
        done = raw_input("Is task done [y/n]: ")

        if done.lower() == "y":
            tasks[task] = True
            break
        elif done.lower() == "n":
            tasks[task] = False
            break
        else:
            print "'y' or 'n'"

for t in tasks:
    print "{0}: {1}".format(t, tasks[t])