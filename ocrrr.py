from tkinter import filedialog
from tkinter import *
from gtts import gTTS 
import os
try:  
    from PIL import Image
except ImportError:  
    import Image
import pytesseract

root = Tk()
root.title("IMAGE TO TEXT CONVERTER")
root.geometry("400x300")

def browsefunc():
    global filename
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

    
def ocr_core():  
    img = Image.open(filename)
    img = img.convert('RGBA')  # Convert to RGBA to process transparency
    pix = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
                pix[x, y] = (0, 0, 0, 255)  # Set dark pixels to black
            else:
                pix[x, y] = (255, 255, 255, 255)  # Set light pixels to white

    img = img.convert('RGB')  # Convert to RGB before saving as JPEG
    img.save('temp.jpg')

    text = pytesseract.image_to_string(Image.open('temp.jpg'))
    language = 'en'
  
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save("/Users/indu/Desktop/wel.mp3")  
    os.system("/Users/indu/Desktop/wel.mp3")

    with open("textfile.txt", "w") as file1:
        file1.write(text)

    print(text)
    return text




l1=Label(root,text="Upload new File",font="Times 30")
pathlabel = Label(root)
b1 = Button(root, text="Browse",font="Times 20", command=browsefunc)
b2 = Button(root, text="Upload",font="Times 20", command=ocr_core)


l1.grid(row=0,column=0)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
pathlabel.grid(row=2,column=0)                     


root.mainloop()


  
