from tkinter import *
from PIL import ImageTk, Image
import tkinter.filedialog as filedialog

root = Tk()
root.title("File dialog")


#Opens the file dialog when the button is clicked
def open():

    #Remember to global the declaration of image so that it'll show on the GUI application
    global my_img

    #* is a while card similar to the QBE or SQL in access, *.png means all files with the type of png and *.* means all the files
    #This whole line of code lets you pick a file from a menu and returns the file directory
    root.filename = filedialog.askopenfilename(initialdir = "/pytkinter-study/tkinter/images", title = "Select a file.", filetypes = (("jfif files","*.jfif"),("all files", "*.*")))

    #This label prooves that the filedialog.askopenfilename returns a file directory. Thus, we have to do extra things for it to show on the GUI
    my_lbl = Label(root, text = root.filename).pack()

    #We don't have to enter the image directory because the root.filename have already return the file directory
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_lbl = Label(image = my_img).pack()



my_btn = Button(root, text = "open file", command = open).pack()



root.mainloop()