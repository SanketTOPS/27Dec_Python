import re

mystr = "That is Python!8966"

# x = re.findall("^This", mystr)
# x = re.findall("^[A-Z]", mystr)
x = re.findall("65$", mystr)
print(x)
