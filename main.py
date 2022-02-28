import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
#import arrange # runs whole arrange.py automatically (needs to include if __name__..)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("Freedom Block")
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
        self.load_button = tk.Button(self, textvariable=self.load_text, command=self.display, padx=30, bg='white')
        self.load_text.set("Load file")
        self.load_button.place(relx=0.8, rely=0.5, anchor='n')

        self.block_button = tk.Button(self, text="BLOCK", command=self.read_text, font=('Helvetica bold', 15),\
                            bg='red', fg='white', padx=30)
        self.block_button.place(relx=0.8, rely=0.7, anchor='n')


    def display(self) -> None:
        self.text_box.insert(tk.END, self.entry.get() + '\n')
        self.entry.delete(0, tk.END)

    def read_text(self) -> None:
        self.block_file = open("block.txt","w")
        self.block_file.writelines(self.text_box.get("1.0", "end-1c"))

        

if __name__ == "__main__":
    app = App()
    app.minsize(580, 300)
    app.maxsize(700, 500)
    app.mainloop()
