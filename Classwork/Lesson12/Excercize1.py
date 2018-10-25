numbers = []

for i in range(2000,3201):
    if i % 5 == 0:
        if i % 7 != 0:
            numbers.append(i)

izpis = str(numbers)

izpis = izpis.replace("[", "")
izpis = izpis.replace("]", "")

print izpis

print len(numbers)
