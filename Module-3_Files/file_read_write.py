file = open("temp.txt", "r+")

name = input("Enter Name:")
city = input("Enter City:")

file.write(f"Name:{name}\nCity:{city}\n")
# file.close()


print(file.read())
