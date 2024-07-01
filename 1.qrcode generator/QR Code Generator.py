from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt
import qrcode as qr
import imageio.v2 as imageio

root = tk.Tk()
root.geometry("500x300")
root.title("QR Code Generator")
root.config(bg="#424242")


def new_entry():
    entry1.config(state="able")
    text_var.set("")
    button1.config(text="Generate", command=generate)


def generate():
    entry1.config(state="disable")
    button1.config(text="new Entry", command=new_entry)

    img = qr.make(data=text_var.get())
    img.save("qr.png")
    img2 = imageio.imread("qr.png")
    plt.imshow(img2)
    plt.axis("off")
    plt.show()


label1 = ttk.Label(root, text="Enter the Text or Link to create qr code",
                   font=("Times New Roman", 20),
                   background="#424242",
                   foreground="#05f72d")
label1.pack(padx=10, pady=30)

text_var = tk.Variable()
entry1 = ttk.Entry(textvariable=text_var, width=400, font=("Times New Roman", 16), foreground="#05aff7")
entry1.pack(padx=25, pady=10)

button1 = ttk.Button(root, text="Generate", command=generate)
button1.pack(pady=10)

root.mainloop()
