class studinfo:
    # private
    __stid = 12
    __stnm = "Sanket"

    def __printdata(self):  # private method
        print("This is printdata!")
        print("ID:", self.__stid)
        print("Name:", self.__stnm)

    def myfunc(self):  # public
        self.__printdata()  # private


st = studinfo()
# print("ID:", st.stid)
# print("Name:", st.stnm)

# st.printdata()
# st.__printdata()
st.myfunc()
