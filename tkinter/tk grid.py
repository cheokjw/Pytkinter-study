from tkinter import *

#initializing Tk class OOP(Object-Oriented Programming)
root = Tk()

#Creating a Label Widget
MyLabel1 = Label(root, text = "Hello World")
MyLabel2 = Label(root, text = "My Name is JW")

#grid enable us to put where we want our content to show up
#It stays in place even if we resize the window(it stays on the left side of the screen in this case)
#Instead of staying at the middle of the screen as .pack()
#.grid is relative to each other (explain this by changing mylabel2.grid column = numbers bigger than 1, it'll stay the same)
MyLabel1.grid(row = 0, column = 0)
MyLabel2.grid(row = 1, column = 0)

"""
OR you can code it like this:-
MyLabel1 = Label(root, text = "Hello World").grid(row = 0, column = 0)
MyLabel2 = Label(root, text = "My Name is JW").grid(row = 1, column = 0)
"""

#Tkinter loop func
root.mainloop()