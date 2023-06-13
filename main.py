import tkinter as tk
from tkinter import scrolledtext
from tkinter.filedialog import askopenfile
import shutil

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("Malicious Site Blocker")
        self.geometry("580x300")
        self.configure(bg='white')
        
        self.frame = tk.Frame(self, width=300, height=250)
        self.frame.place(relx=0.05, rely=0.05)
        
        # Text Box
        self.text_box = scrolledtext.ScrolledText(self.frame)
        self.text_box.place(x=0, y=0, width=300, height=250)

        # self.canvas = tk.Canvas(self, width=700, height=30, bg='white', highlightthickness=0)
        # self.canvas.place(relx=0.05, rely=0.9)

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

        # Block button
        self.block_button = tk.Button(self, text="BLOCK", command=self.read_text, font=('Helvetica bold', 15),\
                            bg='red', fg='white', padx=30)
        self.block_button.place(relx=0.8, rely=0.8, anchor='n')
        
        # Button to clear text box
        self.clear_button = tk.Button(self, text="Clear text", command=self.clear_text, padx=30, bg="white")
        self.clear_button.place(relx=0.8, rely=0.6, anchor='n')
        
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
            
    # function to clear text box
    def clear_text(self) -> None:
        self.text_box.delete("1.0", tk.END)
    
    # block button functionality
    def read_text(self) -> None:
        
        domains = self.text_box.get("1.0", tk.END)
        
        domains = domains.split("\n")

        domains = [x for x in domains if len(x) > 0]
        
        domains = list(map(lambda x: f"\n127.0.0.1\t{x}\n127.0.0.1\twww.{x}\n", domains))

        with open("hosts_file.txt", "r") as f:
            core = f.read()
        
        for x in domains:
            core += x

        print(core)
        # file = open("hosts", "w")
        # file.writelines(core)
        # file.close()
        
        # shutil.move("hosts", "C:\\Windows\\System32\\drivers\\etc\\hosts")
        
 # -------------------------------------------- #

if __name__ == "__main__":
    app = App()
    app.minsize(580, 300)
    app.maxsize(700, 500)
    app.mainloop()
