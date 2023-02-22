from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
from datetime import datetime

GUI = Tk() #หน้าจอหลังโปรแกรม
GUI.title('海外仓 WMS V.1.10') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม
GUI.resizable(0,0) #ปิดการย่อขยายหน้าต่าง
time = datetime.now() .strftime('%Y-%m-%d %H:%M:%S')

canvas = Canvas(GUI, width=500, height=400)
canvas.pack()
bg_img = PhotoImage(file='//Users//mac//Desktop//Python101//images//fullfill1.png')
canvas.create_image(100,200, image=bg_img, anchor=CENTER)

L1 = Label(GUI,text='海外仓 WMS V.1.10',font=('Angsana New' ,30),fg='white')
L1.place(x=125,y=20)

L2 = Label(GUI,text='{}'.format(time),fg='white')
L2.place(x=350,y=370)

#####################################
def Button1():
    text = 'โปรดแสกนบาร์โค้ดเพื่อทำการรับเข้า'
    messagebox.showinfo('Inbound' ,text)
    
FB1 = Frame(GUI)
FB1.place(x=178 ,y=100)
B1 = ttk.Button(FB1,text='Inbound',width=14, command=Button1)
B1.pack()

#####################################
def Button2():
    text = "You don't authorization,Please contact inventory Manager!"
    messagebox.showwarning('Outbound' ,text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=178 ,y=130)
B2 = ttk.Button(FB2,text='Outbound',width=14, command=Button2)
B2.pack()

#####################################
def Button3():
    text = "You don't authorization,Please contact inventory Manager!"
    messagebox.showwarning('Inventory' ,text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=178 ,y=160)
B3 = ttk.Button(FB3,text='Inventory',width=14, command=Button3)
B3.pack()

#####################################
def Button4():
    text = "You don't authorization,Please contact inventory Manager!"
    messagebox.showwarning('Goods maintenance' ,text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=178 ,y=190)
B3 = ttk.Button(FB3,text='Goods maintenance',width=14, command=Button4)
B3.pack()

#####################################
def Button5():
    text = "You don't authorization,Please contact inventory Manager!"
    messagebox.showwarning('History' ,text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=178 ,y=220)
B3 = ttk.Button(FB3,text='History',width=14, command=Button5)
B3.pack()

GUI.mainloop()
