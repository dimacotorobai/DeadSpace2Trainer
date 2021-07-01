import tkinter as tk

#Make window
window = tk.Tk()
window.geometry('350x500')

#Label
greeting = tk.Label(text='Hello, Tkinter')
greeting.pack()

window.mainloop()