import datetime

file = open("stdata.txt", "a")

id = input("Enter an ID:")
name = input("Enter a Name:")
sub = input("Enter a Subject:")

file.write(f"Created:{datetime.datetime.now()}\nID:{id}\nName:{name}\nSub:{sub}\n")
