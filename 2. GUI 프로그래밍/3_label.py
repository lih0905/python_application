from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="D:/Google 드라이브/Programming/파이썬 무료 강의_활용편/2. GUI 프로그래밍/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="D:/Google 드라이브/Programming/파이썬 무료 강의_활용편/2. GUI 프로그래밍/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()