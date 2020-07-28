import time
from PIL import ImageGrab

time.sleep(5) # 5초 대기 : 사용자가 준비하는 시간

for i in range(1,11): # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save(rf'D:\Google 드라이브\Programming\파이썬 무료 강의_활용편\2. GUI 프로그래밍\project\image{i}.png') # 파일로 저장
    time.sleep(2)


