from tkinter import *


root = Tk()
root.title("tkinter Frames")

#Declaring a Frame element
#The padx and pady in the frame controls the size of the frame.
frame = LabelFrame(root, text = "This is a frame", padx = 5, pady = 5)

#The padx and pady in the .pack() is for controlling the size outside the frame
frame.pack(padx = 10, pady = 10)

"""
You can understand better by trying this code:
frame = LabelFrame(root, text = "This is a frame", padx = 50, pady = 50)
frame.pack(padx = 10, pady = 10)

AND

frame = LabelFrame(root, text = "This is a frame", padx = 5, pady = 5)
frame.pack(padx = 100, pady = 100)
"""


#Declaring the button inside the frame instead of root(The main GUI)
b = Button(frame, text = "Do not click this button!")
b2 = Button(frame, text = "or here")

#Normally, we can't use .pack() and .grid() together inside the root. But, it is possible now because of the frame element
#This is because we are packing the frame and arranging the buttons inside the frame
b.grid(row = 0, column = 0)
b2.grid(row = 1, column = 1)

mainloop()