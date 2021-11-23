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

#widgets
#Display
txtDisplay = Entry(calc, font = ('arial', 20, 'bold'), bg = "grey", bd=30, width=30, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#Buttons
numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd =4, text = numberpad[i]))
        btn[i].grid(row = j, column =k, pady = 1)

        i += 1
               


#===========Menu Area==============

def fncExit():
    fncExit = tkinter.messagebox.askyesno("Scientific Calculator","Confirm Exit")
    if fncExit > 0:
        root.destroy()
        return
#def fncStandard():
#    root.resizable(width = False, height=False)
#    root.geometry("500x560+0+0")
    
def fncScientific():
    root.resizable(width = False, height=False)
    root.geometry("900x560+0+0")
    
menubar = Menu(calc)

fileMenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Standard", command = fncStandard)
fileMenu.add_command(label = "Scientific", command = fncScientific)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command=fncExit)

editMenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Cut")
editMenu.add_command(label = "Copy")
editMenu.add_separator()
editMenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "Help Dialog")

root.configure(menu=menubar)
root.mainloop()



