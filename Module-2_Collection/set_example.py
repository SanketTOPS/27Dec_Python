myset = {"a", "b", "c", "d", "e", "a", "b"}

"""print(myset)

print(len(myset))"""

"""if "c" in myset:
    print("Yes...")
else:
    print("No..")"""


# ---------------------------- #
# print(myset)

"""for i in myset:
    print(i)
"""

# ---------------------------------- #

# print(myset)
# myset.add("f")
# myset.update(["g", "h", "i"])
# myset.pop()
# myset.remove("t")
# myset.discard("t")
# myset.clear()
# print(myset)

# -------------------------- #

newset = {"p", "q", "r", "s", "t", "a", "c"}
print(myset)
print(newset)


# x = myset.union(newset)
x = myset.intersection(newset)
print(x)
