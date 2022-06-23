from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# ------------ GUI ------------- #
window = Tk()
window.title('Watermarking App!')

# ------------Background------------- #
canvas = Canvas(height=200, width=1000)
canvas.grid(row=0, column=0)


# ------------ Functions -------------#
def open_watermark():
    global my_image
    filename = filedialog.askopenfilename(initialdir='/', title='Choose A File',
                                                 filetypes=(('png files', '*.png'), ('jpg files', '*.jpg')))
    watermark.set(filename)


def open_photo():
    global my_image
    filename = filedialog.askopenfilename(initialdir='/', title='Choose A File',
                                                 filetypes=(('png files', '*.png'), ('jpg files', '*.jpg')))
    photo.set(filename)


def create_watermark():
    watermark_open = watermark_entry.get()
    photo_open = photo_entry.get()
    save_name = save_name_entry.get()
    watermark = Image.open(watermark_open)
    photo = Image.open(photo_open)
    photo.paste(watermark, (0, 0), watermark)
    photo.save(f'{save_name}.png', "PNG")
    watermark_entry.delete(0, END)
    photo_entry.delete(0, END)
    save_name_entry.delete(0, END)


open_wtmrk = Button(window, text='Select Watermark', command=open_watermark).grid(row=1, column=1)
watermark = StringVar(None)
watermark_entry = Entry(window, textvariable=watermark, width=50)
watermark_entry.grid(row=1, column=0)


open_photo = Button(window, text='Select Photo', command=open_photo).grid(row=2, column=1)
photo = StringVar(None)
photo_entry = Entry(window, textvariable=photo, width=50)
photo_entry.grid(row=2, column=0)


create_watermarked = Button(window, text='Save Photo', command=create_watermark).grid(row=3, column=1)
save_name = StringVar(None)
save_name_entry = Entry(window, textvariable=save_name, width=50)
save_name_entry.grid(row=3, column=0)



window.mainloop()


