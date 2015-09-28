import tkinter as tk
from tkinter.scrolledtext import ScrolledText

#indicates we want a widget to expand in all directions
inflate = "swne"


class HMDmain(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        #set this frame to expand to %100 available space
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #initialise internal UI elements
        self.text = ScrolledText(self, wrap='word')
        
        #add widgets to the layout manager
        self.text.grid(sticky=inflate)


if __name__ == "__main__":
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    HMDmain(root).grid(sticky=inflate)

    root.mainloop()
