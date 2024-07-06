import tkinter as tk
from tkinter import ttk
import sys, os


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("Drawing Pad")
root.geometry("1050x570+150+50")
root.config(bg="grey")
root.resizable(False, False)

current_x = 0
current_y = 0
current_color = 'black'


def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y


def addline(work):
    global current_x, current_y, current_color
    canvas.create_line((current_x, current_y, work.x, work.y),
                       width=get_current_value(), fill=current_color,
                       smooth=True, capstyle="round")
    current_x, current_y = work.x, work.y


def show_color(new_color):
    global current_color
    current_color = new_color


def new_canvas():
    canvas.delete('all')
    display_pallete()


image_icon = tk.PhotoImage(file=resource_path("logo.png"))
root.iconphoto(False, image_icon)

color_box = tk.PhotoImage(file=resource_path("color.png"))
l1 = tk.Label(root, image=color_box, bg="#f2f3f5")
l1.place(x=10, y=20)

eraser = tk.PhotoImage(file=resource_path("eraser.png"))
b1 = tk.Button(root, image=eraser, bg="#f2f3f5", command=new_canvas)
b1.place(x=20, y=400)

colors = tk.Canvas(root, bg="#fff", width=37, height=300, bd=0)
colors.place(x=15, y=50)


def display_pallete():
    id = colors.create_rectangle((10, 10, 30, 30), fill="black")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10, 40, 30, 60), fill="grey")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('grey'))

    id = colors.create_rectangle((10, 70, 30, 90), fill="red")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10, 100, 30, 120), fill="orange")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10, 130, 30, 150), fill="yellow")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((10, 160, 30, 180), fill="green")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10, 190, 30, 210), fill="blue")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10, 220, 30, 240), fill="purple")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

    id = colors.create_rectangle((10, 250, 30, 270), fill="brown4")
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))


display_pallete()

canvas = tk.Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addline)


def get_current_value():
    return f"{current_val.get():.2f}"


def slider_changed(event):
    value_label.configure(text=get_current_value())


current_val = tk.DoubleVar()
slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=slider_changed, variable=current_val)
slider.place(x=10, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

root.mainloop()
