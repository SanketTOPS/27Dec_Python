import keyword

x = keyword.kwlist
print(x)

"""for i in x:
    print(i)"""


key = input("Enter any string:")

if key in x:
    print("This is keyword...")
else:
    print("This is not keyword!")
