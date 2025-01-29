def getdata(id, name, sub):
    print("ID:", id)
    print("Name:", name)
    print("Subject:", sub)


# getdata(101, "Sanket", "Python")

n = int(input("Enter number of students:"))
for i in range(n):
    id = input("Enter an ID:")
    name = input("Enter a Name:")
    sub = input("Enter a Subject:")
    getdata(id, name, sub)  # function calling
