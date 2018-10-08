# python list

a = [1, 2, 3, 4, "ree", 123.3, [2, 3, 4], "gugu"]

# accessing the list
print a[0]
print a[4]
print a[6]

# accessing the nested list
print a[6]

# acccessing element of nested list
print a[6][1]

# use of reverse indexing
print a[-1]

# from x
print a[2:]

# from - to
print a[2:4]

# from beginning to.. x
print a[:4]

# adding elements
a.append("TEST")
print a[-1]

# removing from list
# obtaining and removing LAST ELEMENT
b = a.pop()
print b
print a

# remove by value, only fist occurrence
a.remove(1)
print a

# remove by index
a.pop(1)
print a





