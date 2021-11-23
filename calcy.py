from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background = "white")
root.resizable(width = False, height=False)
root.geometry("510x560+0+0")

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total =0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.operator = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstNumber = txtDisplay.get()
        secondNumber = str(num)
        if self.input_value:
            self.current = secondNumber
            self.input_value = False
        else:
            if secondNumber == '.':
                if secondNumber in firstNumber:
                    return
            self.current = firstNumber + secondNumber
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())


    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "+":
            self.total += self.current
        if self.op == "-":
            self.total -= self.current
        if self.op == "/":
            self.total /= self.current
        if self.op == "*":
            self.total *= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clearEntry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def clearEntryAll(self):
        self.clearEntry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)


    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def squareroot(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def plusminus(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)


added_value = Calc()

            

#widgets
#Display
txtDisplay = Entry(calc, font = ('arial', 20, 'bold'), bg = "grey", bd=30, width=30, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#Buttons Setup for numbers
numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "grey", text = numberpad[i]))
        btn[i].grid(row = j, column =k, pady = 1)
        btn[i]["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
        i += 1
               
#standard calculator button setup
bottonClear = Button(calc, text="C", width=6, height=2, font=('arial', 20, 'bold'), bd =4,
                     bg = "orange", command = added_value.clearEntry).grid(row=1 ,column=0, pady=1)

bottonClearAll = Button(calc, text="CE", width=6, height=2, font=('arial', 20, 'bold'), bd =4,
                     bg = "orange", command = added_value.clearEntryAll).grid(row=1 ,column=1, pady=1)

bottonSqRoot = Button(calc, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "orange",
                      command = added_value.squareroot).grid(row=1 ,column=2, pady=1)

bottonAdd = Button(calc, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "orange",
                   command = lambda: added_value.operation("+")).grid(row=1 ,column=3, pady=1)

bottonSubtract = Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "orange",
                        command = lambda: added_value.operation("-")).grid(row=2 ,column=3, pady=1)
bottonMultiply = Button(calc, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "orange",
                        command = lambda: added_value.operation("*")) .grid(row=3 ,column=3, pady=1)
bottonDivision = Button(calc, text="/", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "orange",
                        command = lambda: added_value.operation("/")).grid(row=4 ,column=3, pady=1)
bottonZero = Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd =4,
                     bg = "grey", command = lambda: added_value.numberEnter(0)).grid(row=5 ,column=0, pady=1)

bottonDot = Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "blue",
                   command = lambda: added_value.numberEnter(".")).grid(row=5 ,column=1, pady=1)
bottonPlusMinus = Button(calc, text="+-", width=6, height=2, font=('arial', 20, 'bold'), bd =4,
                     bg = "blue", command = added_value.plusminus).grid(row=5 ,column=2, pady=1)
bottonEqual = Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd =4,
                     bg = "blue", command =added_value.sum_of_total).grid(row=5 ,column=3, pady=1)

#Scientific calculator button setup

bottonPi = Button(calc, text="π", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "orange",
                  command = added_value.pi) .grid(row=6 ,column=0, pady=1)

#botton2Pi = Button(calc, text="2π", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "orange",
                   #command = added_value.tau).grid(row=6 ,column=1, pady=1)
bottonCos = Button(calc, text="cos", width=6, height=2, font=('arial', 20, 'bold'), bd =4,bg = "orange",
                   command = added_value.cos).grid(row=6 ,column=1, pady=1)
bottonTan = Button(calc, text="tan", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "orange",
                   command = added_value.tan).grid(row=6 ,column=2, pady=1)
bottonTan = Button(calc, text="sin", width=6, height=2, font=('arial', 20, 'bold'), bd =4, bg = "orange",
                   command = added_value.sin).grid(row=6 ,column=3, pady=1)

#Labels
#labelDisplay =Label(calc, text="Scientific Calculator", font=('arial',30,'bold'), justify=CENTER)
#labelDisplay.grid(row = 0, column = 4, columnspan =4)



#functions

def fncExit():
    fncExit = tkinter.messagebox.askyesno("Scientific Calculator","Confirm Exit")
    if fncExit > 0:
        root.destroy()
        return
def fncStandard():
    root.resizable(width = False, height=False)
    root.geometry("510x560+0+0")
    
def fncScientific():
    root.resizable(width = False, height=False)
    root.geometry("510x670+0+0")


#menu

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

