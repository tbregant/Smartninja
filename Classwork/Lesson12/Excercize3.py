# input: "TO je en string"
# output: "to JE EN STRING"


input_str = raw_input("Input: ")

output = ""

for index in range (0, len(input_str)):
    if input_str[index].upper() == input_str[index]:
        output += input_str[index].lower()
    else:
        output += input_str[index].upper()

print output