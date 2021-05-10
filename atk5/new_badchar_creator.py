from __future__ import print_function
listRem = "\\x00\\x16\\x2f\\xf4\\xfd".split("\\x")
for x in range(1, 256):
    if "{:02x}".format(x) not in listRem:
        print("\\x" + "{:02x}".format(x), end='')
print()
