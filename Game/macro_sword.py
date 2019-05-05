# import pyobjc-core
import pyautogui as pag
import mss
import cv2
import numpy as np

# 마우스 클릭 후 대기시
# pag.PAUSE = 0.08

# bluestacks
# icon position
left_icon_pos = {'left': 100, 'top': 560, 'width': 70, 'height': 70}
right_icon_pos = {'left': 250, 'top': 560, 'width': 70, 'height': 70}

# button position
# 700 일수도
left_button = (70, 700)
right_button = (355, 700)


# rgb값 이용해서 이미지 판별
def compute_icon_type(img):
    mean = np.mean(img, axis=(0, 1))
    result = None

    if mean[0] > 50 and mean[0] < 55 and mean[1] > 50 and mean[1] < 55 and mean[2] > 50 and mean[2] < 55:
        result = 'BOMB'
    if mean[0] > 250 and mean[1] > 85 and mean[1] < 110 and mean[2] > 250:
        result = 'SWORD'
    if mean[0] > 100 and mean[0] < 130 and mean[1] > 150 and mean[1] < 200 and mean[2] > 90 and mean[2] < 110:
        result= 'POISON'
    if mean[0] > 210 and mean[0] < 230 and mean[1] > 200 and mean[1] < 225 and mean[2] > 120 and mean[2] < 135:
        result ='JEWEL'

    return result

def click(coords):
    # # 마우스 이동
    # pag.moveTo(x=coords[0], y=coords[1], duration=0.08)
    # # 키 누름
    # pag.mouseDown()
    # # 키 뗌
    # pag.mouseUp()
    pag.click(x=coords[0], y=coords[1], duration=0.02)
    # print('x: ' + str(coords[0]) + ' y: ' + str(coords[1]))


while True:
    # x, y = pag.position()
    # position_str = 'x: ' + str(x) + ' y: ' + str(y)
    # print(position_str)

    with mss.mss() as sct:
        left_img = np.array(sct.grab(left_icon_pos))[:, :, :3]
        right_img = np.array(sct.grab(right_icon_pos))[:, :, :3]

        # cv2.imshow('left_img', left_img)
        # cv2.imshow('right_img', right_img)
        # cv2.waitKey(0)

        left_icon = compute_icon_type(left_img)
        right_icon = compute_icon_type(right_img)

        if left_icon == 'SWORD' and (right_icon == 'BOMB' or right_icon == 'POISON'):
            print('LEFT')
            click(left_button)
        elif right_icon == 'SWORD' and (left_icon == 'BOMB' or left_icon == 'POISON'):
            print('RIGHT')
            click(right_button)
        elif left_icon == 'JEWEL' and right_icon == 'JEWEL':
            print('FEVER')
            click(left_button)
            click(right_button)
        else:
            a = 3

