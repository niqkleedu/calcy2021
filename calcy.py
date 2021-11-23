from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background = "white")
root.resizable(width = False, height=False)
root.geometry("500x560+0+0")

calc = Frame(root)
calc.grid()

menubar = Menu(calc)
filemenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Standard")
filemenu.add_command(label = "Scientific")
filemenu.add_separator()
filemenu.add_command(label = "Exit")

root.configure(menu=menubar)
root.mainloop()

