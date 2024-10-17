import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry('300x200')
root.title('Button Widget')
tk.Label(root, text='Height').pack()
ttk.Entry(root, textvariable = tk.StringVar()).pack()
tk.Label(root, text='Width').pack()
ttk.Entry(root, textvariable = tk.StringVar()).pack()
root.mainloop()
