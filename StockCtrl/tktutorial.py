from tkinter import *

headertxt = ("arial", 12, "bold")
buttontxt = ("arial", 8, "bold")

window = Tk()
window.geometry("300x300")
window.title("Hello World")

# frame = Frame(window, padx=500, pady=500)
# frame.grid(row = 0, column = 0, sticky = "nsew",)
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)

def printt():
    print("TKinter Tutorial")

def exit_window():
    exit()

label_1 = Label(window, text = "Welcome to the World", font = headertxt)
label_1.pack()

button1 = Button(window,text="Submit", font = buttontxt, command = printt)
button1.place(x=100, y=100)

button2 = Button(window,text="Close", font = buttontxt, command = exit_window)
button2.place(x=150, y=100)

window.mainloop()