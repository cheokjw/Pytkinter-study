from tkinter import *

root = Tk()
root.title("Dropdown box")
root.geometry("400x400")


# Button functions 
def show(var):
    my_lbl = Label(root, text = clicked.get())
    my_lbl.pack()

def show_day():
    my_lbl = Label(root, text = clicked.get())
    my_lbl.pack()



# We can create dropdown options by typing it manually or using a list
options = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thurday",
    "Friday",
    "Saturday",
]


clicked = StringVar()
# This is used when the options are typed in manually
# clicked.set("Monday")
# The index method is used when the options are created in a list
clicked.set(options[0])


"""
Method 1 = Typing all the options manually
drop = OptionMenu(root, clicked,"Sunday", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday", command = show)
drop.pack()
"""

# Method 2 = Using a list, remember to put * before options
drop = OptionMenu(root, clicked, *options, command = show)
drop.pack()


my_btn = Button(root, text = "Show day", command = show_day).pack()

root.mainloop()