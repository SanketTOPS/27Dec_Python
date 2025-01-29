def getdata(id, name, sub):
    print("ID:", id)
    print("Name:", name)
    print("Subject:", sub)


# getdata(101, "Ashok", "JAVA") #positional arguments
# getdata("Python", 101, "Sanket")


# getdata(id=101, name="Sanket", sub="PHP")  # keyword arguments

getdata(name="Sanket", id=101, sub="PHP")  # keyword arguments
