from tkinter import *

root = Tk()
root.title("Freedom Block")
WIDTH = 580
HEIGHT = 300
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg='white')

# Text Box
text_box = Text(root, width=30, height=30, padx=15, pady=15)
text_box.place(relx=0.05, rely=0.05)

canvas = Canvas(root, width=700, height=50, bg='white', highlightthickness=0)
canvas.place(relx=0.05, rely=0.9)

label = Label(root, text="Enter website (ex: reddit.com)", padx=30, bg='white')
label.place(relx=0.8, rely=0.1, anchor='n')
entry = Entry(root, width=25)
entry.place(relx=0.8,rely=0.2, anchor='n')
entry.focus()

# Button add file to text box
def display():
    text_box.insert(END, entry.get() + '\n')
    entry.delete(0, END)

add_button = Button(root, text="Add to list", command=display, padx=30, bg='white')
add_button.place(relx=0.8, rely=0.3, anchor='n')

# Button load text file
load_text = StringVar()
load_button = Button(root, textvariable=load_text, command=display, padx=30, bg='white')
load_text.set("Load file")
load_button.place(relx=0.8, rely=0.5, anchor='n')

# Button BLOCK
block_button = Button(root, text="BLOCK", command=display, font=('Helvetica bold', 15),\
                       bg='red', fg='white', padx=30)
block_button.place(relx=0.8, rely=0.7, anchor='n')


root.minsize(WIDTH, HEIGHT)
root.maxsize(700, 500)
root.mainloop()
