import sys
from tkinter import *
def mhello():
    text = ment.get
    mlabel2 = Label(mgui, text=text).pack()
    return

mgui = Tk()
ment = StringVar

mgui.geometry('170x220+500+300')
mgui.title('test')
mlabel = Label(mgui, text='Player 1 name').pack()
mEntry = Entry(mgui,textvariable=ment).pack()
#mlabel = Label(mgui, text='Player 2 name').pack()
#mEntry = Entry(mgui,textvariable=ment).pack()
mbutton = Button(mgui,text = 'start', command = mhello, fg= 'black',bg = 'white').pack()
mgui.mainloop()