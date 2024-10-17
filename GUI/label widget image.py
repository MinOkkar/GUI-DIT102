import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x800')
root.title("Label Widget Image")
x = tk.PhotoImage(file= 'python.png' ).subsample(3,3)
y = tk.PhotoImage(file= 'rsu.png').subsample(3,3)

tk.Label(root, text = 'Hi, Python').pack()

ttk.Label(root, image = x).pack()

ttk.Label(root, text= "Hi, RSU").pack()

ttk.Label(root, image = y).pack()


root.mainloop()