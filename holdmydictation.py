import tkinter as tk
from tkinter import Text

#indicates we want a widget to expand in all directions 
inflate="swne"

class HMDmain(tk.Frame):
    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self,parent, *args, **kwargs)
        
        

        #define UI elements
        self.parent = parent
        self.text = Text(self)

        #show UI elements by invoking the UI manager on them
        self.text.grid(sticky=inflate)
        self.grid(sticky=inflate)

if __name__ == "__main__":
    root = tk.Tk()
    HMDmain(root).grid(sticky=inflate)
    root.mainloop()
