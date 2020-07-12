from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry("640x480") # 가로 * 세로

listbox = Listbox(root, selectmode="extended", height=0) # height는 한번에 보여줄 갯수 (0 : 모두 보여줌)
#listbox = Listbox(root, selectmode="single", height=0) # 한번에 하나만 선택가능
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # 삭제
    #listbox.delete(END) # 리스트박스 마지막 옵션 삭제
    #listbox.delete(0) # 리스트박스 첫번째 옵션 삭제

    # 갯수 확인
    #print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    #print("첫번째부터 3번째까지의 항목 : ", listbox.get(0,2))
 
    # 선택된 항목 확인 (위치로 반환)
    print("선택된 항목 : ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()