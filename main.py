from tkinter import *   

window = Tk()

window.title("Welcome to LikeGeeks app")
window.geometry('350x200')  

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)



def hand_clicked():
    print("Button was clicked !!")

button = Button(window, text='Click Me', width=25)
button.pack()
button.bind("<Button-1>", hand_clicked)

window.mainloop()