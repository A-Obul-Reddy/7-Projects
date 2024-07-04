import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
from tkinter import filedialog as fd

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x400")
root.title("Youtube Video Downloader")


def download():
    try:
        browse.configure(state="disabled")
        download_btn.configure(state="disabled")
        ytlink = link.get()
        ytobj = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytobj.streams.get_highest_resolution()
        title.configure(text=ytobj.title)
        conclusion.configure(text="")
        percent.configure(text="0%")
        video.download(output_path=path.get() + "/")
        conclusion.configure(text="Download complete")
    except:
        conclusion.configure(text="Download failed")
    browse.configure(state="normal")
    directory.configure(text="selected directory ")
    link.set("")
    title.configure(text="Enter the youtube video link")


def set_path():
    path1 = fd.askdirectory()
    if path1:
        path.set(path1)
        directory.configure(text="select directory " + path1)
        percent.configure(text="")
        progressbar.set(0)
        download_btn.configure(state="normal")
        conclusion.configure(text="")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    per = str(int((bytes_downloaded / total_size) * 100))
    progressbar.set(float(per) / 100)
    percent.configure(text=per + "%")
    percent.update()


title = ctk.CTkLabel(root, text="Enter the youtube video link")
title.pack(padx=10, pady=10)

link = tk.StringVar()
link_entry = ctk.CTkEntry(root, width=400, height=5, textvariable=link)
link_entry.pack(padx=10, pady=10)

path = tk.StringVar()
directory = ctk.CTkLabel(root, text="selected directory ", width=400, height=1)
directory.pack(padx=10, pady=10)

browse = ctk.CTkButton(root, text="Browse", command=set_path)
browse.pack(padx=10, pady=10)

download_btn = ctk.CTkButton(root, text="Download", command=download, state="disabled")
download_btn.pack(padx=10, pady=10)

percent = ctk.CTkLabel(root, text="")
percent.pack(padx=10, pady=10)

progressbar = ctk.CTkProgressBar(root, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

conclusion = ctk.CTkLabel(root, text="")
conclusion.pack(padx=10, pady=10)

root.mainloop()
