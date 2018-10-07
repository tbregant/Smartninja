print "Pozdravljen. To je program za pretvorbo milje v kilometre"

while True:
    milje = float(raw_input("Prosim vnesi dolzino v miljah: "))

    faktor_pretvorbe = 0.621371192

    print milje * faktor_pretvorbe

    nadaljevanje = raw_input("Ali zelis nadaljevati z novo pretvorbo? Da/Ne: ")

    if nadaljevanje.lower() != "da":
        print "Hvala in lep dan se naprej!"
        exit()