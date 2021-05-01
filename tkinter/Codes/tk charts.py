from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Tkinter charts")
root.geometry("400x200")

def graph():
    # This creates a normal distributed graph. Which works as X~N(mean, std., number of data points)
    house_prices = np.random.normal(200000, 25000, 5000)

    # matplotlib class which plots histogram graph automatically
    # 20 = number of datas
    plt.hist(house_prices, 20)
    plt.show()

my_btn = Button(root, text = "Show graph", command = graph)
my_btn.pack()



root.mainloop()