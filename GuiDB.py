from tkinter import *
import sqlite3


root = Tk()
root.title('GuiDB')
root.geometry("400x400")

# Databsses
# Create a databaseor connect to one
conn = sqlite3.connect('address_book.db')


# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
            firstName text,
            lastName text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")

#Commit Changess
conn.commit()

#Close Connection
conn.close()

root.mainloop()
