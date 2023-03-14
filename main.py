import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageFont
from PIL import ImageDraw

window = Tk()
window.title("Watermarking")
window.config(padx=10, pady=10)
window.minsize(width=800, height=600)
l1 = tk.Label(window, text='Add Student Data with Photo', width=30, font=('times', 18, 'bold'))
l1.grid(row=1, column=1)
b1 = tk.Button(window, text='Upload File',
    width=20, command=lambda:upload())
b1.grid(row=2, column=1)


def upload():
        global img
        f_types = [('Jpg Files', '*.jpg'),  ("all files", "*.*")]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = Image.open(filename)
        img_resized = img.resize((400, 200)) # new width & height
        draw = ImageDraw.Draw(img)

        # Creating text and font object
        text = "HolyPython.com"
        font = ImageFont.truetype('arial.ttf', 82)

        # Positioning Text
        textwidth, textheight = draw.textsize(text, font)
        width, height = img.size
        x = width / 2 - textwidth / 2
        y = height - textheight - 300

        # Applying text on image via draw object
        draw.text((x, y), text, font=font)

        # Saving the new image
        img.save('watermarked.png')

window.mainloop()
