# global var.
a = 43
b = 76


def production():
    # Local var.
    a = 43
    b = 76
    print("Mul:", a * b)


print("Sum:", a + b)


production()
