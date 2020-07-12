import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry("640x480") # 가로 * 세로

# 기차 예매 시스템 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료")
    
def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")
    
def error():
    msgbox.showerror("에러", "결제 오류가 발생하였습니다.")
    
def okcancel(): # 선택지 제시
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
    
def retrycancel(): # 선택지 제시
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if response == 1: # 재시도
        print("재시도")
    elif response == 0: # 취소
        print("취소")

def yesno(): # 선택지 제시
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")
        
def yesnocancel(): # 선택지 제시
    response = msgbox.askyesnocancel(title=None, message="저장후 종료하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소 : 프로그램 종료 취소
    print("응답 : ", response) # True, False, None
    if response == 1: # 네
        print("예")
    elif response == 0: # 아니오
        print("아니오")
    else:
        print("취소")

Button(root, text="알림", command=info).pack()
Button(root, text="경고", command=warn).pack()
Button(root, text="에러", command=error).pack()

Button(root, text="확인 취소", command=okcancel).pack()
Button(root, text="재시도 취소", command=retrycancel).pack()
Button(root, text="예 아니오", command=yesno).pack()
Button(root, text="예 아니오 취소", command=yesnocancel).pack()

root.mainloop()