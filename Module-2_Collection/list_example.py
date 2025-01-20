tech = ["python", "java", "php", "kotlin", "dart", "python"]
"""print(tech)
print(tech[0])
print(tech[-1])
print(tech[0:3])
print(tech[2:])
print(tech[:3])"""

# ----------------------------- #
# print(len(tech))

"""if "php" in tech:
    print("Yes...")
else:
    print("Noo")"""

# ----------------------------- #
# print(tech)

"""for i in tech:
    print(i)"""

# ------------------------------ #
# print(tech)

# List's Methods
# tech.append("C++")
# tech.insert(0, "C")
# tech[4] = "Android" #Update a value
# tech.pop()  # Remove a last value only
# tech.pop(1)
# tech.clear()
# del tech[2]
# del tech
# tech.remove("kotlin")
# tech.sort()
# tech.reverse()
# print(tech.index("php"))

# newtech = tech.copy()
# print(newtech)
# print(tech)


# --------------------------------- #
print(tech)

newtech = ["c", "c++", "html", "css"]
print(newtech)

# print(tech + newtech)
tech.extend(newtech)
print(tech)
