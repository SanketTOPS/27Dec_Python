file = open("stdata.txt", "w")

id = input("Enter an ID:")
name = input("Enter a Name:")
sub = input("Enter a Subject:")

"""file.write(id)
file.write(name)
file.write(sub)"""

file.write(f"ID:{id}\nName:{name}\nSub:{sub}")
