import sqlite3

try:
    db = sqlite3.connect("newdb.db")
    print("Database created/connected!")
except Exception as e:
    print(e)


# Table Create
create_tbl = (
    "create table studinfo(id integer primary key autoincrement, name text, city text)"
)
try:
    db.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data

"""insert_data = "insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('ashok','surat'),('hitesh','bhavnagar')"

try:
    db.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
"""

# Update Data
"""update_data = "update studinfo set name='harsh', city='ahmedabad' where id=4"
try:
    db.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data = "delete from studinfo where name='nirav'"
try:
    db.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show Data
cr = db.cursor()
show_data = "select * from studinfo"
try:
    cr.execute(show_data)
    data = cr.fetchall()
    # data = cr.fetchmany(3)
    # data = cr.fetchone()
    # print(data)

    for i in data:
        print(i[1])
except Exception as e:
    print(e)
