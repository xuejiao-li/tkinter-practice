import tkinter as tk

window = tk.Tk()

window.title("Memo list")

# width x height + x_offset + y_offset, 
# it has to be next to the sign 
window.geometry("400x400+600+100")

def insertitem():
    listbox.insert(tk.END, content.get())

def deletelist():
    listbox.delete(0, tk.END)

def deleteitemselected():
    listbox.delete(tk.ANCHOR)


label = tk.Label(window, text = "Insert the Items below")
label.pack()
button = tk.Button(window, text = "Insert Item", command=insertitem)
button.pack()

button_delete = tk.Button(window, text = "Delete list", command=deletelist)
button_delete.pack()

button_delete_selected = tk.Button(window, text = "Delete selected Item", command=deleteitemselected)
button_delete_selected.pack()



content = tk.StringVar()
entry = tk.Entry(window, textvariable = content)
entry.pack()

listbox = tk.Listbox(window)
listbox.pack()


window.mainloop()