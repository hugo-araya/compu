from tkinter import *
from PIL import Image, ImageChops, ImageEnhance, ImageOps

canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(10, 10, 80, 80)
canvas.create_line(10, 80, 80, 10)
canvas.create_oval(100, 10, 200, 110, width=2, fill='blue')
foto=Image.open('Nighthawks.jpg')
foto.show()
mainloop()
