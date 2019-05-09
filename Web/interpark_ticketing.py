import pyautogui as pag

# 655, 295...예매 안내 취소
# 770, 635...예매 하기
# 330, 490...보안 문자 입력
# 520, 555...보안 문자 입력 완료
# 

# 터미널에서 넘어가는 과정 때문에 한번의 클릭 더 필요하다
pag.click(x=1080, y=735)
pag.click(x=1080, y=735)
pag.click(x=665, y=295, duration=0.5)
# pag.click(x=665, y=295)
pag.click(x=780, y=635)
pag.click(x=340, y=490)
# pag.click(x=530, y=555)
# 키 누름
# pag.mouseDown()
# 키 뗌
# pag.mouseUp()
# pag.click(x=770, y=635, duration=0.01)
# pag.click(x=770, y=635, duration=1)
# pag.click(x=330, y=490, duration=1)
# pag.click(x=520, y=555, duration=1)

# while True:
#     x, y = pag.position()
#     position_str = 'x: ' + str(x) + ' y: ' + str(y)
#     print(position_str)