import re

x = "This is Python!"

result = re.findall("is", x)
print(result)

if result:
    print("Match Done...")
else:
    print("Error!")
