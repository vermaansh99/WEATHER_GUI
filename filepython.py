from tkinter import *
from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root, width=200, height=200, bd=0,
                highlightthickness=0)
canvas.pack()

mask = PhotoImage(width=200, height=200)
cx,cy = 100,100 # image & circle center point
r = 100         # circle radius
r_squared = r*r
for y in range(200):
    for x in range(200):
        # using the formula for a circle:
        # (x - h)^2 + (y - k)^2 = r^2
        # any pixel outside our circle gets filled
        if (x - cx)**2 + (y - cy)**2 > r_squared:
            mask.put('blue', (x,y))

canvas.create_image(100,100, image=mask, anchor='c')

myimage = Image.open('userPic/cropped.jpg')
item = canvas.create_image(100,100, image=myimage, anchor='c')
canvas.lower(item)

root.mainloop()