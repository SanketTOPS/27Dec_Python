n1=int(input("Enter Number1:"))
n2=int(input("Enter Number2:"))

print("1:Add")
print("2:Sub")
print("3:Mul")
print("4:Div")
choice=int(input("Select a valid choice from above:"))

if choice==1:
    print("Add:",n1+n2)
elif choice==2:
    print("Sub:",n1-n2)
elif choice==3:
    print("Mul:",n1*n2)
elif choice==4:
    print("Div:",n1/n2)
else: #FALSE
    print("Error!Invalid choice...")

