from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Base")

#This function is for opening a new window showing the simpson image when the button from the main window is pressed
def open():

    #We have to global my_img because python would not show the image when its a local variable
    global my_img

    #Link for difference between root and toplevel
    #https://stackoverflow.com/questions/29655219/whats-the-difference-between-tkinters-tk-and-toplevel-classes#:~:text=One%20of%20tkinter%27s%20core%20architectural,initializes%20the%20entire%20tkinter%20framework.
    #The toplevel widget is used when a python application needs to represent some extra information, pop-up, or the group of widgets on the new window.
    top = Toplevel()
    top.title("My Second Window")
    my_img = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/simpson.jfif"))
    my_label = Label(top, image = my_img).pack()

    #top.destroy only closes the second window whereas top.quit closes the whole program
    Quit_button = Button(top, text = "Close window", command = top.destroy).pack()


button = Button(root, text = "Press to open the second window", command = open)
button.pack()



mainloop()