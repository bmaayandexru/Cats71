from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка {e}")
        return None


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img

def exit():
    root.destroy()

root = Tk()
root.title("Cats")
root.geometry("600x480+400+400")

menu_bar = Menu(root)
root.config(menu = menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=set_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

#update_button = Button(text="Обновить", command= set_image)
#update_button.pack()

label = Label()
label.pack()


url = "https://cataas.com/cat"

set_image()

root.mainloop()
