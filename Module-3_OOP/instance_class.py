class studinfo:
    stid = 101
    stnm = "Sanket"

    def printdata(self):
        print("ID:", self.stid)
        print("Name:", self.stnm)


# Calling via Object
"""st = studinfo()
st.printdata()
st.stid = 102
st.stnm = "Nirav"
st.printdata()"""


# Calling via Instance
studinfo().printdata()
studinfo().stid = 102
studinfo().stnm = "Nirav"
studinfo().printdata()
