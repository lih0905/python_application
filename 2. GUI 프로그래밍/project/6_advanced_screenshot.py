import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> curr_time = '_20200601_102030'
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save(rf'D:\Google 드라이브\Programming\파이썬 무료 강의_활용편\2. GUI 프로그래밍\project\image{curr_time}.png')

# 사용자가 F9 누르면 스크린샷 저장
keyboard.add_hotkey("F9", screenshot)
#keyboard.add_hotkey("ctrl+shift+s", screenshot) # 복합 할당

# ESC 누를 때까지 프로그램 수행
keyboard.wait('esc')