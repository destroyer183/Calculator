import tkinter as tk
from tkinter import *
import keyboard

root = tk.Tk()

root.title("Calculator")

root.geometry('350x500')

output = 0
input1 = 0
input2 = 0
memory = 0
addition = False
subtraction = False
multiplication = False
division = False
firstnum = True

equation = tk.Label(root, text = "equation")
equation.configure(font=("Arial", 20, ""))
equation.place(x = 0, y = 0)

display = tk.Label(root, text = "display")
display.configure(font=("Arial", 40, "bold"))
display.place(x = 0, y = 40)

equal = tk.Button(root, text="=", anchor='center', bg='DarkSlateGray2', command=lambda:calculate())
equal.configure(font=("Arial", 20, "bold"))
equal.place(x = 175, y = 470, height = 60, width = 350, anchor='center')

def calculate():
    global output, input1, input2, display, equation
    if addition == True:
        equation.configure(text= str(input1) + " + " + str(input2) + " =")
        input1 = float(input1)
        input1 += float(input2)
        output = input1

    elif subtraction == True:
        equation.configure(text= str(input1) + " - " + str(input2) + " =")
        input1 = float(input1)
        input1 -= float(input2)
        output = input1

    elif multiplication == True:
        equation.configure(text= str(input1) + " x " + str(input2) + " =")
        input1 = float(input1)
        input1 *= float(input2)
        output = input1

    elif division == True:
        equation.configure(text= str(input1) + " / " + str(input2) + " =")
        input1 = float(input1)
        input1 /= float(input2)
        output = input1

    display.configure(text= output)
    print(output)

plus = tk.Button(root, text="+", anchor='center', bg='gainsboro', command=lambda:add())
plus.configure(font=("Arial", 20, "bold"))
plus.place(x = 262.5, y = 380, height = 60, width = 87.5)

def add():
    global output, input1, input2, firstnum, addition, subtraction, multiplication, division, display, equation

    if output == 0:
        if subtraction == True:
            input1 -= input2
            input2 = 0
            subtraction = False

        elif multiplication == True:
            input1 *= input2
            input2 = 0
            multiplication = False

        elif division == True:
            input1 /= input2
            input2 = 0
            division = False
        
    elif output != 0:
        if addition == True:
            input2 = 0
            addition = False
            
        elif subtraction == True:
            input2 = 0
            subtraction = False

        elif multiplication == True:
            input2 = 0
            multiplication = False

        elif division == True:
            input2 = 0
            division = False
    output = 0

    if input1 and input2 != 0:
        input1 += input2
        input2 = 0
        firstnum = False

    firstnum = False
    addition = True
    subtraction = False
    multiplication = False
    division = False

    equation.configure(text= str(input1) + " + ")
    display.configure(text= "0")

minus = tk.Button(root, text="-", anchor='center', bg='gainsboro', command=lambda:subtract())
minus.configure(font=("Arial", 20, "bold"))
minus.place(x = 262.5, y = 320, height = 60, width = 87.5)

def subtract():
    global output, input1, input2, firstnum, addition, subtraction, multiplication, division, display, equation

    if output == 0:
        if addition == True:
            input1 += input2
            input2 = 0
            addition = False

        elif multiplication == True:
            input1 *= input2
            input2 = 0
            multiplication = False

        elif division == True:
            input1 /= input2
            input2 = 0
            division = False
        
    elif output != 0:
        if addition == True:
            input2 = 0
            addition = False
            
        elif subtraction == True:
            input2 = 0
            subtraction = False

        elif multiplication == True:
            input2 = 0
            multiplication = False

        elif division == True:
            input2 = 0
            division = False
    output = 0
    
    if input1 and input2 != 0:
        input1 -= input2
        input2 = 0
        firstnum = False

    firstnum = False
    addition = False
    subtraction = True
    multiplication = False
    division = False

    equation.configure(text= str(input1) + " - ")
    display.configure(text= "0")

multiply = tk.Button(root, text="x", anchor='center', bg='gainsboro', command=lambda:multiplie())
multiply.configure(font=("Arial", 20, "bold"))
multiply.place(x = 262.5, y = 260, height = 60, width = 87.5)

def multiplie():
    global output, input1, input2, firstnum, addition, subtraction, multiplication, division, display, equation

    if output == 0:
        if addition == True:
            input1 += input2
            input2 = 0
            addition = False
        
        elif subtraction == True:
            input1 -= input2
            input2 = 0
            subtraction = False

        elif division == True:
            input1 /= input2
            input2 = 0
            division = False

    elif output != 0:
        if addition == True:
            input2 = 0
            addition = False
            
        elif subtraction == True:
            input2 = 0
            subtraction = False

        elif multiplication == True:
            input2 = 0
            multiplication = False

        elif division == True:
            input2 = 0
            division = False
    output = 0

    if input1 and input2 != 0:
        input1 *= input2
        input2 = 0
        firstnum = False

    firstnum = False
    addition = False
    subtraction = False
    multiplication = True
    division = False

    equation.configure(text= str(input1) + " x ")
    display.configure(text= "0")

divide = tk.Button(root, text="/", anchor='center', bg='gainsboro', command=lambda:divyde())
divide.configure(font=("Arial", 20, "bold"))
divide.place(x = 262.5, y = 200, height = 60, width = 87.5)

def divyde():
    global output, input1, input2, firstnum, addition, subtraction, multiplication, division, display, equation

    if output == 0:
        if addition == True:
            input1 += input2
            input2 = 0
            addition = False
        
        elif subtraction == True:
            input1 -= input2
            input2 = 0
            subtraction = False

        elif multiplication == True:
            input1 *= input2
            input2 = 0
            multiplication = False

    elif output != 0:
        if addition == True:
            input2 = 0
            addition = False
            
        elif subtraction == True:
            input2 = 0
            subtraction = False

        elif multiplication == True:
            input2 = 0
            multiplication = False

        elif division == True:
            input2 = 0
            division = False
    output = 0

    if input1 and input2 != 0:
        input1 *= input2
        input2 = 0
        firstnum = False

    firstnum = False
    addition = False
    subtraction = False
    multiplication = False
    division = True

    equation.configure(text= str(input1) + " / ")
    display.configure(text= "0")

clear = tk.Button(root, text="CE", anchor='center', bg='gainsboro', command=lambda:clearall())
clear.configure(font=("Arial", 20, "bold"))
clear.place(x = 262.5, y = 140, height = 60, width = 87.5)

def clearall():
    global output, input1, input2, addition, subtraction, multiplication, division, firstnum
    output = 0
    input1 = 0
    input2 = 0
    addition = False
    subtraction = False
    multiplication = False
    division = False
    firstnum = True

    display.configure(text="display")

    equation.configure(text="equation")

decimal = tk.Button(root, text=".", anchor='center', bg='white', command=lambda:assigndecimal())
decimal.configure(font=("Arial", 20, "bold"))
decimal.place(x = 175, y = 380, height = 60, width = 87.5)

def assigndecimal():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 = str(input1) + "."

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 = str(input2) + "."

        display.configure(text=input2)
    print(input1)
    print(input2)

integer = tk.Button(root, text="+/-", anchor='center', bg='white', command=lambda:integerassign())
integer.configure(font=("Arial", 20, "bold"))
integer.place(x = 0, y = 380, height = 60, width = 87.5)

def integerassign():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 = "-"
        else:
            input1 = "-" + str(input1)
            
        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 = "-"
        else:
            input2 = "-" + str(input2)

        display.configure(text=input2)

num0 = tk.Button(root, text="0", anchor='center', bg='white', command=lambda:assign0())
num0.configure(font=("Arial", 20, "bold"))
num0.place(x = 87.5, y = 380, height = 60, width = 87.5)

def assign0():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 = 0
        else:
            input1 = str(input1) + "0"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 = 0
        else:
            input2 = str(input2) + "0"

        display.configure(text=input2)
    print(input1)
    print(input2)

keyboard.on_press_key("0", lambda _:assign0())

num3 = tk.Button(root, text="3", anchor='center', bg='white', command=lambda:assign3())
num3.configure(font=("Arial", 20, "bold"))
num3.place(x = 175, y = 320, height = 60, width = 87.5)

def assign3():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 += 3
        else:
            input1 = str(input1) + "3"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 += 3
        else:
            input2 = str(input2) + "3"

        display.configure(text=input2)
    print(input1)
    print(input2)

num1 = tk.Button(root, text="1", anchor='center', bg='white', command=lambda:assign1())
num1.configure(font=("Arial", 20, "bold"))
num1.place(x = 0, y = 320, height = 60, width = 87.5)

def assign1():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 += 1
        else:
            input1 = str(input1) + "1"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 += 1
        else:
            input2 = str(input2) + "1"

        display.configure(text=input2)
    print(input1)
    print(input2)

num2 = tk.Button(root, text="2", anchor='center', bg='white', command=lambda:assign2())
num2.configure(font=("Arial", 20, "bold"))
num2.place(x = 87.5, y = 320, height = 60, width = 87.5)

def assign2():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 += 2
        else:
            input1 = str(input1) + "2"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 += 2
        else:
            input2 = str(input2) + "2"

        display.configure(text=input2)
    print(input1)
    print(input2)

num6 = tk.Button(root, text="6", anchor='center', bg='white', command=lambda:assign6())
num6.configure(font=("Arial", 20, "bold"))
num6.place(x = 175, y = 260, height = 60, width = 87.5)

def assign6():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 += 6
        else:
            input1 = str(input1) + "6"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 += 6
        else:
            input2 = str(input2) + "6"

        display.configure(text=input2)
    print(input1)
    print(input2)

num4 = tk.Button(root, text="4", anchor='center', bg='white', command=lambda:assign4())
num4.configure(font=("Arial", 20, "bold"))
num4.place(x = 0, y = 260, height = 60, width = 87.5)

def assign4():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 += 4
        else:
            input1 = str(input1) + "4"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 += 4
        else:
            input2 = str(input2) + "4"

        display.configure(text=input2)
    print(input1)
    print(input2)

num5 = tk.Button(root, text="5", anchor='center', bg='white', command=lambda:assign5())
num5.configure(font=("Arial", 20, "bold"))
num5.place(x = 87.5, y = 260, height = 60, width = 87.5)

def assign5():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 += 5
        else:
            input1 = str(input1) + "5"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 += 5
        else:
            input2 = str(input2) + "5"

        display.configure(text=input2)
    print(input1)
    print(input2)

num9 = tk.Button(root, text="9", anchor='center', bg='white', command=lambda:assign9())
num9.configure(font=("Arial", 20, "bold"))
num9.place(x = 175, y = 200, height = 60, width = 87.5)

def assign9():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 += 9
        else:
            input1 = str(input1) + "9"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 += 9
        else:
            input2 = str(input2) + "9"

        display.configure(text=input2)
    print(input1)
    print(input2)


num7 = tk.Button(root, text="7", anchor='center', bg='white', command=lambda:assign7())
num7.configure(font=("Arial", 20, "bold"))
num7.place(x = 0, y = 200, height = 60, width = 87.5)

def assign7():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 += 7
        else:
            input1 = str(input1) + "7"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 += 7
        else:
            input2 = str(input2) + "7"

        display.configure(text=input2)
    print(input1)
    print(input2)

num8 = tk.Button(root, text="8", anchor='center', bg='white', command=lambda:assign8())
num8.configure(font=("Arial", 20, "bold"))
num8.place(x = 87.5, y = 200, height = 60, width = 87.5)

def assign8():
    global input1, input2
    if firstnum == True:
        if str(input1) == "0":
            input1 += 8
        else:
            input1 = str(input1) + "8"

        display.configure(text=input1)

    elif firstnum == False:
        if str(input2) == "0":
            input2 += 8
        else:
            input2 = str(input2) + "8"

        display.configure(text=input2)
    print(input1)
    print(input2)

memrecall = tk.Button(root, text="MR", anchor='center', bg='gainsboro', command=lambda:memoryrecall())
memrecall.configure(font=("Arial", 20, "bold"))
memrecall.place(x = 175, y = 140, height = 60, width = 87.5)

def memoryrecall():
    global input1, input2
    if firstnum == True:
        input1 = memory
        display.configure(text=input1)

    elif firstnum == False:
        input2 = memory
        display.configure(text=input2)

memadd = tk.Button(root, text="M+", anchor='center', bg='gainsboro', command=lambda:memoryadd())
memadd.configure(font=("Arial", 20, "bold"))
memadd.place(x = 87.5, y = 140, height = 60, width = 87.5)

def memoryadd():
    global memory
    memory = float(display.cget("text"))

memclear = tk.Button(root, text="M-", anchor='center', bg='gainsboro', command=lambda:memoryclear())
memclear.configure(font=("Arial", 20, "bold"))
memclear.place(x = 0, y = 140, height = 60, width = 87.5)

def memoryclear():
    global memory
    memory = 0

root.resizable(False, False)
root.mainloop()