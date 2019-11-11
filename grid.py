# Codemy.com on YOUTUBE Create Graphical User Interfaces With Python and TKINTER

import tkinter as tk 

root = tk.Tk()

# Creating a Label Widget
myLabel = tk.Label(root, text="Hello World!")
myLabe2 = tk.Label(root, text="My Name Is Xuejiao Li!")

# Shoving it onto the screen 

myLabel.grid(row=0, column=0)
myLabe2.grid(row=1, column=1) # they are all relative to each other. If you put column to 5, the position of myLabel2 will not change. 

root.mainloop()