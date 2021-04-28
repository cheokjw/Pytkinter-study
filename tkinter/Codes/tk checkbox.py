from tkinter import *

root = Tk()
root.title("Checkboxes")
root.geometry("400x400")

#Same type of variable as Radiobuttons. We have to declare the variable type in tkinter.
var = StringVar()
var.set("Pizza")

def checkvar():
    Label(root, text = var.get()).pack()


#onvalue is the value when the checkbox is checked while offvalue is the value when the checkbox is not checked
checkbox = Checkbutton(root, text = "This is a checkbox", variable = var, onvalue = "Burger", offvalue = "Pizza", command = checkvar)
#checkbox.deselect() = Cause the button to deselect by default
checkbox.pack()

my_lbl = Label(root, text = var.get()).pack()

#Shows the value of the checkbox when the button is pressed
my_btn = Button(root, text = "Show var value", command = checkvar).pack()


root.mainloop()