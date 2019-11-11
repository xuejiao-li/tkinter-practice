# Codemy.com on YOUTUBE Creating Input Field With Python and TKINTER

import tkinter as tk 

root = tk.Tk()

e = tk.Entry(root, width=50, bg='blue', fg='white')

e.pack()
e.insert(0, 'Enter Your Name')

def myClick():
    hello = 'hello ' + e.get()
    myLabel = tk.Label(root, text=hello)
    myLabel.pack()

myButton = tk.Button(root, text="Enter Your Name",command=myClick, fg="blue", bg="red") #Just remember that when you cal the function for command do not add () at the end. 

myButton.pack()

root.mainloop()