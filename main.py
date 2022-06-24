from tkinter import *
# from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

# ------------ GUI ------------- #
window = Tk()
window.title('Watermark\'R!')
window.config()
window.geometry('625x625')
# style = Style()
# style.configure('Button', background = '#FFE964')
# ------------Background------------- #
canvas = Canvas(height=625, width=625, bg='black', highlightthickness=0)
background = Image.open('Watermarker App.png')
background_sm = background.resize((740, 675), Image.ANTIALIAS)
watermarker_app = ImageTk.PhotoImage(background_sm)

canvas.create_image(280,310, image=watermarker_app)
canvas.place(x=0, y=0)

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




watermark = StringVar(None)
watermark_entry = Entry(window, textvariable=watermark, width=30, highlightthickness=0)
watermark_entry.place(x=170, y=415)
open_wtmrk = Button(window, text='Select', highlightthickness=0, borderwidth=0, highlightbackground='#FFE964', command=open_watermark).place(x=275, y=440)




photo = StringVar(None)
photo_entry = Entry(window, textvariable=photo, width=30, highlightthickness=0)
photo_entry.place(x=170, y=490)
open_photo = Button(window, text='Select', highlightthickness=0, borderwidth=0, highlightbackground='#FFE964', command=open_photo).place(x=275, y=515)



save_name = StringVar(None)
save_name_entry = Entry(window, textvariable=save_name, width=30, highlightthickness=0)
save_name_entry.place(x=170, y=565)
create_watermarked = Button(window, text='Save', highlightthickness=2, borderwidth=0, highlightbackground='#FFE964', command=create_watermark).place(x=277, y=590)


window.mainloop()
