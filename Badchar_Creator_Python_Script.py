from __future__ import print_function
listRem = "\\x23\\x3c\\x83".split("\\x")
for x in range(1, 256):
    if "{:02x}".format(x) not in listRem:
        print("\\x" + "{:02x}".format(x), end='')
print()

#qouted hex are bad char like \x00 in this program change this as your requirement, If you leave it empty and run it this will print all the possible hex.
