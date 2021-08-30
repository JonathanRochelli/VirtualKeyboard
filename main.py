import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller
from Button import Button

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
        if (key == " "): buttons.append(Button([125, 50+i*80], key, [645, 75]))
        else : buttons.append(Button([50+j*80, 50+i*80], key, [75, 75]))

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
                    button.setColor((0,0,255))
                    keyboard.press(button.getText())
                    sleep(0.30)
            else:
                button.unfocus()

    cv2.imshow("Image", img)
    cv2.waitKey(1)