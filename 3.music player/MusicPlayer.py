import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import pygame
import os

root = tk.Tk()
root.geometry("500x300")
root.title("Music Player")
root.config(bg="#4a4a4a")
pygame.mixer.init()
n = 0


def start_song():
    print(songs_box.get())
    print("start song")
    global n
    n += 1
    if n == 1:
        song = songs_box.get()
        pygame.mixer.music.load(path.get() + "/" + song)
        print(path.get() + "/" + song)
        pygame.mixer.music.play(0)
        button2.config(text="pause")
    elif n % 2 == 0:
        pygame.mixer.music.pause()
        button2.config(text="play")
    elif n % 2 == 1:
        pygame.mixer.music.unpause()
        button2.config(text="pause")


def set_to_one(x, y, z):
    global n
    print(x, y, z)
    n = 0
    button2.config(text="play")


def directory():
    global n, menu
    n = 0
    path.set(fd.askdirectory())
    if path.get():
        menu.destroy()
        label1.config(text="Select directory : " + path.get())
        lst = os.listdir(path.get())
        songs_box.set(lst[0])
        menu = ttk.OptionMenu(root, songs_box, *lst)
        menu.pack(padx=10, pady=10)
        print(lst)
        print("directory")


label1 = ttk.Label(root, text="Select directory ", background="#4a4a4a", font=("Times New Roman", 20))
label1.pack(padx=10, pady=30)

button1 = tk.Button(root, text="Browse", command=directory,
                    background="#05ff2b", foreground="#f52727",
                    activebackground="#f52727", activeforeground="#05ff2b", width= 50)
button1.pack(padx=10, pady=10)

button2 = tk.Button(root, text="play", command=start_song,
                    background="#05ff2b", foreground="#f52727",
                    activebackground="#f52727", activeforeground="#05ff2b",
                    width=50)
button2.pack(padx=10, pady=10)

path = tk.StringVar(root)
path.set("/")

songs = os.listdir(path.get())
songs_box = tk.StringVar(root)
songs_box.set("select songs")
menu = ttk.OptionMenu(root, songs_box, *songs)
menu.pack(padx=10, pady=10)
songs_box.trace("w", set_to_one)

root.mainloop()
