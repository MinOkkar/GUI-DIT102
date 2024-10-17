import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
#-------------------functions-------------------------

def EXIT():
       answer = askyesno(title='Confirm', message='Do you want to Exit?')
       if answer:
           root.destroy()   

def about():
      def exit_abou():
        abou.destroy()
      abou = tk.Tk()
      abou.title('About')
      abou.geometry('300x84')
      tk.Label(abou, text="Created by Edward for DIT-102 project").pack()
      tk.Label(abou, text="31,July,2024").pack()
      tk.Button(abou, text="OK", command=exit_abou).place(x=260, y=50)
      abou.mainloop()

def dataload(x):  #load text file 
    weapons = []
    with open(x, 'r') as f:
        lines = f.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            thing = dict(zip(headers, values))
            weapons.append(thing)
            listbox.insert(tk.END, thing['name'])
    update_count(len(weapons))
    return weapons

def save_data_to_csv(filename):
    with open(filename, 'w') as f:
        headers = ['name', 'type', 'caliber', 'capacity']
        f.write(','.join(headers) + '\n')
        for thing in things:
            f.write(f"{thing['name']},{thing['type']},{thing['caliber']},{thing['capacity']}\n")

def add_thing():
    name = name_entry.get()
    type_ = type_entry.get()
    cali = cali_entry.get()
    cap = cap_entry.get()
    
    if name and type_ and cali and cap:
        thing = {'name': name, 'type': type_, 'caliber': cali, 'capacity': cap}
        things.append(thing)
        listbox.insert(tk.END, name)
        clear_entries()
        save_data_to_csv("data.csv")
        update_count(len(things))

def clear():
        name_entry.delete(0, tk.END)
        type_entry.delete(0, tk.END)
        cali_entry.delete(0, tk.END)
        cap_entry.delete(0, tk.END)

def load_display(event):
    selected_index = listbox.curselection()
    if selected_index:
        thing = things[selected_index[0]] #delete current and add new
        name_entry.delete(0, tk.END)
        name_entry.insert(0, thing['name'])
        type_entry.delete(0, tk.END)
        type_entry.insert(0, thing['type'])
        cali_entry.delete(0, tk.END)
        cali_entry.insert(0, thing['caliber'])
        cap_entry.delete(0, tk.END)
        cap_entry.insert(0, thing['capacity'])

def delete_thing():
    selected_index = listbox.curselection()
    if selected_index:
        del things[selected_index[0]]
        listbox.delete(selected_index)
        clear_entries()
        save_data_to_csv('data.csv')
        update_count(len(things))

def update_thing():
    selected_index = listbox.curselection()
    if selected_index:
        thing = things[selected_index[0]]
        thing['name'] = name_entry.get()
        thing['type'] = type_entry.get()
        thing['caliber'] = cali_entry.get()
        thing['capacity'] = cap_entry.get()
        listbox.delete(selected_index)
        listbox.insert(selected_index, thing['name'])
        clear_entries()
        save_data_to_csv('data.csv')
        update_count(len(things))

def search():
    search_term = search_entry.get()
    listbox.delete(0, tk.END)
    for thing in things:
        if search_term.lower() in thing['name'].lower():
            listbox.insert(tk.END, thing['name'])

def clear_entries():
    # name_entry.delete(0, tk.END)
    type_entry.delete(0, tk.END)
    cali_entry.delete(0, tk.END)
    cap_entry.delete(0, tk.END)

def update_count(x):
    count.config(text=f"Total Firearm: {x}")

#---------------------interface------------------------ 
root = tk.Tk()
root.title("Blackmarket")
root.geometry('650x350+50+50')
root.iconbitmap(r"io.ico")
weapons = [] #database

menubar = Menu(root)          
root.config(menu=menubar)
h_menu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label="Help", menu=h_menu) 
h_menu.add_cascade(label="Clear", command=clear)
h_menu.add_command(label='About', command=about)
h_menu.add_command(label='Exit', command=EXIT)


name_label = tk.Label(root, text="Name")
name_label.place(x=10, y=30)
name_entry = tk.Entry(root)
name_entry.place(x=65, y=30)

type_label = tk.Label(root, text="Type")
type_label.place(x=10, y = 60)
type_entry = tk.Entry(root)
type_entry.place(x=65, y=60)

cali_label = tk.Label(root, text="Caliber")
cali_label.place(x=10, y=90)
cali_entry = tk.Entry(root)
cali_entry.place(x=65, y=90)

cap_label = tk.Label(root, text="Capacity")
cap_label.place(x=10, y=120)
cap_entry = tk.Entry(root)
cap_entry.place(x=65, y=120)

add = tk.Button(root, text= "Add Firearm",command=add_thing)
add.place(x=90, y=150)

Update = tk.Button(root, text="Update selected Firearm",command=update_thing)
Update.place(x=60, y=180)

delete = tk.Button(root, text= "Delete Firearm",command=delete_thing)
delete.place(x=85, y=210)


#bar and entry search
search_entry = tk.Entry(root)
search_entry.place(x=300,y=30)
search_button = tk.Button(root, text = "Search by name", command=search)
search_button.place(x=430,y=27)

#display
listbox = tk.Listbox(root,width=37,height=13)
listbox.place(x=300,y=60)
listbox.bind('<<ListboxSelect>>', load_display)

count = tk.Label(root, text = "Total Firearm: ")
count.place(x=300,y=300)

things = dataload(r"data.csv")

root.mainloop()