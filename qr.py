#qr.py

from tkinter import *
import qrcode

main = Tk()
main.title("Qr Generator")
main.geometry("1000x500")
main.resizable(False,False)

def gen():
    name = title.get()
    text = box.get()
    qr = qrcode.make(text)
    qr.save("Qrcode/"+str(name)+".png")

    global Image
    Image = PhotoImage(file="Qrcode/"+str(name)+".png")
    Image_view.config(image=Image)


Image_view = Label(master=main)
Image_view.pack(padx=50,pady=5,side=RIGHT)

lb = Label(master=main,text="Title",font="arial 20").place(x=50,y=170)
title = Entry(master=main,width=13,font="arial 15")
title.place(x=50,y=220)

box = Entry(master=main,width=28,font="arial 15")
box.place(x=50,y=260)

button = Button(master=main,text="Generate",width=15,height=1,font=5,command=gen)
button.place(x=50,y=300)

main.mainloop()
