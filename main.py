import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller
from Button import Button

OPACITY = 0.6
RED = (0, 0, 255)
WINDOW_X = 50
WINDOW_Y = 50
SIZE = [75, 75]
SPACE = 5

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

detector = HandDetector(detectionCon=0.8)
keys = [["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["Q", "S", "D", "F", "G", "H", "J", "K", "L", "M"],
        ["W", "X", "C", "V", "B", "N", ",", ";", ":", "!"],
        [" "]
    ]

keyboard = Controller()
def drawAll(img, buttons):
    for button in buttons:
        button.draw(img)

buttons = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        if (key == " "): buttons.append(Button([130, WINDOW_Y+i*(SIZE[1] + SPACE)], key, [SIZE[0] * 8 + SPACE * 7, SIZE[1]]))
        else : buttons.append(Button([WINDOW_X+j*(SIZE[0] + SPACE), WINDOW_Y+i*(SIZE[1] + SPACE)], key, SIZE))

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList,bboxInfo = detector.findPosition(img)
    drawAll(img, buttons)

    if lmList:
        for button in buttons:
            x,y = button.pos
            w,h = button.size

            if x < lmList[8][0] < x +w and y <lmList[8][1]<y+h:
                button.focus()
                l,_,_ = detector.findDistance(8, 12, img)
                if (l<35):
                    button.setColor(RED)
                    keyboard.press(button.getText())
                    sleep(0.30)
            else:
                button.unfocus()

    cv2.imshow("Image", img)
    cv2.waitKey(1)