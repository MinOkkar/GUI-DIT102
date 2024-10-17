import tkinter as tk
from tkinter import Menu
from tkinter.messagebox import askyesno

def e():
    answer = askyesno(title = "Confirm", message = 'Do you want to Exit?')
    if answer:
        root.destroy()

def about():
    print("name - Okkar")
    print("ID = 6604133")


root = tk.Tk()
root.title('Test')
menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='file',menu=file_menu)
file_menu.add_command(label="new")
file_menu.add_command(label="exit", command=e )

help_menu = Menu(menubar,tearoff=0,)
menubar.add_cascade(label="Help",menu= help_menu)
help_menu.add_command(label="about",command= about)


root.mainloop()