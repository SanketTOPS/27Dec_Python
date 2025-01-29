"""def getsum(a, b):
    return a, b


x = getsum(23, 54)
print(x)
print("First Value:", x[0])
print("Second Value:", x[1])"""


def getdata(id, name):
    return id, name


def userdata():
    x = getdata(101, "Sanket")
    print("ID:", x[0])
    print("Name:", x[1])


userdata()
