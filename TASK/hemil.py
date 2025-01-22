# WAP to create dynamic list from user.
data = []

n = int(input("Enter th number of elements:"))
for i in range(n):
    city = input("Enter city name:")
    data.append(city)
print(data)
