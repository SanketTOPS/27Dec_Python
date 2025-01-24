stdata = {}

n = int(input("Enter number of pairs:"))

for i in range(n):
    key = input("Enter your Key's:")
    val = input("Enter your Value's:")
    stdata[key] = val

print(stdata)
