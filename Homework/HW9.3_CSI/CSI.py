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

guilty = ""

# TODO: create new list do count charecteristics for each person.

for id, val in sdb.iteritems():
    for inner_id, inner_val in val.iteritems():
        if inner_val == sc[inner_id]:
            guilty = id
        else:
            break

print "The suspect has " + sc["Hair color"] + " hair color, " + sc["Face shape"] + " Face shape, " \
                         + sc["Eye color"] + " Eye color, " + sc["Gender"] + " Gender, " + sc["Race"] + " Race."
print "Suspect's name is: " + guilty










