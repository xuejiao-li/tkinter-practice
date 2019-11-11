# Codemy.com on YOUTUBE Create Graphical User Interfaces With Python and TKINTER

import tkinter as tk 

root = tk.Tk()

# Creating a Label Widget
myLabel = tk.Label(root, text="Hello World!")

# Shoving it onto the screen 
myLabel.pack()

root.mainloop()