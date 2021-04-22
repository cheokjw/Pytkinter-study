from tkinter import *
from PIL import ImageTk, Image
import math

#initializing Tk class OOP(Object-Oriented Programming)
root = Tk()
root.title("Simple Calculator")
#Shows the icon at the top left corner of the GUI
#.iconbitmap() only supports .ico type of images. Other type will not work
root.iconbitmap("C:/Users/cheok/OneDrive/Desktop/py projects/tkinter/images/calculator-2465656-2042102.ico")
root.configure(bg = "black")


#Entry(root) = shows an input field which allows users to enter data
entryWid = Entry(root, font = ("AngsanaUPC"), borderwidth = 1)
#columnspan allows 3 buttons to be under the input field
entryWid.grid(row = 0, column = 0, columnspan = 5, padx = 0, pady = 10, ipadx = 60, ipady = 30)


"""
My own try by using the index/ array (but only available for one math operator)


def button_click(number):
    entryWid.insert("end", number)
    current_num = entryWid.get()
    first_num = current_num[0: current_num.index("+")]
    second_num = current_num[current_num.index("+") + 1 : -1]
    print(first_num) 
    print(second_num)
    if number == "=":
        Total = int(first_num) + int(second_num)
        entryWid.insert("end", Total)
"""

"""
My own method where it uses the .Boolean to tell the calculator which button had been pressed


def button_click(number):
    entryWid.insert(END , number)
    current_num = entryWid.get()

def Addition():
    first_number = entryWid.get()
    global fnum
    fnum = int(first_number)
    Addition.Boolean = True
    Subtract.Boolean = False
    Divide.Boolean = False
    Multiply.Boolean = False
    entryWid.delete(0, END)

def Subtract():
    first_number = entryWid.get()
    global fnum
    fnum = int(first_number)
    Addition.Boolean = False
    Subtract.Boolean = True
    Divide.Boolean = False
    Multiply.Boolean = False
    entryWid.delete(0, END)

def Divide():
    first_number = entryWid.get()
    global fnum
    fnum = int(first_number)
    Addition.Boolean = False
    Subtract.Boolean = False
    Divide.Boolean = True
    Multiply.Boolean = False
    entryWid.delete(0, END)

def Multiply():
    first_number = entryWid.get()
    global fnum
    fnum = int(first_number)
    Addition.Boolean = False
    Subtract.Boolean = False
    Divide.Boolean = False
    Multiply.Boolean = True
    entryWid.delete(0, END)

def Equal():
    second_number = int(entryWid.get())
    entryWid.delete(0, END)
    if Addition.Boolean == True:
        Total = fnum + second_number
    
    elif Subtract.Boolean == True:
        Total = fnum - second_number
    
    elif Divide.Boolean == True:
        Total = fnum / second_number
    
    elif Multiply.Boolean == True:
        Total = fnum * second_number
    
    entryWid.insert(0, Total)

#Clearing the Input field
def Clear():
    entryWid.delete(0, END)
"""

# video's guide
def button_click(number):
    entryWid.insert(END , number)

def Addition():
    global fnum
    global math
    first_number = entryWid.get()
    math = "Addition"
    fnum = float(first_number)
    entryWid.delete(0, END)

def Subtract():
    global fnum
    global math
    first_number = entryWid.get()
    math = "Subtraction"
    fnum = float(first_number)
    entryWid.delete(0, END)

def Divide():
    global fnum
    global math
    first_number = entryWid.get()
    math = "Divide"
    fnum = float(first_number)
    entryWid.delete(0, END)

def Multiply():
    global fnum
    global math
    first_number = entryWid.get()
    math = "Multiply"
    fnum = float(first_number)
    entryWid.delete(0, END)

def Equal():
    second_number = float(entryWid.get())
    entryWid.delete(0, END)    
    if math == "Addition":
        Answer = fnum + second_number

    elif math == "Subtraction":
        Answer = fnum - second_number

    elif math == "Divide":
        Answer = fnum / second_number

    elif math == "Multiply":
        Answer = fnum * second_number 

    entryWid.insert(0, Answer)

#Clearing the Input field
def Clear():
    entryWid.delete(0, END)


Image_1 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Desktop/py projects/tkinter/images/no 1.png").resize((80, 50), Image.ANTIALIAS))


#Define buttons from 1 - 0
Button1 = Button(root, text = "1", padx = 35, pady = 20, command = lambda: button_click(1), borderwidth = 1, bg = "white")
Button2 = Button(root, text = "2", padx = 35, pady = 20, command = lambda: button_click(2), borderwidth = 1, bg = "white")
Button3 = Button(root, text = "3", padx = 35, pady = 20, command = lambda: button_click(3), borderwidth = 1, bg = "white")
Button4 = Button(root, text = "4", padx = 35, pady = 20, command = lambda: button_click(4), borderwidth = 1, bg = "white")
Button5 = Button(root, text = "5", padx = 35, pady = 20, command = lambda: button_click(5), borderwidth = 1, bg = "white")
Button6 = Button(root, text = "6", padx = 35, pady = 20, command = lambda: button_click(6), borderwidth = 1, bg = "white")
Button7 = Button(root, text = "7", padx = 35, pady = 20, command = lambda: button_click(7), borderwidth = 1, bg = "white")
Button8 = Button(root, text = "8", padx = 35, pady = 20, command = lambda: button_click(8), borderwidth = 1, bg = "white")
Button9 = Button(root, text = "9", padx = 35, pady = 20, command = lambda: button_click(9), borderwidth = 1, bg = "white")
Button0 = Button(root, text = "0", padx = 35, pady = 20, command = lambda: button_click(0), borderwidth = 1, bg = "white")
DecimalButton = Button(root, text = ".", padx = 37, pady = 20, command = lambda: button_click("."), borderwidth = 1, bg = "white")

#Defining special char buttons
ClearButton = Button(root, text = "AC", padx = 20, pady = 20, command = Clear, borderwidth = 1, bg = "white")
AddtionButton = Button(root, text = "+", padx = 24, pady = 50, command = Addition, borderwidth = 1, bg = "white")
SubtractButton = Button(root, text = "-", padx = 26, pady = 20, command = Subtract, borderwidth = 1, bg = "white")
MultiplyButton = Button(root, text = "x", padx = 25, pady = 20, command = Multiply, borderwidth = 1, bg = "white")
DivideButton = Button(root, text = "/", padx = 25, pady = 20, command = Divide, borderwidth = 1, bg = "white") 
EqualButton = Button(root, text = "=", padx = 65, pady = 20, command = Equal, borderwidth = 1, bg = "white")

#Placing buttons onto the screen
Button1.grid(row = 1, column = 0)
Button2.grid(row = 1, column = 1)
Button3.grid(row = 1, column = 2)
SubtractButton.grid(row = 1, column = 3)
ClearButton.grid(row = 1, column = 4)

#column span allows the button to be within the specified columns
#row span allows the button to be within the specified rows
Button4.grid(row = 2, column = 0)
Button5.grid(row = 2, column = 1)
Button6.grid(row = 2, column = 2)
AddtionButton.grid(row = 2, column = 3, rowspan = 2)
MultiplyButton.grid(row = 2, column = 4)

Button7.grid(row = 3, column = 0)
Button8.grid(row = 3, column = 1)
Button9.grid(row = 3, column = 2)
DivideButton.grid(row = 3, column = 4)

DecimalButton.grid(row = 4, column = 0)
Button0.grid(row = 4, column = 1)
EqualButton.grid(row = 4, column = 2, columnspan = 2)





#Tkinter loop func
root.mainloop()