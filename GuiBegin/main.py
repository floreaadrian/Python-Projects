from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title','Monkeys.')
answer = tkinter.messagebox.askquestion('Question 1','Yes or no')

if answer == 'yes':
    print(" Hi ")


root.mainloop()
