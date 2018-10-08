

tasks = []
tasks_done = []

while True:
    task = raw_input("Pleas inpute task [q - to quit]: ")
    if task.lower() == "q":
        break
    tasks.append(task)

    while True:
        done = raw_input("Is task done [y/n]: ")

        if done.lower() == "y":
            tasks_done.append(True)
            break
        elif done.lower() == "n":
            tasks_done.append(False)
            break
        else:
            print "'y' or 'n'"


for n, task in enumerate(tasks):
    # print n, task, tasks_done[n]
    # with format string
    print "{}: {}".format(task, tasks_done[n])


for t, td in zip(tasks, tasks_done):
    print t, td