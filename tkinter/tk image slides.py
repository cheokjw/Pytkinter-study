from tkinter import *
from PIL import ImageTk, Image

#Initializing the GUI program
root = Tk()
root.title("image slides")

#Defining all the images by using the PIL lib
my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/PoliticalIdleItalianbrownbear-size_restricted.gif"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/tenor.gif"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/simpson.jfif"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/download (1).jfif"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/j.jfif"))


#Listing all the images into an img_list
img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

#Showing the first/ default image onto the GUI program
my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)


#Button function section
def forward(img_index):
    #The my_label, button_forward and button_backward is globalized because it has to be updated once every click
    #This is to update the image index because the we have used the list method for the image slides
    global my_label
    global button_forward
    global button_backward

    #.grid.forget() deletes the current label/ showing image
    my_label.grid_forget()
    my_label = Label(image = img_list[img_index])

    #Plus 1 into the img_index to show the next image if the forward button is pressed. For example, if the default img_index is 0, it'll add 1 into img_index so it becomes 1
    #Thus, it'll show the image which has the img_index of 1, which is, the second image.
    button_forward = Button(root, text = ">>>", command = lambda: forward(img_index + 1))
    button_backward = Button(root, text = "<<<", command = lambda: backward(img_index - 1))

    #Since theres only 5 images in the img_list, img_index 4 will be the last image in the img_list
    #Thats why, we'll disable the forward button when we've reached the last image.
    if img_index == 4:
        button_forward = Button(root, text = ">>>", state = DISABLED)

    #Then, we'll have to show the update of the button because the img_index wouldn't be changed if we didn't update it
    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_backward.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

#Basically the same concept as the forward func but its reversed
def backward(img_index):
    global my_label
    global button_forward
    global button_backward
    
    my_label.grid_forget()
    my_label = Label(image = img_list[img_index])
    button_forward = Button(root, text = ">>>", command = lambda: forward(img_index + 1))
    button_backward = Button(root, text = "<<<", command = lambda: backward(img_index - 1))
    my_label.grid(row = 0, column = 0, columnspan = 3)

    if img_index == 0:
        button_backward = Button(root, text = "<<<", state = DISABLED)

    button_backward.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)



#root.quit button command is for exiting the GUI program after pressing the button
button_back = Button(root, text = "<<<", command = backward, state = DISABLED)
button_exit = Button(root, text = "Exit", command = root.quit)
button_forward = Button(root, text = ">>>", command = lambda: forward(1))



button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)




root.mainloop()