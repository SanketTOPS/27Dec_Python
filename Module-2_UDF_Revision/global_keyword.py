x = 10

print("x:", x)


def getval():
    global x
    x += 1
    print("New X:", x)


getval()
