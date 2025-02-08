import pandas

"""stdata = {
    "id": [1, 2, 3],
    "name": ["sanket", "nirav", "ashok"],
    "city": ["rajkot", "surat", "baroda"],
}"""

# result = pandas.DataFrame(stdata)
# print(result)


# --------------------------- #

data = pandas.read_excel("Book1.xlsx")
print(data)
