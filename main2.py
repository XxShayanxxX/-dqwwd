from tkinter import *   
from tkinter import messagebox

window = Tk()

window.title("HELLO ")
window.geometry('350x200')

def msg():
    messagebox.showwarning("Alert", "Your compuer is hacked")

button = Button(window, text='Click Me :D', width=25)
button.pack()

window.mainloop()