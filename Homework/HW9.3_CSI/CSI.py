print "Welcome to CSI forensics. "
dna = raw_input("Please enter DNA sequence: ")

# DNA characteristics
dnac = { "Hair color":{"Black":"CCAGCAATCGC",
                    "Brown":"GCCAGTGCCG",
                    "Blonde":"TTAGCTATCGC"},

      "Face shape":{"Square":"GCCACGG",
                     "Round":"ACCACAA",
                     "Oval":"AGGCCTCA"},

      "Eye color":{"Blue":"TTGTGGTGGC",
                   "Green":"GGGAGGTGGC",
                   "Brown":"AAGTAGTGAC"},

      "Gender":{"Female":"TGAAGGACCTTC",
                "Male":"TGCAGGAACTTC"},

      "Race":{"White":"AAAACCTCA",
              "Black":"CGACTACAG",
              "Asian":"CGCGGGCCG"}}

# suspect charactetistics
sc = {}

for id, val in dnac.iteritems():
    dnac_type = id
    for inner_id, inner_val in val.iteritems():
        if dna.find(inner_val) != -1:
            dnac_value = inner_id
        else:
            continue
        sc[dnac_type] = dnac_value

# check if anything was found based on entered DNA
if sc.__len__() == 0:
    print "Unknown DNA"
    exit()

# suspects database
sdb = { "Eva":{"Gender":"Female",
               "Race":"White",
               "Hair color":"Blonde",
               "Eye color":"Blue",
               "Face shape":"Oval"},
        "Larisa":{"Gender":"Female",
                  "Race":"White",
                  "Hair color":"Brown",
                  "Eye color":"Brown",
                  "Face shape":"Oval"},
        "Matej":{"Gender":"Male",
                 "Race":"White",
                 "Hair color":"Black",
                 "Eye color":"Blue",
                 "Face shape":"Oval"},
        "Miha":{"Gender":"Male",
                "Race":"White",
                "Hair color":"Brown",
                "Eye color":"Green",
                "Face shape":"Square"}}

hits = {}

# populate hits dictionary with suspect database, set count at 0
for suspect in sdb:
    hits[suspect] = 0

guilty = ""

# count matching characteristics
for name, caracteristics in sdb.iteritems():
    for cname, cval in caracteristics.iteritems():
        if cval == sc[cname]:
            hits[name] += 1
            if hits[name] == 5:
                guilty = name
                print name

print "The suspect is {4} {3} with {0} hair, {2} eyes and {1} face".format(sc["Hair color"], sc["Face shape"], sc["Eye color"], sc["Gender"], sc["Race"])
print "The suspect's name is: " + guilty
