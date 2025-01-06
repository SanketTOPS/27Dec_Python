n1=int(input("Enter Number1:"))
n2=int(input("Enter Number2:"))

if n1 and n2 !=0: #root
    if n1>n2:
        print("Sub:",n1-n2)
    else:
        print("Mul:",n1*n2)
else:
    print("Error!Bcz of number is ZERO")
