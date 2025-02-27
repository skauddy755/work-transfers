import tkinter as tk
from tkinter import ttk
from  PIL import Image, ImageTk
import os

root = tk.Tk()
root.geometry("720x500")
root.title("Display Images using Grid Function")


img_names = os.listdir(".\\data")
img_paths = [os.path.join(".\\data", img_name) for img_name in img_names]
imgs = [Image.open(img_path) for img_path in img_paths]



main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

second_frame = tk.Frame(my_canvas)

my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

NUM_COLUMS = 4
r, c = 0, 0

for img in imgs:
    pic = ImageTk.PhotoImage(img.resize((250, 250)))
    lb = tk.Label(second_frame, image = pic)
    lb.image = pic
    lb.grid(row = r, column = c)

    c += 1
    if c >= NUM_COLUMS:
        r += 1
        c = 0


root.mainloop()