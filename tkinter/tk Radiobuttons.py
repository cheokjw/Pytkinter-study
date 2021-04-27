from tkinter import *

#Radio Buttons, similar to microsoft access's look up buttons
#We can create it in two ways, ones by creating each button manually, and the other ones by using a for in loop.
root = Tk()
root.title("Lookup Buttons")



"""
#Method 1(Creating each buttons manually)

#In tkinter, we have to declare the type of variables we want. For example, IntVar() for numbers, and StringVar() for strings
r = IntVar()
#This line sets the default value to 2
r.set("2")

#Shows the value inside the variable when the button is clicked.
def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()


#Radiobutton() creates a list like button for us to click.
#r.get() allows us to obtain the value from the variable.
Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()


myLabel = Label(root, text = r.get())
myLabel.pack()

myButton = Button(root, text = "Click Me!", command = lambda: clicked(r.get()))
myButton.pack()
"""



#Method 2(Creating Radiobuttons using for in loop)
#This method is faster because we don't have to type in each button manually
#Create a list containing sets containing (text and value)
Toppings = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Tomato","Tomato"),
    ("Mushrooms","Mushrooms")
]

pizza = StringVar()
pizza.set("Cheese")

#This loops each element inside the list and set and return the value into the RadioButton
for text, toppings in Toppings:
    Radiobutton(root, text = text, variable = pizza, value = toppings, command = lambda: clicked(pizza.get())).pack(anchor = W)


#Others are the same as method 1
def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()

myLabel = Label(root, text = pizza.get())
myLabel.pack()


root.mainloop()
