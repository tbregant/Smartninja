# working with files

# below equal to: write_file = open("ime_datoteke.txt", "w") ... but more safer way below

with open("file_name.txt", "a") as write_file: # "ab" append binary
    write_file.write("Vrstica 2\n")
# end of context, file closed.


with open("file_name.txt", "r") as read_file:
    vsebina = read_file.read()
print vsebina


# split to rows
vsebina = vsebina.split("\n")

for line in vsebina:
   line = line.split(" ")
   if len(line) == 2:
        print line[1]


