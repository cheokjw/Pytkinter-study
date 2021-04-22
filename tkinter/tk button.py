from tkinter import *

#initializing Tk class OOP(Object-Oriented Programming)
root = Tk()

#a function that shows the text "Look! I clicked a Button"
def myClick():
    myLabel = Label(root, text = "Look! I clicked a Button !")
    myLabel.pack()

#Button(root, text) = having a button for user to click
#state = DISABLED = wont allow user to click the button, but it'll still show the button
#padx = num = controlling the x-axis(width size) of the button
#pady = num = controlling the y-axis(length size) of the button
#command = func = letting the button to do something
#fg = "colour" = changing the text colour
#bg = "colour" = changing the button background color
myButton = Button(root, text = "Click Me!", padx = 50, pady = 50, fg = "Blue", bg = "light green", command = myClick)
myButton.pack()

#Tkinter loop func
root.mainloop()