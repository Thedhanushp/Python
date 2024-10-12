#Graphical User Interface GUI

from tkinter import *

#for making a window 
window = Tk()

window.geometry("300x500")
window.configure(bg="purple")

def hello():
    print("button clicked")
def hey():
    print("hello user") 
    
button1 = Button(text="Okey",command=hello)
button2 = Button(text="Okey",command=hey)

button1.grid(row=1,column=2)
button2.grid(row=3,column=4)

label = Label(window,text="Window")
#to attach the button
"""
button.pack()
label.pack()
"""
#to display the window
window.mainloop()


