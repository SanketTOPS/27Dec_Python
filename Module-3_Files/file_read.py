file = open("stdata.txt", "w")
# print(file.read())
# print(file.readline())
# print(file.readlines())
# print(file.readlines()[1])
# print(file.readlines()[0:3])

"""for i in file:
    print(i)"""

if file.readable():
    print("Yes...")
else:
    print("Noo")
