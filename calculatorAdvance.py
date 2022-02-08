from tkinter import *
root = Tk()
root.title("calculator")
display_scr = Entry(root,width= 25,borderwidth = 5,font = 'Arial 9 bold')
display_scr.grid(row = 0,column = 0,columnspan = 3)

def click(num):
    current = display_scr.get()
    display_scr.delete(0, END)
    display_scr.insert(0,str(current) + str(num))
    
def clear():
    display_scr.delete(0,END)

def add():
    global num
    global opt
    opt = 'add'
    num = int(display_scr.get())
    display_scr.delete(0,END)
    
def sub():
    global num
    global opt
    opt = 'sub'
    num = int(display_scr.get())
    display_scr.delete(0,END)
    
def mul():
    global num
    global opt
    opt = 'mul'
    num = int(display_scr.get())
    display_scr.delete(0,END)

def div():
    global num
    global opt
    opt = 'div'
    num = int(display_scr.get())
    display_scr.delete(0,END)
    
def equal():
    global opt
    num2 = int(display_scr.get())
    display_scr.delete(0,END)
    if opt == "add":
        sum = num + num2
    if opt == "sub":
        sum = num - num2
    if opt == "mul":
        sum = num * num2
    if opt == "div":
        sum = num // num2
    display_scr.insert(0,sum)
    
# head = Label(root,text = "Calculator",font ="arial 10 bold").grid(row=0,column=2)


btn_1 = Button(root,text = "1",padx = 20,pady=20,command = lambda: click(1))
btn_2 = Button(root,text = "2",padx = 20,pady=20,command = lambda: click(2))
btn_3 = Button(root,text = "3",padx = 20,pady=20,command = lambda: click(3))
btn_4 = Button(root,text = "4",padx = 20,pady=20,command = lambda: click(4))
btn_5 = Button(root,text = "5",padx = 20,pady=20,command = lambda: click(5))
btn_6 = Button(root,text = "6",padx = 20,pady=20,command = lambda: click(6))
btn_7 = Button(root,text = "7",padx = 20,pady=20,command = lambda: click(7))
btn_8 = Button(root,text = "8",padx = 20,pady=20,command = lambda: click(8))
btn_9 = Button(root,text = "9",padx = 20,pady=20,command = lambda: click(9))
btn_0 = Button(root,text = "0",padx = 20,pady=20,command = lambda: click(0))
clear_btn = Button(root,text = "clear",padx = 42,pady =20,command = clear)
addition = Button(root,text ="+",padx = 20,pady = 20,command =add)
subtraction = Button(root,text ="-",padx = 20,pady = 20,command =sub)
multiplication = Button(root,text ="*",padx = 20,pady = 20,command =mul)
division = Button(root,text ="/",padx = 20,pady = 20,command =div)
equal = Button(root,text ="=",padx = 51,pady = 20,command = equal)

btn_1.grid(row =4,column =0)
btn_2.grid(row =4,column =1)
btn_3.grid(row =4,column =2)
btn_4.grid(row =2,column =0)
btn_5.grid(row =2,column =1)
btn_6.grid(row =2,column =2)
btn_7.grid(row =1,column =0)
btn_8.grid(row =1,column =1)
btn_9.grid(row =1,column =2)
btn_0.grid(row =5,column =0)
clear_btn.grid(row = 5,column =1,columnspan=2)
addition.grid(row = 6,column = 0)
subtraction.grid(row = 7,column = 0)
multiplication.grid(row = 7,column = 1)
division.grid(row = 7,column = 2)
equal.grid(row =6,column=1,columnspan=2)
root.mainloop()