from tkinter import *

#initializing Tk class OOP(Object-Oriented Programming)
root = Tk()

#Creating a Label Widget
MyLabel = Label(root, text = "Hello World")

#Pack = Straight up shows the content as big as it is onto the screen
MyLabel.pack()

#Tkinter loop func
root.mainloop()