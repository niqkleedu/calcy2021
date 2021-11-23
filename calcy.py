from tkinter import*
import math
import parser
import tkinter.messagebox

root = calcy()
root.title("Scientific Calculator")
root.configure(background = "white")
root.resizable(width = False, height=False)
root.geometry("500x560+0+0)

calc = Frame(root)
calc.grid()

menubar = Menu(calc)
filemenu = Menu
