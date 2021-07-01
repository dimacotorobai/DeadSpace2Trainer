import tkinter as tk

class Window():
    def __init__(self, master):
        self.master = master
        master.title('Dead Space™ 2 Hack')
        master.geometry('300x500')

        self.label = tk.Label(master=master, text='Label1')
        self.label.pack()

        self.greet_button = tk.Button(master=master, text='Press Me')
        self.greet_button.pack()

        self.close_button = tk.Button(master=master, text='Close App', command = master.quit)
        self.close_button.pack()

root = tk.Tk()
my_gui = Window(root)
root.mainloop()