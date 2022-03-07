import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
import shutil

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("Degenerate Blocker")
        self.geometry("580x300")
        self.configure(bg='white')

        # Text Box
        self.text_box = tk.Text(self, width=30, height=30, padx=15, pady=15)
        self.text_box.place(relx=0.05, rely=0.05)

        self.canvas = tk.Canvas(self, width=700, height=50, bg='white', highlightthickness=0)
        self.canvas.place(relx=0.05, rely=0.9)

        self.label = tk.Label(self, text="Enter website (ex: reddit.com)", padx=30, bg='white')
        self.label.place(relx=0.8, rely=0.1, anchor='n')
        
        self.entry = tk.Entry(self, width=25)
        self.entry.place(relx=0.8,rely=0.2, anchor='n')
        self.entry.focus()

        # Button add file to text box
        self.add_button = tk.Button(self, text="Add to list", command=self.display, padx=30, bg='white')
        self.add_button.place(relx=0.8, rely=0.3, anchor='n')

        # Button load text file
        self.load_text = tk.StringVar()
        self.load_button = tk.Button(self, textvariable=self.load_text, command=lambda:self.load_file(), padx=30, bg='white')
        self.load_text.set("Load file")
        self.load_button.place(relx=0.8, rely=0.5, anchor='n')

        self.block_button = tk.Button(self, text="BLOCK", command=self.read_text, font=('Helvetica bold', 15),\
                            bg='red', fg='white', padx=30)
        self.block_button.place(relx=0.8, rely=0.7, anchor='n')

    # display entries in text box
    def display(self) -> None:
        self.text_box.insert(tk.END, self.entry.get() + '\n')
        self.entry.delete(0, tk.END)
    
    # load file button functionality
    def load_file(self) -> None:
        self.load_text.set("Loading...")
        file = askopenfile(mode='rb', title="Choose a file", filetype=[("Text file", "*.txt")])
        if(file):
            read_file = file.read()
            self.text_box.insert(tk.END, read_file)
            self.load_text.set("Load file")
    
    # block button functionality
    def read_text(self) -> None:
        
        domains = self.text_box.get("1.0", tk.END)
        
        domains = domains.split("\n")

        domains = [x for x in domains if len(x) > 0]
        
        def change(str_: str) -> str:
            str_ = f"127.0.0.1\t{str_}\n127.0.0.1\twww.{str_}\n"
            return str_
        
        domains = list(map(change, domains))

        core = '''# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

'''
        
        for x in domains:
            core += x

        file = open("hosts", "w")
        file.writelines(core)
        file.close()
        
        shutil.move("hosts", "C:\\Windows\\System32\\drivers\\etc\\hosts")
        
 # -------------------------------------------- #

if __name__ == "__main__":
    app = App()
    app.minsize(580, 300)
    app.maxsize(700, 500)
    app.mainloop()
