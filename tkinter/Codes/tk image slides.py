from tkinter import *
from PIL import ImageTk, Image

#Initializing the GUI program
root = Tk()
root.title("Image slides")

#Defining all the images by using the PIL lib
my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/PoliticalIdleItalianbrownbear-size_restricted.gif"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/tenor.gif"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/simpson.jfif"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/download (1).jfif"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/cheok/OneDrive/Documents/GitHub/pytkinter-study/tkinter/images/j.jfif"))


#Listing all the images into an img_list
img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


#Defining the status bar
#bd = border, (bd = 1 = enable border)
#anchor = moving the label to the position according to S(South), E(East), N(North), W(West)
#relief = the status/ look/ attribute of the border. It can be RAISED, SUNKEN, RIDGE, SOLID, GROOVE or FLAT
status = Label(root, text = f"Image 1 of {len(img_list)}", bd = 1, relief = SUNKEN, anchor = E)


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

    #Plus 1 into the img_index to show the next image if the forward button is pressed. For example, if the default img_index is 1, it'll add 1 into img_index so it becomes 2
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

    #Updating the status label according to the img_index
    status = Label(root, text = f"Image {img_index + 1} of {len(img_list)}", bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

#Basically the same concept as the forward func but its reversed
#img_index variable is called from the updated button_backward from forward func
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

    #Updating the status label according to the img_index
    status = Label(root, text = f"Image {img_index + 1} of {len(img_list)}", bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)


#root.quit button command is for exiting the GUI program after pressing the button
button_back = Button(root, text = "<<<", command = backward, state = DISABLED)
button_exit = Button(root, text = "Exit", command = root.quit)
button_forward = Button(root, text = ">>>", command = lambda: forward(1))



button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 10)
#sticky = S(South)/E(East)/N(North)/W(West) = To stretch the grid to any position
#sticky = W + E means stretching the grid from left to right / N + W means stretching from up to down
status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)



root.mainloop()