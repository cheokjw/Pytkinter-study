from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.geometry("400x600")

# Databases

# Create a database or connect to one
Connect = sqlite3.connect("address_book.db")

# Create cursor
# Cursor does all the command execution
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
'''
Commented this line out because we wouldn't want to create a new table everytime we run this program

Cursor.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text, 
        city text, 
        state text,
        zipcode text
)""")
'''



# Submit info into the database when the button is pressed.
def submit():
        
        # Create a database or connect to one
        Connect = sqlite3.connect("address_book.db")

        # Create cursor
        # Cursor does all the command execution
        Cursor = Connect.cursor()


        # Insert info into Table
        # We can put any variable for VALUES(:var) since it only refers to the field of the table, but its better to name it as the field name so that it is easier to refer back
        Connect.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                {
                        "f_name": f_name.get(),
                        "l_name": l_name.get(),
                        "address": address.get(),
                        "city": city.get(),
                        "state": state.get(),
                        "zipcode": zipcode.get()
                        })

        # Commit changes
        Connect.commit()

        # Close connection
        Connect.close()

        # Then, we clear the text box
        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)


def Query():

        # Connect to database
        Connect = sqlite3.connect("address_book.db")

        # Create cursor to execute things in database
        Cursor = Connect.cursor()

        # Query the database
        # oid = The automated number primary key created by sqlite3, but it ignores it unless we specify it in our query
        Cursor.execute("""
                SELECT oid, *
                FROM addresses
        """)

        # Fetch all record. You can also do .fetchone() which only fetch one record, or .fetchmany(number), fetch a specified numbers of record.
        records = Cursor.fetchall()
        print(records)
        print_records = ""

        # Loop through result and make them into a list, then label it and present on GUI
        for record in records:
                # Since the record is a tuple now, we can access its item by doing record[0] <-- This returns the oid of the record
                print_records += f"{record[1]}\t {record[0]}\n"

        if print_records == "[]":
                query_lbl = Label(root, text = "No records")
                query_lbl.grid(row = 10, column = 0, columnspan = 2)
        
        else:
                query_lbl = Label(root, text = print_records)
                query_lbl.grid(row = 10, column = 0, columnspan = 2)

        # Commit execution
        Connect.commit()

        # Close connection
        Connect.close()

# Create a function to delete a record
def delete():

        # Connect to the datbase
        Connect = sqlite3.connect("address_book.db")

        # Create cursor
        Cursor = Connect.cursor()

        Cursor.execute(f"""
                DELETE FROM [addresses]
                WHERE [oid] = {Oid_del.get()}
        
        """)

        # Commit changes
        Connect.commit()

        # Close connections
        Connect.close()

        Oid_del.delete(0, END)



# Create text boxes
f_name = Entry(root, width = 30)
l_name = Entry(root, width = 30)
address = Entry(root, width = 30)
city = Entry(root, width = 30)
state = Entry(root, width = 30)
zipcode = Entry(root, width = 30)

# Placing text boxes
f_name.grid(row = 0, column = 1, padx = 20, pady = 20, ipadx = 30)
l_name.grid(row = 1, column = 1, padx = 20, ipadx = 30)
address.grid(row = 2, column = 1, padx = 20, pady = 20, ipadx = 30)
city.grid(row = 3, column = 1, padx = 20, ipadx = 30)
state.grid(row = 4, column = 1, padx = 20, pady = 20, ipadx = 30)
zipcode.grid(row = 5, column = 1, padx = 20, ipadx = 30)



# Create Text box labels
f_name_lbl = Label(root, text = "First Name : ")
l_name_lbl = Label(root, text = "Last Name : ")
address_lbl = Label(root, text = "Address : ")
city_lbl = Label(root, text = "City : ")
state_lbl = Label(root, text = "State : ")
zipcode_lbl = Label(root, text = "Zipcode : ")

# Placing text box labels
f_name_lbl.grid(row = 0 , column = 0, padx = 10, sticky = "E")
l_name_lbl.grid(row = 1, column = 0, padx = 10, sticky = "E")
address_lbl.grid(row = 2, column = 0, padx = 10, sticky = "E")
city_lbl.grid(row = 3, column = 0, padx = 10, sticky = "E")
state_lbl.grid(row = 4, column = 0, padx = 10, sticky = "E")
zipcode_lbl.grid(row = 5, column = 0, padx = 10, sticky = "E")



# Create submit buttons
Submit_btn = Button(root, text = "Submit", command = submit)
Submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, ipadx = 145)

# Create Query button
Query_button = Button(root, text = "Show records", command = Query)
Query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, ipadx = 130)

# Create delete button
Delete_button = Button(root, text = "Delete", command = delete)
Delete_button.grid(row = 9, column = 0, columnspan = 2, pady = 10, ipadx = 145)

# Create and place Entry widget and label
del_lbl = Label(root, text = "Record Delete : ")
Oid_del = Entry(root, width = 30)
del_lbl.grid(row = 8, column = 0, padx = 10, sticky = "E")
Oid_del.grid(row = 8, column = 1, padx = 20, pady = 20, ipadx = 30)



# Commit changes
Connect.commit()

# Close connection
Connect.close()




root.mainloop()