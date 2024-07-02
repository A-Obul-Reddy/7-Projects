import tkinter as tk
import tkinter.ttk as ttk
from gtts import gTTS
import tkinter.filedialog as fl

root = tk.Tk()
root.title("Text to Speech")
root.geometry("500x450")
root.config(bg="#3d3d3d")


def new_entry():
    button1.config(text="Generate", command=generate)
    entry1.config(state="normal")
    entry1.delete(0, tk.END)


def generate():
    entry1.config(state="disabled")
    text = entry1.get(0.0, tk.END)
    tts = gTTS(text)
    tts.save(path.get() + "/" + entry2.get() + ".mp3")
    button1.config(text="New Text", command=new_entry)


def directory():
    path.set(fl.askdirectory())
    if path.get():
        label2.config(text="select location " + path.get())


label1 = ttk.Label(root, text="Enter the text to convert it into speech",
                   font=("Times New Roman", 20),
                   background="#3d3d3d",
                   foreground="#00fc43")
label1.pack(padx=30, pady=10)

entry1 = tk.Text(root, width=400, height=5)
entry1.pack(padx=10, pady=10)

label2 = ttk.Label(root, text="select location ",
                   background="#3d3d3d",
                   foreground="#00fc43",
                   justify="center")
label2.pack(padx=10, pady=10)

button0 = ttk.Button(root,
                     text="Browse directory",
                     command=directory)
button0.pack(padx=10, pady=10)

path = tk.StringVar()

label3 = ttk.Label(root, text="Enter the name of file",
                   background="#3d3d3d",
                   foreground="#00fc43",
                   justify="center")
label3.pack(padx=10, pady=10)

entry2 = ttk.Entry(root, width=50)
entry2.pack(padx=10, pady=10)

button1 = ttk.Button(text="Generate", command=generate)
button1.pack(padx=10, pady=10)

root.mainloop()
