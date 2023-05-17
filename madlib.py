from tkinter import *

# Create Display Window
w = Tk()
w.geometry('600x400')
w.title('Mad Libs Generator')
Label(w, text= 'Obiwan\'s Mad Libs' , font = 'arial 20 bold').pack()
Label(w, text = 'Select your story:', font = 'arial 15 bold').pack()

w.mainloop()