import tkinter as tk

root= tk.Tk()

label = tk.Label(root,text='')
label.pack()



f = open("data.scv")
lines = f.readlines()
datas = ''
for x in lines:
    datas += x


label['text'] = datas

root.mainloop()