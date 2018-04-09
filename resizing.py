from tkinter import filedialog
from tkinter import Button,Tk,Entry,Label
from os import getcwd,mkdir
from PIL import Image

root = Tk()
root.geometry('290x90')
root.resizable(False, False)

def open_files():
    """ функция открытия файлов """
    global files
    files = filedialog.askopenfilenames(initialdir="E:\Study\Programming\Python-study\size change\output", title="Select files", filetypes = [("Image Files", ("*.jpg", "*.gif",'*png','*.jpeg'))])
    return files

Label(root,text='Width').place(x=40, y=0)
Label(root,text='Height').place(x=210, y=0)

width_text = Entry(root)
width_text.place(x=0, y=30)
height_text = Entry(root)
height_text.place(x=165, y=30)



w = Button(root,font='Arial 10', text='Открыть файлы',command=open_files).place(x = 0, y = 53)

def resize_image(input_image_path,
                 output_image_path,
                 size):
    """ функция смены размера файлов """

    original_image = Image.open(input_image_path)
    width, height = original_image.size

    resized_image = original_image.resize(size)
    width, height = resized_image.size

    resized_image.save(output_image_path)


def resize_all():
    directory_output = getcwd() + '/output'
    try:
        output = mkdir(directory_output)
    except FileExistsError:
        pass
    for i in range(len(files)):
        a = files[i].split('/')
        width = int(width_text.get())
        height = int(height_text.get())
        if __name__ == '__main__':
            resize_image(input_image_path=files[i],
                         output_image_path=directory_output+"/"+a[-1],
                         size=(width, height))


resize = Button(root,font='Arial 10', text='Изменить размер',command=resize_all).place(x = 175, y = 53)


root.mainloop()