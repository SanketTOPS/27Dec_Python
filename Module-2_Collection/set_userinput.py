name = set()

n = int(input("Enter number of students:"))

for i in range(n):
    stnm = input("Enter your name:")
    name.add(stnm)

print(name)
