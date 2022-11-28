import PIL.Image
from skimage.io import imread, imsave, imshow
from PIL import ImageTk, Image
from tkinter import *
import matplotlib as plt
import copy


def display_image(window, placeholder):
    placeholder.insert(0, " ")
    color_image_dir=get_image_in_memory(window, placeholder)

    if(len(color_image_dir)<=5):
        color_image_dir="img/space.jpg"

    while (color_image_dir[0] == ' '):
        color_image_dir=color_image_dir[1:]

    print(color_image_dir)


    image_to_display = PIL.Image.open(str(color_image_dir))
    color_img_label=create_label(window, image_to_display)

    color_img_label.place(x=50, y=50)


def get_image_in_memory(window, placeholder):
    file_path = placeholder.get()

    return file_path


def create_bg_label(window, image):
    image = image.resize((800, 410))
    image = ImageTk.PhotoImage(image)

    label = Label(window)
    label.image = image
    label["image"] = label.image

    return label


def create_label(window, image):
    image=image.resize((300, 300))
    image=ImageTk.PhotoImage(image)



    label = Label(window)
    label.image = image
    label["image"] = label.image

    return label


def make_black(window, placeholder, save_name):
    placeholder.insert(0, " ")
    color_image_dir = get_image_in_memory(window, placeholder)

    print(color_image_dir)

    if (len(color_image_dir) <= 5):
        color_image_dir = "img/space.jpg"

    while(color_image_dir[0]==' '):
        color_image_dir=color_image_dir[1:]


    image_to_display = imread(color_image_dir)
    for row in image_to_display:
        for i in row:
            sum=0
            sum+=i[0]
            sum+=i[1]
            sum+=i[2]
            sum=sum/3+1
            i[0]=sum
            i[1]=sum
            i[2]=sum



    image_to_display=PIL.Image.fromarray(image_to_display)
    image_to_save=image_to_display.save("img/"+save_name.get())

    black_label=create_label(window, image_to_display)
    black_label.place(x=450, y=50)


def show_info():
    info = Tk()                                       #
    info.resizable(0, 0)                              #
    info.title("Інструкція")                          # Створення вікна
    info.iconbitmap("img/icon.ico")                   #

    info_canvas = Canvas(info, width=600, height=300)      # Створення полотна
    info_canvas.pack()                                     #

    f=open("img/info.txt", "r")


    text_label=Label(info, text=f.read(),  justify="left")
    text_label.place(x=0, y=0)

    info.mainloop()










def create_window():
    image_to_save=None

    window=Tk()                                                                #
    window.resizable(0, 0)                                                     #
    window.title("Фото в чорно-біле")                                          #Створення вікна
    window.iconbitmap("img/icon.ico")                                          #

    canvas = Canvas(window, width=800, height=410)                             #Створення полотна
    canvas.pack()                                                              #



    background_img_color=PIL.Image.open("img/Background.jpg")                  #Підключення файлів(зробити динамічно)
    background_img_black = PIL.Image.open("img/Background.jpg")                #
    window_bg_image=PIL.Image.open("img/win_bg.jpg")

    window_bg_image_label = create_bg_label(window, window_bg_image)
    color_img_label=create_label(window, background_img_color)                 #Створення нової лейби для кожної картинки
    black_img_label=create_label(window, background_img_black)                 #


    window_bg_image_label.place(x=0, y=0)
    color_img_label.place(x=50, y=50)                                          #Поставити лейбу на полотно
    black_img_label.place(x=450, y=50)                                         #


    placeholder = Entry(window, width=61)  #
    placeholder.place(x=200, y=375)  #

    save_name = Entry(window, width=20)  #
    save_name.insert(0, "Зберегти як")  #
    save_name.place(x=630, y=375)  #


    convert_button=Button(window, text="-->", command=lambda: make_black(window, placeholder, save_name))       #
    convert_button.pack()                                                                                       #
    convert_button.place(x=387, y=185)                                                                          #

    select_file_button = Button(window, text="Обрати вказаний файл", command=lambda: display_image(window, placeholder))            #
    select_file_button.pack()                                                                                                       #
    select_file_button.place(x=50, y=370)                                                                                           #

    select_file_button = Button(window, text="Як користуватись?", command=lambda: show_info())        #
    select_file_button.pack()                                                                       #
    select_file_button.place(x=0, y=0)                                                              #

    return window



win=create_window()

win.mainloop()
