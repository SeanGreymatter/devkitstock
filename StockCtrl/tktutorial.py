from tkinter import *

headertxt = ("arial", 12, "bold")
buttontxt = ("arial", 8, "bold")

window = Tk()
# window.geometry("300x300")
window.title("Hello World")

frame = Frame(window, padx=50, pady=50)
frame.grid(row = 0, column = 0, sticky = "nsew")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

label_1 = Label(window, text = "Welcome to the World", font = headertxt)
label_1.grid(row=1, column=1, padx=10, pady=10)

button1 = Button(window,text="Button", font = buttontxt)
button1.grid(row=1, column=0, padx=10, pady=10)


window.mainloop()