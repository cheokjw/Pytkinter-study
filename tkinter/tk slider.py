from tkinter import *


root = Tk()
root.title("Sliders")
#Defines the size of the GUI, use "widthxheight" instead of "width*height"
root.geometry("400x400")


#This function changes the GUI size as the slide changes
#This function would not work if we didn't put the var into the function
def gui_size(var):
    root.geometry(f"{horizontal.get()}x{vertical.get()}")
    

#Be careful about the (from_ = ), (from = ) would not work
#And you can't code the packing in one line because
vertical = Scale(root, from_ = 200, to = 500, command = gui_size)
vertical.pack()


#orient = HORIZONTAL makes the slider horizontal
horizontal = Scale(root, from_ = 200, to = 500, orient = HORIZONTAL, command = gui_size)
horizontal.pack()


"""
This function only changes the GUI size when the button is clicked

def gui_size():
    height = vertical.get()
    width = horizontal.get()
    root.geometry(f"{width}x{height}")

my_btn = Button(root, text = "Press me to resize the GUI", command = gui_size).pack()
"""


root.mainloop()