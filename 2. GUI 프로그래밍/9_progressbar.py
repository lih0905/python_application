import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry("640x480") # 가로 * 세로

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 바가 좌우로 움직임
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 바가 처음부터 올라감
progressbar.start(10) # 10ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # 작동 중지

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)  # length=길이
progressbar2.pack()

def btncmd():
    for i in range(1,101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progress bar 값 설정
        progressbar2.update() # 매번 업데이트 
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd)
btn.pack()

root.mainloop()