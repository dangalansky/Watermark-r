from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox
import cv2

# ------------ GUI ------------- #
window = Tk()
window.title('Watermark\'R!')
window.geometry('625x625')

# ------------Background------------- #
canvas = Canvas(height=625, width=625, bg='black', highlightthickness=0)
background = Image.open('Watermarker App.png')
background_sm = background.resize((740, 675), Image.ANTIALIAS)
watermarker_app = ImageTk.PhotoImage(background_sm)
canvas.create_image(280, 310, image=watermarker_app)
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
    # recieve entry data
    wm_filepath = watermark_entry.get()
    photo_filepath = photo_entry.get()
    save_name = save_name_entry.get()

    # read photo files
    photo = cv2.imread(photo_filepath)
    watermark = cv2.imread(wm_filepath)
    # option to scale down watermark by 50% if larger than photo
    if if_scale.get() == 1:
        watermark = cv2.resize(watermark, (0, 0), watermark, 0.5, 0.5)

    # define region of interest (ROI), default == lower right corner
    wm_rows, wm_cols, wm_channels = watermark.shape
    ph_rows, ph_cols, ph_channels = photo.shape

    if orientation.get() == 2:
        x_offset = ph_cols - wm_cols
        y_offset = ph_rows - wm_rows
        roi = photo[y_offset: ph_rows, x_offset: ph_cols]

    elif orientation.get() == 1:
        x_offset = 0
        y_offset = 0
        roi = photo[y_offset: y_offset + wm_rows, x_offset: x_offset + wm_cols]

    # create a mask from watermark
    img2gray = cv2.cvtColor(watermark, cv2.COLOR_RGB2GRAY)
    mask_inv = cv2.bitwise_not(img2gray)
    fg = cv2.bitwise_or(watermark, watermark, mask=mask_inv)

    # final ROI format and place on top of photo using overlay technique
    final_roi = cv2.bitwise_or(roi, fg)
    watermark = final_roi
    photo[y_offset: (y_offset + wm_rows), x_offset: (x_offset + wm_cols)] = watermark

    # save watermarked photo, reset entry fields to empty
    cv2.imwrite(f"{save_name}.png", photo)
    watermark_entry.delete(0, END)
    photo_entry.delete(0, END)
    save_name_entry.delete(0, END)
    messagebox.showinfo(title='Success!', message='Watermarked Image Has Been Created and Saved!')


# Find and Open Watermark File
watermark = StringVar(None)
watermark_entry = Entry(window, textvariable=watermark, width=30, highlightthickness=0)
watermark_entry.place(x=170, y=415)
open_wtmrk = Button(window, text='Select', highlightthickness=0, borderwidth=0, highlightbackground='#FFE964',
                    command=open_watermark).place(x=275, y=440)

# Option to Scale Down Watermark 50%
if_scale = IntVar()
scale_down = Checkbutton(text="Scale Down 50%", variable=if_scale, bg="black", fg="#ED031A")
scale_down.place(x=480, y=415)

# Option to watermark position to upper left
orientation = IntVar()
upper_left = Radiobutton(text="Upper Left", value=1, variable=orientation, bg="black", fg="#ED031A")
lower_right = Radiobutton(text="Lower Right", value=2, variable=orientation, bg="black", fg="#ED031A")
upper_left.place(x=15, y=415)
lower_right.place(x=15, y=435)

# Find and Open Photo File
photo = StringVar(None)
photo_entry = Entry(window, textvariable=photo, width=30, highlightthickness=0)
photo_entry.place(x=170, y=490)
open_photo = Button(window, text='Select', highlightthickness=0, borderwidth=0, highlightbackground='#FFE964',
                    command=open_photo).place(x=275, y=515)

# Save Watermarked File as .png
save_name = StringVar(None)
save_name_entry = Entry(window, textvariable=save_name, width=30, highlightthickness=0)
save_name_entry.place(x=170, y=565)
create_watermarked = Button(window, text='Save', highlightthickness=2, borderwidth=0, highlightbackground='#FFE964',
                            command=create_watermark).place(x=277, y=590)

window.mainloop()
