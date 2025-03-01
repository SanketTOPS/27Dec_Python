import re

x = "This is Python!"

result = re.search("Python", x)
# print(result)

if result:
    print("Match Done...")
else:
    print("Error!")
