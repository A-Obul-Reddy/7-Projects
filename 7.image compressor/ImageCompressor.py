import tkinter as tk
from tkinter import ttk
from PIL import Image
from tkinter import filedialog as fd
import sys
import os


def relative_path(path):
    base_path = ""
    try:
        base_path = sys._MEIPASS
    except Exception as e:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)


root = tk.Tk()
root.title("Image Compressor")
root.geometry("500x350")
root.config(bg="grey")
img = tk.PhotoImage(file=relative_path("resolution.png"))
root.iconphoto(False, img)


def get_file():
    path = fd.askopenfilename()
    if path:
        file_path.set(path)
        l1.config(text="Selected file : " + path)


def get_path():
    path = fd.askdirectory()
    if path:
        save_path.set(path)
        l2.config(text="Destination : " + path + "/Compressed.png")


def compress():
    img = Image.open(file_path.get())
    width = int(w.get())
    height = int(h.get())
    img = img.resize((width, height))
    img.save(save_path.get() + "/compressed.png")
    l1.config(text="Select image file")
    l2.config(text="Select folder")
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)


l1 = ttk.Label(root, text="Select image file",
               background="grey", font=("Times New Roman", 10, "bold"), foreground="#0320ff")
l1.pack(padx=10, pady=10)

file_path = tk.StringVar()
b1 = ttk.Button(root, text="Browse", command=get_file)
b1.pack(padx=10, pady=10)

l2 = ttk.Label(root, text="Select folder",
               background="grey", font=("Times New Roman", 10, "bold"), foreground="#0320ff")
l2.pack(padx=10, pady=10)

save_path = tk.StringVar()
b2 = ttk.Button(root, text="Browse", command=get_path)
b2.pack(padx=10, pady=10)

l3 = ttk.Label(root, text=" Enter the required width and height respectively (only numbers like 128, 256, 512)",
               background="grey", font=("Times New Roman", 10, "bold"), foreground="#0320ff")
l3.pack(padx=10, pady=10)
w = tk.StringVar()
e1 = ttk.Entry(root, textvariable=w)
e1.pack(padx=10, pady=10)

h = tk.StringVar()
e2 = ttk.Entry(root, textvariable=h)
e2.pack(padx=10, pady=10)

b3 = ttk.Button(root, text="Compress", command=compress)
b3.pack(padx=10, pady=10)

root.mainloop()
