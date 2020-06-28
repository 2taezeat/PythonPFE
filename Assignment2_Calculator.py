from tkinter import *

window = None
displayLabel = None
equation = None
expression = ''

def guiMain():
    setupGUI()
    window.mainloop()

def press(num):
    global expression
    if (num == ''):
        expression = expression + str(num)
        expression = expression[:len(expression) - 1]
        equation.set(expression)
    else:
        expression = expression + str(num)
        equation.set(expression)

def cleardisplay():
    global expression
    displayLabel['text'] = "0"
    expression = ''
    equation.set("0")

def equalPress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def setupGUI():
    global window
    global displayLabel
    global equation
    window = Tk()
    window.title('newKalculator')
    window.resizable(width=FALSE,height = FALSE)
    equation = StringVar()
    equation.set('')

    displayLabel = Label(window,textvariable = equation, justify = RIGHT, relief=SUNKEN, width=18, font='Arial 20',fg = 'red', anchor='e')


    displayLabel.grid(row=0, column=0, columnspan=40, padx=10, pady=10)

    btn1 = Button(window, text='1', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(1))
    btn2 = Button(window, text='2', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(2))
    btn3 = Button(window, text='3', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(3))
    btn4 = Button(window, text='4', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(4))
    btn5 = Button(window, text='5', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(5))
    btn6 = Button(window, text='6', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(6))
    btn7 = Button(window, text='7', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(7))
    btn8 = Button(window, text='8', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(8))
    btn9 = Button(window, text='9', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(9))
    btn0 = Button(window, text='0', width=5, height=2, font='Arial 15', fg = 'green',command=lambda: press(0))

    clearBtn = Button(window, text='C', width=5, height=2, font='Arial 15', command = cleardisplay)
    resultBtn = Button(window, text='=', width=5, height=2, font='Arial 15', command = equalPress)
    addBtn = Button(window, text='+', width=5, height=2, font='Arial 15', command=lambda: press('+'))
    subBtn = Button(window, text='-', width=5, height=2, font='Arial 15', command=lambda: press('-'))
    mulBtn = Button(window, text='x', width=5, height=2, font='Arial 15', command=lambda: press('*'))
    divBtn = Button(window, text='÷', width=5, height=2, font='Arial 15', command=lambda: press('/'))

    dotBtn = Button(window, text='.', width=5, height=2, font='Arial 15', command=lambda: press('.'))
    percentBtn = Button(window, text='%', width=5, height=2, font='Arial 15', command=lambda: press('*0.01'))
    backBtn = Button(window, text='<', width=5, height=2, font='Arial 15', command=lambda: press(''))
    squareBtn = Button(window, text='x²', width=5, height=2, font='Arial 15', command=lambda: press('**2'))

    backBtn.grid(row=1, column=1)
    percentBtn.grid(row=1, column=2)
    squareBtn.grid(row=1, column=3)

    btn1.grid(row=2, column=0)
    btn2.grid(row=2, column=1)
    btn3.grid(row=2, column=2)
    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)
    btn7.grid(row=4, column=0)
    btn8.grid(row=4, column=1)
    btn9.grid(row=4, column=2)
    btn0.grid(row=5, column=1)

    dotBtn.grid(row=5, column=0)

    clearBtn.grid(row=1, column=0)
    resultBtn.grid(row=5, column=2)
    addBtn.grid(row=2, column=3)
    subBtn.grid(row=3, column=3)
    mulBtn.grid(row=4, column=3)
    divBtn.grid(row=5, column=3)


guiMain()