from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.geometry("400x400")

# Databases

# Create a database or connect to one
Connect = sqlite3.connect("address_book.db")

# Create cursor
Cursor = Connect.cursor()


# Create table
"""
Data types = 
1) Text = normal text/ strings
2) Integers = whole numbers
3) Real = decimal numbers
4) Null = Does it exist or does it not exist
5) Blob = Image files/ video files
"""
Cursor.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text, 
        city text, 
        state text,
        zipcode text
)""")





# Commit changes
Connect.commit()

# Close connection
Connect.close()



root.mainloop()