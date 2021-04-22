from tkinter import *

#initializing Tk class OOP(Object-Oriented Programming)
root = Tk()

#Entry(root) = shows an input field which allows users to enter data
#We can change its colour and size or features of the input field as the button eg: fg, bg, width, etc
#.insert(index value, text) = giving a default text/ value into the input field
entryWid = Entry(root, width = 50, borderwidth = 5)
entryWid.pack()
entryWid.insert(0, "Enter Your Name: ")

#We are able to put variables into the text section
#.get() allows us to get the input from the user entry widget
def myClick():
    myLabel = Label(root, text = f"Hello, {entryWid.get()}")
    myLabel.pack()

#Button(root, text) = having a button for user to click
#state = DISABLED = wont allow user to click the button, but it'll still show the button
#padx = num = controlling the x-axis(width size) of the button
#pady = num = controlling the y-axis(length size) of the button
#command = func = letting the button to do something
#fg = "colour" = changing the text colour
#bg = "colour" = changing the button background color
myButton = Button(root, text = "Enter you name", padx = 50, pady = 50, fg = "Blue", bg = "light green", command = myClick)
myButton.pack()

#Tkinter loop func
root.mainloop()