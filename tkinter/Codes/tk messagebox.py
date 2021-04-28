from tkinter import *
import tkinter.messagebox as messagebox


root = Tk()
root.title("Message box")


#types of message boxes = .showinfo(), .showwarning(), .showerror(), .askquestion(), .askokcancel, .askyesno()
def info():
    messagebox.showinfo("This is my pop up","Hello World!")

def warning():
    messagebox.showwarning("This is a warning","Warning")

def error():
    messagebox.showerror("This is an error","Error")

#.askquestion() returns a actual string instead of 1 and 0 like the others
#So we need to use "yes" or "no" in the condition statement
def question():
    response = messagebox.askquestion("This is a question", "Do you agree?")
    Label(root, text = response).pack()
    """
    or
    if response == "yes":
        Label(root, text = "You agreed").pack()
    else:
        Label(root, text = "You disagreed").pack()
    """

#The GUI returns 1 if you agreed or pressed ok and returns 0 when you disagree or press cancel. It all works the same except .askquestion()
def okcancel():
    response = messagebox.askokcancel("This is to confirm", "Is it ok?")
    if response == 1:
        Label(root, text = "you said ok!").pack()
    else:
        Label(root, text = "you said cancel!").pack()

def yesno():
    response = messagebox.askyesno("This is to ask yes or no", "yes or no")
    if response == 1:
        Label(root, text = "you said yes!").pack()
    else:
        Label(root, text = "you said no!").pack()


Button(root, text = "show info", command = info).pack()
Button(root, text = "show warning", command = warning).pack()
Button(root, text = "show error", command = error).pack()
Button(root, text = "ask question", command = question).pack()
Button(root, text = "ask ok cancel", command = okcancel).pack()
Button(root, text = "ask yes no", command = yesno).pack()

root.mainloop()