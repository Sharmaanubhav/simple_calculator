from tkinter import *
root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=45,borderwidth=5)
e.grid(column=0,row=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0, END)
def add():
    first=e.get()
    global first_num
    global math
    math="add"
    first_num=first
    e.delete(0,END)
def sub():
    first=e.get()
    global first_num
    global math
    math="sub"
    first_num=first
    e.delete(0,END)
def mul():
    first=e.get()
    global first_num
    global math
    math="mul"
    first_num=first
    e.delete(0,END)
def div():
    first=e.get()
    global first_num
    global math
    math="div"
    first_num=first
    e.delete(0,END)

def equal():
    second=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,int(second)+int(first_num))
    if math=="sub":
        e.insert(0,int(first_num)-int(second))
    if math=="mul":
        e.insert(0,int(second)*int(first_num))
    if math=="div":
        if int(second)==0:
            e.insert(0,"not defined")
        else:    
            e.insert(0,int(first_num)/int(second))        
#defining buttons    
button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_add=Button(root,text="+",padx=39,pady=20,command=add)
button_equal=Button(root,text="=",padx=91,pady=20,command=equal)
button_clear=Button(root,text="Clear",padx=80,pady=20,command=clear)
button_sub=Button(root,text="-",padx=41,pady=20,command=sub)
button_mul=Button(root,text="*",padx=41,pady=20,command=mul)
button_div=Button(root,text="/",padx=41,pady=20,command=div)
# placing buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)

button_mul.grid(row=5,column=0)
button_clear.grid(row=5,column=1,columnspan=2)

button_div.grid(row=6,column=0)
button_equal.grid(row=6,column=1,columnspan=2)

root.mainloop()