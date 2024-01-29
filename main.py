from tkinter import *
from PIL import Image
from tkinter import filedialog

global img
app = Tk()
app.title("PNG Converter")
app.resizable(False, False)
canvas = Canvas(app, bg="cyan" ,width=500)
canvas.pack(fill=BOTH, expand=1)

mainFrame = Frame(app, bg="cyan")
container = Frame(mainFrame, bg="cyan")
container.grid_columnconfigure(0, weight=int(500 / 3))
container.grid_columnconfigure(1, weight=int(500 / 3))
container.grid_columnconfigure(2, weight=int(500 / 3))

title = Label(container, text="PNG Converter To Jpg", font=("Arial", 30, "bold"), bg="cyan", fg="white", justify=CENTER)
title.grid(row=0, column=1, pady=15)


def get_image():
    global img
    get_img = filedialog.askopenfilename()
    img = Image.open(get_img)


btn = Button(container, text="Select PNG Image", font=("Arial", 20, "bold"), bg="skyblue", fg="white", justify=CENTER, command=get_image)
btn.grid(row=1, column=1, pady=5)


def save_image():
    global img
    pathFile = filedialog.asksaveasfilename(defaultextension="jpg")
    img.save(pathFile)


btn1 = Button(container, text="Convert", font=("Arial", 20, "bold"), bg="green", fg="white", justify=CENTER, command=save_image)
btn1.grid(row=2, column=1, pady=5)
container.pack(fill=BOTH, expand=1)


def fix_size(event):
    canvas.create_window((0, 0), window=mainFrame, width=500, height=app.winfo_height(), anchor=NW)


app.bind("<Configure>", fix_size)

app.mainloop()
