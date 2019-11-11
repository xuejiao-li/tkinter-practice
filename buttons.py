# Codemy.com on YOUTUBE Create Graphical User Interfaces With Python and TKINTER

import tkinter as tk 

root = tk.Tk()

def myClick():
    myLabel = tk.Label(root, text="Look! I clicked a button!!")
    myLabel.pack()

myButton = tk.Button(root, text="Click Me!", command=myClick, padx=50, pady=50, fg="blue", bg="red") #Just remember that when you cal the function for command do not add () at the end. 

myButton.pack()

root.mainloop()