from tkinter import *

# Create Display Window
w = Tk()
w.geometry('600x400')
w.title('Mad Libs App')
Label(w, text= 'Obiwan\'s Mad Libs' , font = 'arial 20 bold', bg='black', fg='green2').pack()
Label(w, text = 'Select your story:', font = 'arial 15 bold', bg='black', fg='green2').pack()
w.configure(bg='black')

w.mainloop()