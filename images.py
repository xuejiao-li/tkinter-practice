from tkinter import *

from PIL import ImageTk, Image


root = Tk()
root.title('Learn to Code at Codem.com')
# png file 16 * 16, 32 * 32, 64 * 64 

#root.iconbitmap('c:/gui/codemy.ico')

my_img = ImageTk.PhotoImage(Image.open("gui/tree.jpg"))
my_label = Label(image=my_img)
my_label.pack()








button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()