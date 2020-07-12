import tkinter.ttk as ttk # 콤보박스는 여기 있음
from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry("640x480") # 가로 * 세로

values = [str(i)+"일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values) # height는 한번에 보여지는 리스트 수
combobox.set("카드 결제일") # 최초 목록 제목 설정 (실제 콤보 박스 리스트 값 설정도 가능)
combobox.pack()

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 값을 수정할 수 없음
readonly_combobox.current(0)  # 0번째 인덱스 값 선택 
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 표시 


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()