import sqlite3
import tkinter as tk

bg_colour = "#86bd84"

# initialise app
root = tk.Tk()
root.title("Dev Kit Stock Control")
#root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('650x500+' + str(x) + '+' + str(y))

frame1 = tk.Frame(root, width=650, height=500, bg=bg_colour)
frame1.grid(row=0, column=0)
# run app
root.mainloop()
