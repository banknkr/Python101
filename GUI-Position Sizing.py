from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('300x150')
GUI.title('Position sizing')       

L1=Label(GUI, text = 'Stock Price (THB)')
L1.place(x=10,y=10)
L1.pack()
E1=Entry(GUI)
E1.pack()


L2=Label(GUI, text = 'Capital (THB)')
L2.place(x=10,y=50)
L2.pack()
E2=Entry(GUI)
E2.pack()

L3 = Label(GUI)
L3.place(x=10,y=100)
L3.pack()

def cal():
    stock = float(E1.get())
    capital = float(E2.get())
    amount = capital / stock
    L3.config(text='Amount = {:.2f}'.format(amount))

B1=Button(GUI, text = 'Calculate',command = cal)
B1.place(x=10,y=70)
B1.pack()

def res():
    E1.delete(0,END)
    E2.delete(0,END)
    L3.config(text='Amount = {:.2f}'.format(0))

B2=Button(GUI, text = 'Reset',command = res)
B2.place(x=10,y=100)
B2.pack()

GUI.mainloop()
