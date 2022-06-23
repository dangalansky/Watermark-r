from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

# ------------ GUI ------------- #
window = Tk()
window.title('Watermarking App!')
window.config(padx=50, pady=50)

# ------------Background------------- #
canvas = Canvas(height=200, width=50)
canvas.grid(row=0, column=3)

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
    messagebox.showinfo(title='Success!', message='Watermarked Image Has Been Created and Saved!')



watermark_label = Label(text='Watermark: ')
watermark_label.grid(row=1, column=0)
watermark = StringVar(None)
watermark_entry = Entry(window, textvariable=watermark, width=30)
watermark_entry.grid(row=1, column=1, pady=10)
open_wtmrk = Button(window, text='Select File', command=open_watermark).grid(row=1, column=2)



photo_label = Label(text='        Photo: ')
photo_label.grid(row=2, column=0)
photo = StringVar(None)
photo_entry = Entry(window, textvariable=photo, width=30)
photo_entry.grid(row=2, column=1, pady=10)
open_photo = Button(window, text='Select File', command=open_photo).grid(row=2, column=2)


save_label = Label(text='Save Photo As:        ')
save_label.grid(row=3, column=0)
save_name = StringVar(None)
save_name_entry = Entry(window, textvariable=save_name, width=30)
save_name_entry.grid(row=3, column=1, pady=10)
create_watermarked = Button(window, text='Save', command=create_watermark).grid(row=3, column=2)



window.mainloop()


