#screenshot py... takes a screen shot of a window and crops correct parts

import pyscreenshot as ImageGrab
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from treys import *


def screenshot(): #################
    print("taking screenshot")
    im = ImageGrab.grab(bbox=(2, 290, 920, 820)) # X1,Y1,X2,Y2  
    im.save('screenshot.png')

def allignment():
    screenshot()
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    print("player cards")
    playerCard1 = img[305:365, 425:480]
    plt.imshow(playerCard1)
    plt.show()

    print("flop card ")
    r2 = img[190:250, 395:445]
    plt.imshow(r2)
    plt.show()
    
def rt():
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    r5 = img[185:250, 540:590]
    plt.imshow(r5)
    plt.show()
    

def toGray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def extractCards():
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    
    directory = "cards/"                                    
    f1 = input("Enter Card 1 Filename : ")
    f2 = input("Enter Card 2 Filename : ")
    
    playerCard1 = img[310:360, 430:470]
    if f1 != "x":
        cv2.imwrite((directory+"/left/"+f1+".png"), playerCard1)
    
    playerCard2 = img[305:360, 470:510]
    if f2 != "x":
        cv2.imwrite((directory+"/right/"+f2+".png"), playerCard2)

def extractFlopCards():
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    directory = "cards/"
    f1 = input("Enter Flop 1 Filename: ")
    f2 = input("Enter Flop 2 Filename: ")
    f3 = input("Enter Flop 3 Filename: ")
    r1 = img[190:250, 350:390]
    r2 = img[190:250, 400:440]                                   
    r3 = img[190:250, 450:490]
    if f1 != "x":
        cv2.imwrite((directory+"/river/"+f1+".png"), r1)
    if f2 != "x":
        cv2.imwrite((directory+"/river/"+f2+".png"), r2)
    if f3 != "x":
        cv2.imwrite((directory+"/river/"+f3+".png"), r3)

def extractTurnCards():
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    directory = "cards/"
    f1 = input("Enter Turn Filename: ")
    r4 = img[190:245, 495:535]
    if f1 != "x":
        cv2.imwrite((directory+"/river/"+f1+".png"), r4)

def extractRiverCards():
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    directory = "cards/"
    f1 = input("Enter River Filename: ")
    r5 = img[188:245, 545:585]
    if f1 != "x":
        cv2.imwrite((directory+"/river/"+f1+".png"), r5)



    
    

def display():
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    #plt.imshow(img, cmap="gray")
    #plt.show()

    r4 = img[190:245, 495:535]
    plt.imshow(r4, cmap="gray")
    plt.show()

def getPlayerCards(): 
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    #cv2.imshow('ImageWindow', img)
    #cv2.waitKey()
    
    playerCard1 = img[305:365, 425:480]
    gray1 = cv2.cvtColor(playerCard1, cv2.COLOR_BGR2GRAY)
    
    playerCard2 = img[300:365, 465:515]
    gray2 = cv2.cvtColor(playerCard2, cv2.COLOR_BGR2GRAY)

    """
    plt.imshow(playerCard1)
    plt.show()
    plt.imshow(playerCard2)
    plt.show()
    """

    #cv2.imwrite("test_image2.png", playerCard2)

    detectedCard1 = detection(gray1.astype(np.uint8), "left")
    detectedCard2 = detection(gray2.astype(np.uint8), "right")

    print("Player Card 1: " + detectedCard1)
    print("Player Card 2: " + detectedCard2)

    return (detectedCard1, detectedCard2)

def getFlopCards():
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    # using bigger box boundary than extraction. 
    r1 = img[185:250, 345:395]
    r2 = img[185:250, 395:445]
    r3 = img[185:250, 445:495]
    d1 = detection(toGray(r1), "river")
    d2 = detection(toGray(r2), "river")
    d3 = detection(toGray(r3), "river")
    
    '''
    plt.imshow(r1)
    plt.show()
    plt.imshow(r3)
    plt.show()
    '''
    
    print("Flop Card 1: " + d1)
    print("Flop Card 2: " + d2)
    print("Flop Card 3: " + d3)
    return (d1,d2,d3)

def getTurnCards():
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    r4 = img[185:250, 490:540]
    d4 = detection(toGray(r4), "river")
    print("Turn Card: " + d4)
    return d4

def getRiverCards():
    img = cv2.imread('screenshot.png', cv2.IMREAD_UNCHANGED)
    r5 = img[185:250, 540:590]
    d5 = detection(toGray(r5), "river")
    print("River Card: " + d5)
    return d5

def getAllCards():
    getPlayerCards()
    getFlopCards()
    getTurnCards()
    getRiverCards()
    


def se():
    screenshot()
    extractCards()
    extractFlopCards()
    extractTurnCards()
    extractRiverCards()
    

def screenshot_and_run():
    screensho
    getPlayerCards()


def createBoard():
    # read current cards
    a,b,c = getFlopCards()
    d = getTurnCards()
    e = getRiverCards()
    
    # create flop only board...
    if d=="" and ("" not in [a,b,c]):
        board = [Card.new(a), Card.new(b), Card.new(c)]
        return board

    # create turn board
    elif d!= "" and e=="" and ("" not in [a,b,c]):
        board = [Card.new(a), Card.new(b), Card.new(c), Card.new(d)]
        return board
    elif ("" not in [a,b,c,d,e]):
        #create full board
        board = [Card.new(a), Card.new(b), Card.new(c), Card.new(d), Card.new(e)]
        return board
    else:
        # return empty board
        return []

def createHand():
    a,b = getPlayerCards()
    if "" not in [a,b]:
        hand = [Card.new(a), Card.new(b)]
        return hand
    else:
     return []


def evaluate():
    screenshot()
    board = createBoard()
    hand = createHand()
    if board and hand:
        evaluator = Evaluator()
        rank = evaluator.evaluate(hand, board)
        rank_class = evaluator.get_rank_class(rank)
        class_string = evaluator.class_to_string(rank_class)
        percentage = 1.0 - evaluator.get_five_card_rank_percentage(rank)  # higher better here
        print("hand = {}, percentage rank among all hands = {}".format(class_string, round(percentage,4)))    
    else:
        print("skipped evaluation... ")
        extract = (input("Do you want to extract data? y/n "))
        if extract == "y":
            se()
        
        
        

def example_evaluate():
    evaluator = Evaluator()
    board = [
        Card.new('3h'),
        Card.new('Kd'),
        Card.new('Jc'),
        Card.new('Qh'),
        Card.new('Qd')
    ]
    
    hand = [
        Card.new('Qs'),
        Card.new('Th')
    ]

    rank = evaluator.evaluate(hand, board)
    rank_class = evaluator.get_rank_class(rank)
    class_string = evaluator.class_to_string(rank_class)
    percentage = 1.0 - evaluator.get_five_card_rank_percentage(rank)  # higher better here
    print("hand = {}, percentage rank among all hands = {}".format(class_string, round(percentage,4)))
        
  

def detection(template, section):
    directory = os.fsencode("cards/"+section)
    for file in os.listdir(directory):
        filename = "cards/"+section+"/"+os.fsdecode(file)
        img_bgr = cv2.imread(filename).astype(np.uint8)
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.95
        loc = np.where(res >= threshold)
        detects = zip(*loc[::-1])

        for pt in zip(*loc[::-1]):
            if pt:
                card_name = filename.split('/')[-1].split('.')[0]
                return card_name
    return ""

def click():
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get("https://www.governorofpoker.com/games/governor-of-poker-3/play/")
    


if __name__ == "__main__":
    #screenshot()
    #openCV()
    #detection()
    print("Starting AI")
    while True:
        time.sleep(3)
        evaluate()
