import tkinter as tk
import darkIO
from tkinter import Menu
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror

#indicates we want a widget to expand in all directions
inflate = "swne"


class HMDmain(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.parent.option_add('*tearOff', False)

        #set this frame to expand to %100 available space
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #init menu
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Save", command=self.onSave)
        fileMenu.add_command(label="Load", command=self.onLoad)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        #init textbox
        self.text = ScrolledText(self, wrap='word')

        #add widgets to the layout manager
        self.text.grid(sticky=inflate)

    def onExit(self):
        self.quit()

    def onSave(self):
        darkIO.DarkIO.save(asksaveasfilename(), self.text.get(0.0, 'end'))

    def onLoad(self):
        if not askyesno(
                "Clear All Text",
                "Loading a new file will clear the current project \n"
                "Would you like to continue?"):
            return

        loadText = ""
        try:
            fname = askopenfile()
            loadText = darkIO.DarkIO.load(fname.name)
        except UnicodeDecodeError:
            showerror("Invalid File Type", "Unable to read file.")
        else:
            self.text.delete(0.0, 'end')
            self.text.insert(0.0, loadText)


if __name__ == "__main__":
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    HMDmain(root).grid(sticky=inflate)

    root.mainloop()
