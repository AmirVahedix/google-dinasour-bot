from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Cordinates():
    replyBtn = (480, 460)
    dino = (186, 492)#492  #24
    #220=x
    #y=524

def restartGame():
    pyautogui.click(Cordinates.replyBtn)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')


def imageGrab():
    box = (
        Cordinates.dino[0]+60, Cordinates.dino[1],
        Cordinates.dino[0]+155, Cordinates.dino[1]+6
    )
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab() != 787):
            pressSpace()
            time.sleep(0.01)

main()

