from tkinter import *
#from PIL import Image, ImageTk
import requests
from os import system as c


window = Tk()
window.geometry("400x400")
#set size permanently   #or you can use window.resizabld(false, false)
window.minsize(500, 500)
window.maxsize(500, 500)
window.title("Smaron")

#window.iconbitmap("E:\\downloads\\icon.ico")

#---------------------------------------------------------------------------------------------------------------
    #first get the picture then save it in pic and set as background
label0 = Label(background='gray')
    #label0.place(x=40,y=150)
label0.pack(fill = BOTH, expand = 'yes')

def lblf():
    label4 = Label(window, text ='                                       ', fg = "gray", font = ("Z003",  16, "bold"), bg="gray")
    label4.place(x = 0, y = 200)
    

    label5 = Label(window, text = f"                                    ",fg='gray', font = ("arial", 16, "bold"),bg='gray')
    label5.place(x = 150, y = 200)
    
    label6 = Label(window, text = f"                                    ", fg = "gray", font = ("Z003",  16, "bold"), bg="gray")
    label6.place(x = 0, y = 250)
    
    label7 = Label(window, text = f"                                    ",fg='gray', font = ("arial", 16, "bold"),bg='gray')
    label7.place(x = 150, y = 250)
    
def lbl(a,b,c,d):
    label1 = Label(window, text = f"    DEC : {a} ", fg = "gray", font = ("Z003",  16, "bold"), bg="black")
    label1.place(x = 0, y = 200)

    label2 = Label(window, text = f"    BIN : {b} ", font = ("arial", 16, "bold"))
    label2.place(x = 200, y = 200)

    label1 = Label(window, text = f"    OCT : {c} ", fg = "gray", font = ("Z003",  16, "bold"), bg="black")
    label1.place(x = 0, y = 250)

    label2 = Label(window, text = f"    HEX : {d} ", font = ("arial", 16, "bold"))
    label2.place(x = 200, y = 250)


def decimalto():
    lblf()

    d=int(decimal.get())

    h=hex(d)
    o=oct(d)
    b=bin(d)
    lbl(d,b[2:],o[2:],h[2:])

def hexto():
    lblf()
    h=decimal.get()
    dec = int(h, 16)
    o=oct(dec)
    b=bin(dec)
    lbl(dec,b[2:],o[2:],h)

def octalto():
    lblf()
    o=decimal.get()
    dcimal = 0
    length = len(o)
    for x in  o:
        length = length-1
        dcimal += pow(8,length) * int(x)
    d=dcimal
    h=hex(d)
    b=bin(d)
    lbl(d,b[2:],o,h[2:])
def bia( ):
    lblf()

    b=decimal.get()
    n=len(b)
    res=0
    for i in range(1,n+1):
        res=res+ int(b[i-1])*2**(n-i)
        print(f'2|__{int(b[i-1])}__--- {res}\n ')
    d=res
    h=hex(d)
    o=oct(d)
    lbl(d,b,o[2:],h[2:])
def exit():
    window.destroy()
def login():
    uname=decimal.get()
    pasw=passw.get()

    if pasw=="Smaron" and uname=="Smaron":
        print("done")
        window.destroy()
        window1 = Tk()
        window1.geometry("1000x700")
        def add():
    
            global y 
            label2 = Label(window1, text = "UserName :", font = ("arial", 11, "bold"))
            label2.place(x = 0, y = y)

            decimal = StringVar()
            textBox1 = Entry(window1, text="hi", textvar = decimal, width = 30, font = ("arial", 11, "bold"))
            textBox1.place(x = 150, y = y)
            
            label2 = Label(window1, text = "Password :", font = ("arial", 11, "bold"))
            label2.place(x = 0, y = y+50)

            passw= StringVar()
            textBox1 = Entry(window1, text="hi", textvar = passw, width = 30, font = ("arial", 11, "bold"))
            textBox1.place(x = 150, y = y+50)

            y=y+100
            print(y)
        button1 = Button(window1, text = "   Add   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = add)
        button1.place(x = 50, y = 100)
        window1.maxsize(1000, 700)
        window1.title("Smaron")
        window1.mainloop()
x=0
y=150


    
  

label1 = Label(window, text = " Converter ", fg = "gray", font = ("Z003",  40, "bold"), bg="black")
label1.place(x = 150, y = 50)

label2 = Label(window, text = "UserName :", font = ("arial", 16, "bold"))
label2.place(x = 0, y = 150)

decimal = StringVar()
textBox1 = Entry(window, text="hi", textvar = decimal, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 150, y = 150)

label2 = Label(window, text = "Password :", font = ("arial", 16, "bold"))
label2.place(x = 0, y = 200)

passw= StringVar()
textBox1 = Entry(window, text="hi", textvar = passw, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 150, y = 200)


button1 = Button(window, text = " Decimal ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = decimalto)
button1.place(x = 0, y = 300)



button1 = Button(window, text = "   Exit  ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = exit)
button1.place(x = 200, y = 250)
button1 = Button(window, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 200, y = 350)

#display window

window.mainloop()
