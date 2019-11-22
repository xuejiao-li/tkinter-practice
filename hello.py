# Codemy.com on YOUTUBE Create Graphical User Interfaces With Python and TKINTER

import tkinter as tk 
import tkinter.messagebox

root = tk.Tk()
root.title('tkinter practice')

# Creating a Label Widget

root.geometry('800x800+300+100')
label_1 = tk.Label(root,
    text='Hello World!',
    width=50,
    font=('',18),
    bg='sky blue',
    fg='white',
    pady=10,
    anchor=tk.E
    )

label_1.pack(padx=5, pady=5)

sv=tk.StringVar()
entry_1 =tk.Entry(root, 
    textvariable=sv,
    font=('',16), 
    width=30,
    bg='black',
    fg='white',
    justify=tk.RIGHT,
    bd=5
    )
entry_1.pack(padx=5, pady=5)

sv.set('enter something')

def button_1():
    if button_1_v.get() == 'Click me':
        button_1_v.set('You clicked me')
    else:
        button_1_v.set('Click me')
# Shoving it onto the screen 
button_1_v = tk.StringVar()

button_1 = tk.Button(root, textvariable=button_1_v, command=button_1)
button_1_v.set('Click me')
button_1.pack()

def frame_color_enter(event):
    frame_1.config(bg='red')

def frame_color_default(event): # have to add one argument 
    frame_1.config(bg='black')

def fram_button_1(event):
    tk.messagebox.showinfo('title','you clicked once')

def fram_double_button_1(event):
    tk.messagebox.showinfo('title', 'you clicked twice')

frame_1 = tk.Frame(root, width=400, height=400,bg='black')
frame_1.pack()
frame_1.bind('<Enter>', frame_color_enter)
frame_1.bind('<Leave>', frame_color_default)
# frame_1.bind('<Button-1>', fram_button_1)
frame_1.bind('<Double-Button-1>', fram_double_button_1)


def show():
    tk.messagebox.showinfo('Title', 'You selected: ' + clicked.get())

options = [
    'Monday',
    'Tuesday',
    'Thursday',
    'Friday'
]

clicked = tk.StringVar()
clicked.set(options[0])

drop = tk.OptionMenu(root, clicked, *options)
drop.pack()

my_button = tk.Button(root, text='show selection', command=show)
my_button.pack()

import random

list_1 = [x for x in range(100)]
# print(list_1)

for x in list_1:
    for c in range(10):
        print('{0:<10}'.format(list_1.pop(0)), end=' ')
    print() # to print \n


root.mainloop()