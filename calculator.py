from tkinter import *
window=Tk()
window.title("calculator")
entry1=Entry(window,width=60,borderwidth=10,bg="light blue")
entry1.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def addButton(num):
    return Button(window,padx=16,bd=8,fg="blue",text=num,width=5, command= lambda: clickButton(str(num)))



def createButton():
    bttn0 = addButton(0)
    bttn1 = addButton(1)
    bttn2 = addButton(2)
    bttn3 = addButton(3)
    bttn4 = addButton(4)
    bttn5 = addButton(5)
    bttn6 = addButton(6)
    bttn7 = addButton(7)
    bttn8 = addButton(8)
    bttn9 = addButton(9)

    bttn_add = addButton('+')
    bttn_sub = addButton('-')
    bttn_mult = addButton('*')
    bttn_div = addButton('/')
    bttn_clear = addButton('C')
    bttn_equal = addButton('=')

    row1=[bttn7,bttn8,bttn9,bttn_add]
    row2=[bttn4,bttn5,bttn6,bttn_sub]
    row3=[bttn1,bttn2,bttn3,bttn_mult]
    row4=[bttn_clear,bttn0,bttn_equal,bttn_div]

    r=1
    for row in [row1,row2,row3,row4]:
        c=0
        for buttn in row:
             buttn.grid(row=r, column=c, columnspan=1)
             c+=1
        r+=1

def clickButton(value):
    current_eq=str(entry1.get())

    if value =='C':
        entry1.delete(-1,END)
    elif value=='=':
        answer=str(eval(current_eq))
        entry1.delete(-1,END)
        entry1.insert(0,answer)

    else:
        entry1.delete(0,END)
        entry1.insert(0,current_eq+value)



createButton()
window.mainloop()
