class studinfo:
    stid = 12
    stnm = "Sanket"

    def myfunc(x):
        print("This is member function!")

    def getsum(self, x, y):
        print("Sum:", x + y)


# Object of class
st = studinfo()
print("ID:", st.stid)
print("Name:", st.stnm)
st.myfunc()
st.getsum(56, 89)
