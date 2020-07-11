from tkinter import *

root = Tk()
root.title('Nado GUI')

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2222222222222222") # 텍스트 좌우, 위아래 여백 사이즈 조절
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4444444444444") # 버튼 자체 크기 조절
btn4.pack()

btn5 = Button(root, fg='red', bg='yellow', text="버튼5") # 버튼 자체 크기 조절
btn5.pack()

# 이미지로 버튼 만들기
photo = PhotoImage(file="D:/Google 드라이브/Programming/파이썬 무료 강의_활용편/2. GUI 프로그래밍/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")
    
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()