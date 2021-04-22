from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("image slides")


my_img1 = ImageTk.PhotoImage(Image.open())
my_img2 = ImageTk.PhotoImage(Image.open())
my_img3 = ImageTk.PhotoImage(Image.open())
my_img4 = ImageTk.PhotoImage(Image.open())
my_img5 = ImageTk.PhotoImage(Image.open())


img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)


def forward(img_index):
    global my_label
    global button_forward
    global button_back

    #.grid.forget() deletes the current label/ showing image
    my_label.grid.forget()
    my_label = Label(image = img_list[img_index - 1])
    button_forward = Button(root, text = ">>>", command = lambda: forward(img_index + 1))
    button_backward = Button(root, text = "<<<", command = lambda: backward)
    my_label.grid(row = 0, column = 0, columnspan = 3)


def backward():
    return None


button_back = Button(root, text = "<<<", command = backward)
#root.quit button command is for exiting the GUI program after pressing the button
button_exit = Button(root, text = "Exit", command = root.quit)
button_forward = Button(root, text = ">>>", command = lambda: forward(2))


button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)



root.mainloop()