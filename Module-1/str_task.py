name = input("Enter a fullname:")
age = input("Enter an Age:")
mobile = input("Enter a Mobile:")
password = input("Enter Password:")
cpass = input("Enter Confirm Password:")

if (
    name.isalpha()
    and age.isdigit()
    and mobile.isdigit()
    and len(mobile) == 10
    and password.isalnum()
    and cpass.isalnum()
    and password == cpass
):
    print("Name:", name)
    print("Age:", age)
    print("Mobile:", mobile)
    print("Password:", password)
else:
    print("Error!")
