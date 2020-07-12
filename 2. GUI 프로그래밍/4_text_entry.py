from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5) # 텍스트 입력이 가능한 박스 생성
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # 한줄로만 생성됨
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 첫번째 라인, 첫번째 컬럼부터 가져와라
    print(e.get())

    # 내용 삭제 
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()