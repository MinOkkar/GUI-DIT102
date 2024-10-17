import tkinter as tk
from tkinter import ttk
main = tk.Tk()
tk.Label(main, text = "insert here").pack()
textbox = ttk.Entry(main)
textbox.focus()
textbox.pack()

def Printc():
    print(f"did you just said {textbox.get()} ?")


w = ttk.Button(main,text="Print",command=Printc)
w.pack()
main.mainloop()
