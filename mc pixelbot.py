#notes for later: make gradient lighter in the cetner, darker in the outside. Make tolerance by subtracting tempIm[0,0] from 255, 0, 0 to find the difference, then check if it is < certain number to make a tolerance function
#then I will make the screenshot 50x50, and check the pixels to all directions from it and move to the lightest one, repeating each time it finished moving. It only aimbots if the color is dark enough
#the darkness determines how many pixels it moves at 1 time

#imports
import PIL
from PIL import ImageGrab
from pyautogui import *
import mouse
import time
import random
import win32api
import keyboard
import numpy as np
#variables and other thingies
#this stuff gets your screen resolution, and adapts the thing to target the center of any screen
screenW = win32api.GetSystemMetrics(0)
screenH = win32api.GetSystemMetrics(1)
centerX = screenW / 2
centerY = screenH / 2
#toggling variables
aimbot = False
triggerbot = False
scriptToggle = False
myImage = ImageGrab.grab(bbox=(centerX - 50, centerY - 50, centerX + 50, centerY + 50))
tempIm = myImage.load()

#code and other more different thingies

def checkCenterPxColor():
  if scriptToggle == True:
    #self explanatory, it checks pixel color.
    #print("Screen Center Color " + str(tempIm[0,0]))
    #if the pixel is red it triggers the triggerbot and triggers the aim. Its only checking for red here, because i only want red to trigger for anticheat reasons, so ill make green trigger the triggerbot later
    if tempIm[50, 50][0] > 0 and tempIm[0,0][1] == 0 and tempIm[0,0][2] == 0:
      if triggerbot == True:
        mouse.click(button='left')
    #this individually looks at every pixel on ur screen
def aim():
  posX = 0
  posY = 0
  lightestRed = 0
  
  if aimbot == True:
    print("searching...")
    for i in range(0, 100, 1):
      for j in range(0, 100, 1):
        #if the pixel is the brightest one seen yet it will make that the new brighest pixel
        if tempIm[i, j][0] > lightestRed and tempIm[i, j][1] == 0 and tempIm[i, j][2] == 0:
          lightestRed = tempIm[i, j][0]
          posX = i
          posY = j
    if posX != 0 or posY != 0:
      print("aiming...")
      (mouseX, mouseY) = mouse.get_position()
      mouse.move(mouseX + posX - 50, mouseY + posY - 50)

while True:
  myImage = ImageGrab.grab(bbox=(centerX - 50, centerY - 50, centerX + 50, centerY + 50))
  tempIm = myImage.load()
  checkCenterPxColor()
  aim()
  if keyboard.is_pressed('l'):
    scriptToggle = not scriptToggle
    print("script toggled to " + str(scriptToggle))
    sleep(0.1)
  if keyboard.is_pressed('t'):
    triggerbot = not triggerbot
    print("triggerbot toggled to " + str(triggerbot))
    sleep(0.1)
  if keyboard.is_pressed('p'):
    aimbot = not aimbot
    print("aimbot toggled to " + str(aimbot))
    sleep(0.1)
