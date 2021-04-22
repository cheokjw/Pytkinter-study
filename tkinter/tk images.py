from tkinter import *
#PIL stands for Python Image Library, its old, doesn't really work anymore
#The new version is Pillow(a fork of PIL which got improved)
from PIL import ImageTk, Image

root = Tk()


#Shows the icon at the top left corner of the GUI
#.iconbitmap() only supports .ico type of images. Other image type will not work
root.iconbitmap("C:/Users/cheok/OneDrive/Desktop/py projects/tkinter/images/calculator-2465656-2042102.ico")



#ImageTk.PhotoImage is used to present images inside the tkinter program
#BUT!!!! PhotoImage only supports GIF/ PGM/ PPM formats
#So, we'll need the help of Image.open() from PIL because it supports all types of image formats and do all the resizing
#Image.resize((width, height)Image.ANTIALIAS) ANTIALIAS is a high-quality downsampling filter

"""
You can code it in one line but you can also seperate it
1st method: 
my_img = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Desktop/py projects/tkinter/simpson.jfif").resize((100, 100),Image.ANTIALIAS))

2nd method:
image = Image.open("C:/Users/cheok/OneDrive/Desktop/py projects/tkinter/simpson.jfif").resize((100,100), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
"""
my_img = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Desktop/py projects/tkinter/simpson.jfif").resize((100, 100),Image.ANTIALIAS))
my_label = Label(image = my_img)
my_label.pack()







#root.quit() is a function which stops the program. Putting it into the button command will execute its function when the button is clicked
QuitButton = Button(root, text = "Exit Program", command = root.quit)
QuitButton.pack()

root.mainloop()