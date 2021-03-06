#IMPORT MODULES
import pygame
import random
import math



#INITIALISE PYGAME 
pygame.init()
#Enusre font has init correctly
if(pygame.font.init()) == 0:
    print("Error the font module hasn't initialsied properly.")


    
#DECODE MAPS
#!---------------------------------Map Layout-------------------------------------!
#Table used to create the level,where
##W = wall with grass
##B = plain wall
##1 = player 1 spawn point
##2 = player 2 spawn point
    
level1 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                                                                  W",
"W                                                                                  W",
"W      1                                                                           W",
"W                                                         2             WWW        W",
"W    WWWWWW                                                             BBB        W",
"W    BBBBBB                                                                        W",
"W                        WWWWWWWWWWWWWWWWWWWW           WWWWWWW                    W",
"W             WWWW                                                                 W",
"W                                                                              WWWWW",
"W                                                                              BBBBW",
"W                                                                                  W",
"W    WWWWWW                                                                        W",
"W                                                       WWWWWWWWWWWWWWW            W",
"W                                                       BBBBBBBBBBBBBBB            W",
"W                    WWWWWWWWWWWWWWWWWWWWWW             BBBBBBBBBBBBBBB            W",
"W                                                                                  W",
"W   WWWWWWWWWWW                                                                    W",
"W                                                                                  W",
"W                                                                      WWWWWWWWWWWWW",
"W                                                                                  W",
"W                        WWWWWWWWWWWWW                                             W",
"W                        BBBBBBBBBBBBB                                             W",
"W                                                WWWWWWWWWWWWWWWWWWWW              W",
"W                                                                                  W",
"W           WWWWWW                                                                 W",
"W           BBBBBB                                                                 W",
"W                                                                                  W",
"W                                                                                  W",
"W                             WWWWWWWWWWWWWWWWWWWWWW            WWWWWWWWWWWWWWWWWWWW",
"W                                                               BBBBBBBBBBBBBBBBBBBW",
"W                                                                                  W",
"W    WWWWWWWWWWWWWWWW                                                              W",
"W                                                WWWWWWWWWWWW                      W",
"W                                                                                  W",
"W                                                                                  W",
"W                             WWWWWWWWWWWW                                         W",
"W                                                    WWWWWW                        W",
"W    WWWWWWWWWWWW                                    BBBBBBWWWWWWWWWWW             W",
"W                     WWW                                                          W",
"W                                                                                  W",
"W                                                                                  W",
"W                           WWWWWWWWWWWWWW                             WWWWW       W",
"W                                                w                                 W",
"W            WWWWWWWW                                         WWWWWW               W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W    WWWWWWWWW    WWWWWWWWWWWWWWWWWWWW    WWWWWWWW        WWWWWWW                WWW",
"W    BBBBBBBBB    BBBBBBBBBBBBBBBBBBBB    BBBBBBBB                                 W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

level2 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                                                            W",
"W                                                                            W",
"W      1                                                 2                   W",
"W                                                                            W",
"WWWWWWWWWWWWW            WWWW        WWWWWWWWWWWWWWWWWWWWWWWW                W",
"WBBBBBBBBBBBB            BBBB        BBBBBBBBBBBBBBBBBBBBBBBB                W",
"WBBBBBBBBBBBB            BBBB        BBBBBBBBBBBBBBBBBBBBBBBB                W",
"WBBBBBBBBBBBB            BBBB        BBBBBBBBBBBBBBBBBBBBBBBB                W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"W            WWWWWWWWWWWWWWWW                       WWWWWWWWWWWWWWWWWWWWW    W",
"W            BBBBBBBBBBBBBBBB                       BBBBBBBBBBBBBBBBBBBBB    W",
"W            BBBBBBBBBBBBBBBB                       BBBBBBBBBBBBBBBBBBBBB    W",
"W            BBBBBBBBBBBBBBBB                       BBBBBBBBBBBBBBBBBBBBB    W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"WWWWW                WWWWWWWWWWWW    WWWWWWWWWWWWWWWWWWWW            WWWWWWWWW",
"WBBBB                BBBBBBBBBBBB    BBBBBBBBBBBBBBBBBBBB            BBBBBBBBW",
"WBBBB                BBBBBBBBBBBB    BBBBBBBBBBBBBBBBBBBB            BBBBBBBBW",
"WBBBB                BBBBBBBBBBBB    BBBBBBBBBBBBBBBBBBBB            BBBBBBBBW",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"W    WWWWWWWWWWWWWWWW            WWWWWWWWWWWW                WWWWWWWWWWWW    W",
"W    BBBBBBBBBBBBBBBB            BBBBBBBBBBBB                BBBBBBBBBBBB    W",
"W    BBBBBBBBBBBBBBBB            BBBBBBBBBBBB                BBBBBBBBBBBB    W",
"W    BBBBBBBBBBBBBBBB            BBBBBBBBBBBB                BBBBBBBBBBBB    W",
"W        BBBB                                                                W",
"W        BBBB                                                                W",
"W        BBBB                                                                W",
"W        BBBB                                                                W",
"W    WWWWBBBBWWWWWWWWWWWWWWWW    WWWWWWWWWWWWWWWW            WWWW            W",
"W    BBBBBBBBBBBBBBBBBBBBBBBB    BBBBBBBBBBBBBBBB            BBBB            W",
"W    BBBBBBBBBBBBBBBBBBBBBBBB    BBBBBBBBBBBBBBBB            BBBB            W",
"W    BBBBBBBBBBBBBBBBBBBBBBBB    BBBBBBBBBBBBBBBB            BBBB            W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"W                                                                            W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

level3 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W                  1                                      2                        W",
"W    WWWW                                                                          W",
"W    BBBB                                                                          W",
"W                        WWWWWWWWWWWWWWWWWWWW           WWWWWWW                    W",
"W             WWWW                                                                 W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W    WWWWWW                                                                        W",
"W                                                       WWWWWWWWWWWWWWW            W",
"W                                                       BBBBBBBBBBBBBBB            W",
"W                    WWWWWWWWWWWWWWWWWWWWWW             BBBBBBBBBBBBBBB            W",
"W                                                                                  W",
"W   WWWWWWWWWWW                                                                    W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W                        WWWWWWWWWWWWW                                             W",
"W                        BBBBBBBBBBBBB                                             W",
"W                                                WWWWWWWWWWWWWWWWWWWW              W",
"W                                                                                  W",
"W           WW                                                                     W",
"W           BB                                                                     W",
"W                                                                                  W",
"W                                                                                  W",
"W                             WWWWWWWWWWWWWWWWWWWWWW            WWWWWWWWWWWWWWWWWWWW",
"W                                                               BBBBBBBBBBBBBBBBBBBW",
"W                                                                                  W",
"W    WWWWWWWWWWWWWWWW                                                              W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                    WWWWWW                        W",
"W    WWWWWWWWWWWW                                    BBBBBBWWWWWWWWWWWW            W",
"W    BBBBBBBBBBBB                     w                      BBBBBBBBBB            W",
"W    BBBB                                                                          W",
"W    BBBB                                                                          W",
"W    BBBB                   WWWWWWWWWWWWWW                                         W",
"W    BBBB                                                                          W",
"W                                                                                  W",
"W                                                                         WWWWW    W",
"W                                                                         BBBBB    W",
"W                                                                         BBBBB    W",
"W    WWWWWWWWW    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                        BBBBB    W",
"W    BBBBBBBBB    BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB                                 W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

#Put all maps into mapList
mapList = [level1,level2,level3]
#number of pixels each leter takes up on the screen
gameBlockSize = 16



#INITALISE DISPLAY
#room width and height for menus
roomWidthStart = 800
roomHeightStart = 800

#CHECK IF NEEDED BUT LIKELY NEEDED TO ITITALISE-----------------------------------------!
roomWidth = 800
roomHeight = 600
roomWidthHalf = roomWidth/2
roomHeightHalf = roomHeight/2

#Also check this
tempRoomHeight = 0

#Set up display
gameName = "TAG"
gameDisplay = pygame.display.set_mode((roomWidth,roomHeight))
pygame.display.set_caption(gameName)


#INITALISE CLOCK
clock = pygame.time.Clock()
#Frames per seccond
FPS = 30           

#Initalise globals
state = "choose tagger"
#state = "game title"
                  
#ASSIGN GLOBALS

false = 0
true = 1

#SCORING
score = [0,0]           #First int is player x score seccond int is player y score

#ASSIGN COLOURS
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)

#ASSIGN FONTS
basic = "freesansbold.ttf"

#DEFINE KEYS
#keyList = [keyLeft,keyRight,keyUp,keyDown,keyDot,keyForwardSlash,keyQ,keyE,keyW,keyA,keyS,keyD]
#keyList = [keyLeft- 0,keyRight - 1,keyUp - 2,keyDown - 3,keyDot - 4,keyForwardSlash 5 ,keyQ - 6,keyE - 7,keyW - 8,keyA - 9,keyS - 10,keyD -11]
keyList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] 

#Plyer Two
keyLeft = false
keyRight = false
keyUp = false
keyDown = false
keyDot = false
keyForwardSlash = false

#Player one
keyQ = false
keyE = false
keyW = false
keyA = false
kayS = false
keyD = false

#Numbers
keyListNumbers = [0,0,0,0,0,0,0,0,0,0]
#keyListNumbers = [key0,Key1,key2,key3,key4,key5,key6,key7,key8,key9]
key1 = false
key2 = false
key3 = false
key4 = false
key5 = false
key6 = false
key7 = false
key8 = false
key9 = false
key0 = false

#ASSIGN PLAYER COLOURS
player1Colour = green
player2Colour = blue

#Assign player sprites ------------------------------------------------------ basic only one no animation
#Player1
player1Sprite = [
pygame.image.load("Run/Corre_test0000.png").convert_alpha(),
pygame.image.load("Run/Corre_test0001.png").convert_alpha(),
pygame.image.load("Run/Corre_test0002.png").convert_alpha(),
pygame.image.load("Run/Corre_test0003.png").convert_alpha(),
pygame.image.load("Run/Corre_test0004.png").convert_alpha(),
pygame.image.load("Run/Corre_test0005.png").convert_alpha(),
pygame.image.load("Run/Corre_test0006.png").convert_alpha(),
pygame.image.load("Run/Corre_test0007.png").convert_alpha(),
pygame.image.load("Run/Corre_test0008.png").convert_alpha(),
pygame.image.load("Run/Corre_test0009.png").convert_alpha(),
]
player1SpriteListLength = len(player1Sprite)
player1SpriteIndex = 0
player1IntSpriteIndex = 0
player1SpriteFPS = 10
player1SpriteFPSAdd = 10/FPS
player1SpriteMask = pygame.mask.from_surface(player1Sprite[0])
player1SpriteRectangle = player1Sprite[0].get_rect()
player1SpriteMaskRectangle = player1SpriteMask
player1SpriteHalfWidth = player1SpriteRectangle.center[0]
player1SpriteHalfHeight = player1SpriteRectangle.center[1]


#player two
player2Sprite = [
pygame.image.load("Run/Corre_test0000.png").convert_alpha(),
pygame.image.load("Run/Corre_test0001.png").convert_alpha(),
pygame.image.load("Run/Corre_test0002.png").convert_alpha(),
pygame.image.load("Run/Corre_test0003.png").convert_alpha(),
pygame.image.load("Run/Corre_test0004.png").convert_alpha(),
pygame.image.load("Run/Corre_test0005.png").convert_alpha(),
pygame.image.load("Run/Corre_test0006.png").convert_alpha(),
pygame.image.load("Run/Corre_test0007.png").convert_alpha(),
pygame.image.load("Run/Corre_test0008.png").convert_alpha(),
pygame.image.load("Run/Corre_test0009.png").convert_alpha(),
]
player2SpriteListLength = len(player2Sprite)
player2SpriteIndex = 0
player2IntSpriteIndex = 0
player2SpriteFPS = 10
player2SpriteFPSAdd = 10/FPS
player2SpriteMask = pygame.mask.from_surface(player2Sprite[0])
player2SpriteRectangle = player2Sprite[0].get_rect()
player2SpriteMaskRectangle = player2SpriteMask
player2SpriteHalfWidth = player2SpriteRectangle.center[0]
player2SpriteHalfHeight = player2SpriteRectangle.center[1]

#floors
whiteBoxSprite = pygame.image.load("floor.png").convert_alpha()
whiteBoxSpriteMask = pygame.mask.from_surface(whiteBoxSprite)
whiteBoxSpriteRectangle = whiteBoxSprite.get_rect()
whiteBoxSpriteHalfWidth = whiteBoxSpriteRectangle.center[0]
whiteBoxSpriteHalfHeight = whiteBoxSpriteRectangle.center[1]

plainBrownSprite = pygame.image.load("plainBrown.png").convert_alpha()
plainBrownSpriteMask = pygame.mask.from_surface(plainBrownSprite)
plainBrownSpriteRectangle = plainBrownSprite.get_rect()
plainBrownSpriteHalfWidth = plainBrownSpriteRectangle.center[0]
plainBrownSpriteHalfHeight = plainBrownSpriteRectangle.center[1]




#two by two sprite
BlockSprite2x2 = pygame.image.load("2by2.png").convert_alpha()

#ASSIGN PLAYER VARIABLES
#How to win
numberOfRounds = 30
numberOfRoundsLeft = numberOfRounds
playerTotalTimeLeft =[0,0]
playerTotalDistanceApart = [0,0]

#Random number start
randomNumberMax = 30
randomStartNumber = random.randint(1,randomNumberMax)
playerNumber = [4,5]
framesLeft = 10 * FPS
timeShowWhoGuessedRight = 5 * FPS

#Switch maps
roundsBeforeSwitch = 2
roundsUntillSwitch = roundsBeforeSwitch

#Title stuff
gameTitleFontSizeMin = 150
gameTitleFontSizeMax = 300
gameTitleFontSize = gameTitleFontSizeMin
gameTitleFontState = "growing"
titleBoxTopPosition = 300
titleBoxThickness = (200,40)
titleBoxColour = green
#boxCoords = (roomWidthStart/2-halfTitleBoxThickness,roomHeightStart - titleBoxTopPosition, titleBoxThickness[0],titleBoxThickness[1])

#Gravity
pixelsToMeters = player1SpriteHalfHeight
gravityMax = 10
gravityAdd = 0.2
airResistanceSlow = 0.1

#Jumps
jumpsMax = 2
jumpsHeight = 20
jumpsRemaning = [jumpsMax,jumpsMax]
fallSpeedIncreace = 1.2 #must be bigger than 1

#Speed
BaseSpeed = 8
chasingSpeedMultiplier = 1.3
player1Speed = BaseSpeed        #[ x speed, jump height]
player2Speed = BaseSpeed        #[ x speed, jump height]

#Initilise bad countdown, never works because the code doesnt alwyas run at max speed
tagSwitchTime = 30 #in secconds
tagTimerCountdown = FPS * tagSwitchTime

#Velocity
player1PosChange = [0,0]    #float version for smooth movement
player2PosChange = [0,0]

player1ActualPosChange = [0,0] #integer version for actual moving and colliosion
player1ActualPosChange = [0,0]


#DEFINE FUNCTIONS
#Fill the screen with black
def loadMap(mapNumber):
    wallCoordList = []
    spawnPointList1 = []
    spawnPointList2 = []
    plainBrownList = []
    roomWidth = 0
    roomHeight = 0
    blockSize = 16

    #convert w's into coordinate list
    x = y = 0
    for row in mapList[mapNumber-1]:
        for column in row:
            if column == "W":
                wallCoordList.append((x,y))
            if column == "1":
                spawnPointList1.append((x,y))
            if column == "2":
                spawnPointList2.append((x,y))
            if column == "B":
                plainBrownList.append((x,y))
            x += blockSize
            if x > roomWidth:
                roomWidth = x
        y += blockSize
        if y > roomHeight:
            roomHeight = y
        x = 0
        
    #SPAWN PLAYERS
    player1SpawnPoint = list(spawnPointList1[0])
    player1Pos = [player1SpawnPoint[0],player1SpawnPoint[1]]


    player2SpawnPoint = list(spawnPointList2[0])
    player2Pos = [player2SpawnPoint[0], player2SpawnPoint[1]]
    
    return wallCoordList,player1SpawnPoint,player2SpawnPoint,player1Pos,player2Pos,roomWidth,roomHeight,plainBrownList

def clearScreen(colour):
    gameDisplay.fill(colour)

def intRoundUp(number):
    g = int(number) + 1
    return g

def text_objects(text,font,colour):
    textSurface = font.render(text,True,colour)
    return textSurface, textSurface.get_rect()

def drawText(x,y,colour,font,size,text):
    drawingFont = pygame.font.Font(font,size)
    textSurf,textRect = text_objects(text,drawingFont,colour)
    textRect.center = (x,y)
    gameDisplay.blit(textSurf,textRect)


def resetVariables():
    #RESET TIMER
    tagTimerCountdown = FPS * tagSwitchTime
    return tagTimerCountdown


def drawPlainBrownBox(coords):
    #Player1 Coll
    #Vertical
    player1TopCorner = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight]
    player1_brownBoxOffsetWithVsp = (coords[0] - (player1TopCorner[0]),coords[1] - (player1TopCorner[1] + player1ActualPosChange[1]))
    player1_brownBoxCollideWithVsp = player1SpriteMask.overlap(plainBrownSpriteMask,player1_brownBoxOffsetWithVsp)
    
    if player1_brownBoxCollideWithVsp:

        #add jumps
        if player1ActualPosChange[1] > 0:
            jumpsRemaning[0] = jumpsMax


##        #Move to pixel perfect location
##        player1TopCornerMinusTwo = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight + 1]
##        player1_whiteSquareOffsetMinusTwo = [coords[0] - player1TopCornerMinusTwo[0],coords[1]  - player1TopCornerMinusTwo[1]]
##        player1_whiteSquareCollideMinusTwo = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetMinusTwo)
##        while player1_whiteSquareCollideMinusTwo == None:
##            player1Pos[1] += 1
##            #update variables for loop
##            player1TopCornerMinusTwo = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight - 2]
##            player1_whiteSquareOffsetMinusTwo = [coords[0] - player1TopCornerMinusTwo[0],coords[1]  - player1TopCornerMinusTwo[1]]
##            player1_whiteSquareCollideMinusTwo = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetMinusTwo)
   
        
        player1ActualPosChange[1] = 0

        

    
    
    #Horisontal
    player1_brownBoxOffsetWithHsp = (coords[0] - (player1TopCorner[0] + player1ActualPosChange[0]),coords[1] - player1TopCorner[1])
    player1_brownBoxCollideWithHsp = player1SpriteMask.overlap(plainBrownSpriteMask,player1_brownBoxOffsetWithHsp)
    if player1_brownBoxCollideWithHsp:
        player1ActualPosChange[0] = 0


    #Player2 Coll
    #Vertical
    player2TopCorner = [player2Pos[0] - player2SpriteHalfWidth,player2Pos[1] - player2SpriteHalfHeight]
    player2_brownBoxOffsetWithVsp = (coords[0] - player2TopCorner[0],coords[1] - (player2TopCorner[1] + player2ActualPosChange[1]))
    player2_brownBoxCollideWithVsp = player2SpriteMask.overlap(plainBrownSpriteMask,player2_brownBoxOffsetWithVsp)
    
    if player2_brownBoxCollideWithVsp:
        if player2ActualPosChange[1] > 0:
            jumpsRemaning[1] = jumpsMax
        player2ActualPosChange[1] = 0

    #Horisontal
    player2_brownBoxOffsetWithHsp = (coords[0] - (player2TopCorner[0] + player2ActualPosChange[0]),coords[1] - player2TopCorner[1])
    player2_brownBoxCollideWithHsp = player2SpriteMask.overlap(plainBrownSpriteMask,player2_brownBoxOffsetWithHsp)
    if player2_brownBoxCollideWithHsp:
        player2ActualPosChange[0] = 0


              
    gameDisplay.blit(plainBrownSprite,coords)
    globalVariables = [player1Pos,player1ActualPosChange,player2Pos,player2ActualPosChange]
    return globalVariables





def drawWhiteBox(coords):
    #Player1 Coll
    #Vertical
    player1TopCorner = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight]
    player1_whiteSquareOffsetWithVsp = (coords[0] - (player1TopCorner[0]),coords[1] - (player1TopCorner[1] + player1ActualPosChange[1]))
    player1_whiteSquareCollideWithVsp = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetWithVsp)
    
    if player1_whiteSquareCollideWithVsp:

        #add jumps
        if player1ActualPosChange[1] > 0:
            jumpsRemaning[0] = jumpsMax


##        #Move to pixel perfect location
##        player1TopCornerMinusTwo = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight + 1]
##        player1_whiteSquareOffsetMinusTwo = [coords[0] - player1TopCornerMinusTwo[0],coords[1]  - player1TopCornerMinusTwo[1]]
##        player1_whiteSquareCollideMinusTwo = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetMinusTwo)
##        while player1_whiteSquareCollideMinusTwo == None:
##            player1Pos[1] += 1
##            #update variables for loop
##            player1TopCornerMinusTwo = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight - 2]
##            player1_whiteSquareOffsetMinusTwo = [coords[0] - player1TopCornerMinusTwo[0],coords[1]  - player1TopCornerMinusTwo[1]]
##            player1_whiteSquareCollideMinusTwo = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetMinusTwo)
   
        
        player1ActualPosChange[1] = 0

        

    
    
    #Horisontal
    player1_whiteSquareOffsetWithHsp = (coords[0] - (player1TopCorner[0] + player1ActualPosChange[0]),coords[1] - player1TopCorner[1])
    player1_whiteSquareCollideWithHsp = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetWithHsp)
    if player1_whiteSquareCollideWithHsp:
        player1ActualPosChange[0] = 0


    #Player2 Coll
    #Vertical
    player2TopCorner = [player2Pos[0] - player2SpriteHalfWidth,player2Pos[1] - player2SpriteHalfHeight]
    player2_whiteSquareOffsetWithVsp = (coords[0] - player2TopCorner[0],coords[1] - (player2TopCorner[1] + player2ActualPosChange[1]))
    player2_whiteSquareCollideWithVsp = player2SpriteMask.overlap(whiteBoxSpriteMask,player2_whiteSquareOffsetWithVsp)
    
    if player2_whiteSquareCollideWithVsp:
        if player2ActualPosChange[1] > 0:
            jumpsRemaning[1] = jumpsMax
        player2ActualPosChange[1] = 0

    #Horisontal
    player2_whiteSquareOffsetWithHsp = (coords[0] - (player2TopCorner[0] + player2ActualPosChange[0]),coords[1] - player2TopCorner[1])
    player2_whiteSquareCollideWithHsp = player2SpriteMask.overlap(whiteBoxSpriteMask,player2_whiteSquareOffsetWithHsp)
    if player2_whiteSquareCollideWithHsp:
        player2ActualPosChange[0] = 0


              
    gameDisplay.blit(whiteBoxSprite,coords)
    globalVariables = [player1Pos,player1ActualPosChange,player2Pos,player2ActualPosChange]
    return globalVariables


def checkKeyboard():
    keyList[12] = false
    keyList[13] = false
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
#keyList = [keyLeft,keyRight,keyUp,keyDown,keyDot,keyForwardSlash,keyQ,keyE,keyW,keyA,keyS,keyD,keyUpPressed,keyWPressed]
            #PLAYER ONE
            if event.key == pygame.K_LEFT:      #Left
                keyList[0] = true
            if event.key == pygame.K_RIGHT:     #Right
                keyList[1] = true
            if event.key == pygame.K_UP:        #Up
                keyList[2] = true
                keyList[12] = true
            if event.key == pygame.K_DOWN:      #Down
                keyList[3] = true
            if event.key == pygame.K_PERIOD:    #Backslash
                keyList[4] = true
            if event.key == pygame.K_SLASH:     #Dot
                keyList[5] = true
                
            #PLAYER TWO
            if event.key == pygame.K_w:         #W
                keyList[8] = true
                keyList[13] = true
            if event.key == pygame.K_s:         #S
                keyList[10] = true
            if event.key == pygame.K_a:         #A
                keyList[9] = true
            if event.key == pygame.K_d:         #D
                keyList[11] = true
            if event.key == pygame.K_q:         #Q
                keyList[6] = true
            if event.key == pygame.K_e:         #E
                keyList[7] = true
                
            #Keyboard numbers  
            if event.key == pygame.K_0:         #0
                keyListNumbers[0] = true
            if event.key == pygame.K_1:         #1
                keyListNumbers[1] = true
            if event.key == pygame.K_2:         #2
                keyListNumbers[2] = true
            if event.key == pygame.K_3:         #3
                keyListNumbers[3] = true
            if event.key == pygame.K_4:         #4
                keyListNumbers[4] = true
            if event.key == pygame.K_5:         #5
                keyListNumbers[5] = true
            if event.key == pygame.K_6:         #6
                keyListNumbers[6] = true
            if event.key == pygame.K_7:         #7
                keyListNumbers[7] = true
            if event.key == pygame.K_8:         #8
                keyListNumbers[8] = true
            if event.key == pygame.K_9:         #9
                keyListNumbers[9] = true

            

                
        if event.type == pygame.KEYUP:

            #PLAYER ONE
            if event.key == pygame.K_LEFT:      #Left
                keyList[0] = false
            if event.key == pygame.K_RIGHT:     #Right
                keyList[1] = false
            if event.key == pygame.K_UP:        #Up
                keyList[2] = false
            if event.key == pygame.K_DOWN:      #Down
                keyList[3] = false
            if event.key == pygame.K_PERIOD:    #Backslash
                keyList[4] = false
            if event.key == pygame.K_SLASH:     #Dot
                keyList[5] = false
                
            #PLAYER TWO
            if event.key == pygame.K_w:         #W
                keyList[8] = false
            if event.key == pygame.K_s:         #S
                keyList[10] = false
            if event.key == pygame.K_a:         #A
                keyList[9] = false
            if event.key == pygame.K_d:         #D
                keyList[11] = false
            if event.key == pygame.K_q:         #Q
                keyList[6] = false
            if event.key == pygame.K_e:         #E
                keyList[7] = false

              #Keyboard numbers
            if event.key == pygame.K_0:         #0
                keyListNumbers[0] = false
            if event.key == pygame.K_1:         #1
                keyListNumbers[1] = false
            if event.key == pygame.K_2:         #2
                keyListNumbers[2] = false
            if event.key == pygame.K_3:         #3
                keyListNumbers[3] = false
            if event.key == pygame.K_4:         #4
                keyListNumbers[4] = false
            if event.key == pygame.K_5:         #5
                keyListNumbers[5] = false
            if event.key == pygame.K_6:         #6
                keyListNumbers[6] = false
            if event.key == pygame.K_7:         #7
                keyListNumbers[7] = false
            if event.key == pygame.K_8:         #8
                keyListNumbers[8] = false
            if event.key == pygame.K_9:         #9
                keyListNumbers[9] = false

    
    keyboardImputs = keyList,keyListNumbers            
    return keyboardImputs


def playerChasingSwitch(playerChasing):
    #If player one was chasing, player two is chasing
    if playerChasing == 1:
        playerChasing = 2
    else:
        #if player two was chasing, player one is chasing
        if playerChasing == 2:
            playerChasing = 1

    #Return player chasing
    return playerChasing

def player1Wins(playerChasing,tagTimerCountdown):
    #Reset coordinates
    player1Pos[0] = player1SpawnPoint[0]
    player1Pos[1] = player1SpawnPoint[1]
    player2Pos[0] = player2SpawnPoint[0]
    player2Pos[1] = player2SpawnPoint[1]

    #Add one to score
    score[0] += 1

    #SWITCH CHASING PLAYER
    playerChasing = playerChasingSwitch(playerChasing)

    #Reset variables
    tagTimerCountdown = resetVariables()

    #Return variables
    globalVariables = [player1Pos,player2Pos,score,playerChasing,tagTimerCountdown]
    return globalVariables

def player2Wins(playerChasing,tagTimerCountdown):
    #Reset Coordinates
    player1Pos[0] = player1SpawnPoint[0]
    player1Pos[1] = player1SpawnPoint[1]
    player2Pos[0] = player2SpawnPoint[0]
    player2Pos[1] = player2SpawnPoint[1]

    #Add one to score
    score[1] += 1
    #Switch who's chasing
    playerChasing = playerChasingSwitch(playerChasing)

    #Reset variables
    tagTimerCountdown = resetVariables()

    
    #Return variables
    globalVariables = [player1Pos,player2Pos,score,playerChasing,tagTimerCountdown]
    return globalVariables

def mapSelect(tempRoomHeight,el):
    roomWdith = 800
    if el == mapRange:
        tempRoomHeight = 0
    
        
    #DRAW MAPS
    #Decode map
    wallCoordList = []
    blockSize = 2
    #convert w's into coordinate list
    xStartPos = roomWidthStart/2 - 100
    x = xStartPos
    y = 200 * el - 100
    for row in mapList[el-1]:
        for column in row:
            if column == "W":
                wallCoordList.append((x,y))
            if column == "B":
                wallCoordList.append((x,y))
            x += blockSize    
        y += blockSize
        x = xStartPos
        if y > tempRoomHeight:
            tempRoomHeight = y


    roomHeight = tempRoomHeight + 100
    #Blit map
    for coords in wallCoordList:
        gameDisplay.blit(BlockSprite2x2,coords)

    
    
    drawText(roomWidthStart/2,200*el - 150,black,basic,22,"PRESS " +str(el) + " TO CHOOSE THIS MAP - ")
    return roomWidth,roomHeight
    
    



#---------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------START GAME------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    while state == "game title":
        gameDisplay = pygame.display.set_mode((roomWidthStart,roomHeightStart))
        clearScreen(white)
        keyList,keyListNumbers = checkKeyboard()
        mousePos = pygame.mouse.get_pos()
        
        if gameTitleFontState == "growing":
            gameTitleFontSize += 1
            if gameTitleFontSize >= gameTitleFontSizeMax:
                gameTitleFontState = "shrinking"

        if gameTitleFontState == "shrinking":
            gameTitleFontSize -= 1
            if gameTitleFontSize <= gameTitleFontSizeMin:
                gameTitleFontState = "growing"




        pygame.draw.rect(gameDisplay,titleBoxColour,boxCoords )
        drawText(roomWidthStart/2,300,black,basic,gameTitleFontSize,str(gameName))
        pygame.display.update()
        clock.tick(FPS)



        
    while state == "choose tagger":
        gameDisplay = pygame.display.set_mode((roomWidthStart,roomHeightStart))
        clearScreen(white)
        keyList,keyListNumbers = checkKeyboard()

        keyChange = [keyList[8]-keyList[10],keyList[2] - keyList[3]]
        
        playerNumber = [playerNumber[0] + keyChange[0],playerNumber[1] + keyChange[1]]
    

        if playerNumber[0] > randomNumberMax:
            playerNumber[0] = randomNumberMax

        if playerNumber[1] > randomNumberMax:
            
            playerNumber[1] = randomNumberMax

        if playerNumber[0] < 1:
            playerNumber[0] = 1

        if playerNumber[1] < 1:
            playerNumber[1] = 1

        framesLeft -=1
        if framesLeft > 0:
            drawText(roomWidthStart/2,100,black,basic,22,"PICK A NUMBER BETWEEN 1 AND " + str(randomNumberMax))
            drawText(roomWidthStart/2,150,black,basic,22,"TIME LEFT: " + str(abs(int(framesLeft/FPS))))
            drawText(roomWidthStart/4,200,black,basic,22,str(playerNumber[0]))
            drawText(3 * roomWidthStart/4,200,black,basic,22,str(playerNumber[1]))

        else:
            if framesLeft == 0:
                distanceApart = [abs(randomStartNumber - playerNumber[0]),abs(randomStartNumber - playerNumber[1])]
                closestNumber = min(distanceApart[0],distanceApart[1])

                if closestNumber == distanceApart[1]:
                    playerChasing = 2
                    hiding = 1
                    tempState = "room select"
                    wentToRandom = False
                
                if closestNumber == distanceApart[0]:
                    if closestNumber == distanceApart[1]:
                        a = random.randint(1,2)
                        wentToRandom = True
                        playerChasing = a
                        if a ==1:
                            hiding = 2
                        if a == 2:
                            hiding = 1
                        tempState = "room select"
                    else:
                        playerChasing = 1
                        hiding = 2
                        tempState = "room select"
                        wentToRandom = False
            else:
                if framesLeft == -timeShowWhoGuessedRight:
                    state = tempState
                    wentToRandom = False
                
                else:
        
                    if framesLeft > -timeShowWhoGuessedRight:
                        drawText(roomWidthStart/2,100,black,basic,22,"TIME LEFT: " + str(abs(int((framesLeft+ timeShowWhoGuessedRight)/FPS))))
                        drawText(roomWidthStart/2,150,black,basic,22,"The random number was " + str(randomStartNumber))
                        drawText(roomWidthStart/2,200,black,basic,22,"Player one guessed " + str(playerNumber[0]) + " and was " + str(distanceApart[0]) + " points apart")
                        drawText(roomWidthStart/2,250,black,basic,22,"Player two guessed " + str(playerNumber[1]) + " and was " + str(distanceApart[1]) + " points apart")
                        if wentToRandom:
                            drawText(roomWidthStart/2,300,black,basic,22,"Beacause you were both the same distance apart it went to the random number generator and it chose player " +str(playerChasing) + " to chase")
                        drawText(roomWidthStart/2,350,black,basic,22,"Therefore player chasing is " + str(playerChasing))
                
            

        
        pygame.display.update()
        #WAIT 
        clock.tick(FPS)


        
    while state == "game finished":
        gameDisplay = pygame.display.set_mode((roomWidth,roomHeight))
        clearScreen(white)  
        #Establish user imputs
        keyList,keyListNumbers = checkKeyboard()


        winningPlayerScore = max(score[0],score[1])
        
        if winningPlayerScore == score[0]:
            winningPlayer = "1"
        if winningPlayerScore == score[1]:
            if winningPlayerScore == score[0]:
                winningPlayer = "1 and 2"
            else:
                winningPlayer = "2"




        drawText(roomWidth/2,100,black,basic,22,"GAME OVER")
        
        drawText(roomWidth/2,150,black,basic,22,"PLAYER " + winningPlayer + " Wins")
            
        pygame.display.update()
        #WAIT 
        clock.tick(FPS)



        
    while state == "got tagged":



        
        gameDisplay = pygame.display.set_mode((roomWidth,roomHeight))
        clearScreen(black)
        keyList,keyListNumbers, = checkKeyboard()

        

        drawText(roomWidth/2,100,white,basic,22,deathMessage)
        drawText(roomWidth/2,200,white,basic,22,"SCORE IS EQUAL TO:")
        drawText(roomWidth/2,250,white,basic,22,"PLAYER ONE: " + str(score[0]))
        drawText(roomWidth/2,300,white,basic,22,"PLAYER TWO: " + str(score[1]))
        drawText(roomWidth/2,350,white,basic,22,"PLAYER CHASING IS " + str(playerChasing))

        if roundsUntillSwitch == 0:
            drawText(roomWidth/2,150,white,basic,22,"PRESS 1 TO CHANGE MAP")
            if keyListNumbers[1]:
                state = "room select"
                roundsUntillSwitch = roundsBeforeSwitch

        else:
            drawText(roomWidth/2,150,white,basic,22,"PRESS 1 TO PLAY AGAIN")
            if keyListNumbers[1]:
                blockSize = gameBlockSize
                wallCoordList,player1SpawnPoint,player2SpawnPoint,player1Pos,player2Pos,roomWidth,roomHeight,plainBrownList = loadMap(lastMap)
                gameDisplay = pygame.display.set_mode((roomWidth,roomHeight))
                state = "playing"


        if numberOfRoundsLeft == 0:
            state = "game finished"
            
        pygame.display.update()
        #WAIT 
        clock.tick(FPS)


        
    
    while state == "room select":
        gameDisplay = pygame.display.set_mode((roomWidthStart,roomHeightStart))
        clearScreen(white)
        
        keyList,keyListNumbers, = checkKeyboard()
        mapRange = len(mapList)

        for el in range (1,mapRange+1,1):
            #draw Gui
            mapSelect(tempRoomHeight,el) #have to be in a function so variables arent affected
            
            

            #Check keys
            if keyListNumbers[el]:
                mapNumber = el
                blockSize = gameBlockSize
                wallCoordList,player1SpawnPoint,player2SpawnPoint,player1Pos,player2Pos,roomWidth,roomHeight,plainBrownList = loadMap(el)
                gameDisplay = pygame.display.set_mode((roomWidth,roomHeight))
                state = "playing"
                lastMap = el


        pygame.display.update()
        #WAIT 
        clock.tick(FPS)

        




        
    while state == "playing":

        #-------------------------------------------------------STEP ONE, KEYBOARD IMPUTS/ CLEAR SCREEN ------------------------------------------------------------------------------
        #CLEAR5 SCREEN
        clearScreen(white)      #Always clear screen first, only needed if no background
        
        #Establish user imputs
        keyList,keyListNumbers = checkKeyboard()

        

        #------------------------------------------------------STEP TWO, MOVE THE PLAYERS----------------------------------------------------------------------------
        #APPLY JUMPS TO PAYERS
        #Player two jumps
        #move up when up key is pressed
        if jumpsRemaning[0] > 0:
            if keyList[13]:
                jumpsRemaning[0] -= 1
                player1PosChange[1] =  -jumpsHeight
                
        #variable jump height
        if player2PosChange[1] < 0:
            if keyList[2] != 1:
                player2PosChange[1] = max(player2PosChange[1],-jumpsHeight/2)

        #falling fast
        if keyList[3]:
            player2PosChange[1] += fallSpeedIncreace

        #falling fast
        if keyList[10]:
            player1PosChange[1] += fallSpeedIncreace
            
        #Player one jumps
        #Move up when up key is pressed
        if jumpsRemaning[1] > 0:  
            if keyList[12]:
                jumpsRemaning[1] -= 1
                player2PosChange[1] = -jumpsHeight

        #Variable jump height
        if player1PosChange[1] < 0:
            if keyList[8] != 1:
                player1PosChange[1] = max(player1PosChange[1],-jumpsHeight/2)
                
        
                
        #APPLY GRAVITY TO PLAYERS
        #Player one gravity
        #Add gravity if not reached terminal velocity
        if player1PosChange[1] < gravityMax:
            player1PosChange[1] += gravityAdd
        else:
        #slow down if reached terminal velocity
            if player1PosChange[1] > gravityMax:
                player1PosChange[1] -= airResistanceSlow

        #Player two gravity
        #Add gravity if not reached terminal velocity
        if player2PosChange[1] < gravityMax:
            player2PosChange[1] += gravityAdd
        else:
        #slow down if reached terminal velocity
            if player2PosChange[1] > gravityMax:
                player2PosChange[1] -= airResistanceSlow

                
        #MOVE PLAYERS LEFT AND RIGHT
        if playerChasing == 1:
            player1Speed = BaseSpeed * chasingSpeedMultiplier
            player2Speed = BaseSpeed
        else:
            if playerChasing == 2:
                player2Speed = BaseSpeed * chasingSpeedMultiplier
                player1Speed = BaseSpeed
                    


        player1PosChange[0] = player1Speed *(keyList[11] - keyList[9])
        player2PosChange[0] = player2Speed * (keyList[1] - keyList[0])

        


        #-----------------------------------------------STEP THREE, DRAW WALLS AND COLIDE PLAYERS WITH SAID WALLS--------------------------------------------------------
        #convert velocity into int form
        player1ActualPosChange = [int(player1PosChange[0]),intRoundUp(player1PosChange[1])]
        player2ActualPosChange = [int(player2PosChange[0]),intRoundUp(player2PosChange[1])]

        #run through coordinate list, draw and collide players + RETURN VALUES IF CHANGED
        for el in wallCoordList:
            player1Pos,player1ActualPosChange,player2Pos,player2ActualPosChange = drawWhiteBox(el)
            player1PosChange = player1ActualPosChange
            player2PosChange = player2ActualPosChange

        for el in plainBrownList:
            player1Pos,player1ActualPosChange,player2Pos,player2ActualPosChange = drawPlainBrownBox(el)
            player1PosChange = player1ActualPosChange
            player2PosChange = player2ActualPosChange


         

        #---------------------------------------------STEP FOUR, MOVE PLAYERS AND DO PLAYER-PLAYER INTERACTIONS-----------------------------------------------
        #Move player coordinates
        player1Pos[0] += player1ActualPosChange[0]     #change x player 1
        player1Pos[1] += player1ActualPosChange[1]     #change y player 1
        
        player2Pos[0] += player2ActualPosChange[0]     #change x player 2
        player2Pos[1] += player2ActualPosChange[1]     #change y player 2

        #Player-player collisions
        #Player one is chasing
        if playerChasing == 1 :
            #Check for collisions
            player1_player2Offset = (player1Pos[0] - player2Pos[0],player1Pos[1] - player2Pos[1])
            player1_player2Collide = player1SpriteMask.overlap(player2SpriteMask,player1_player2Offset)
            if player1_player2Collide:
                #Player one wins this round
                playerTotalTimeLeft[1] += tagTimerCountdown #must be called before the tag timer is reset
                player1Pos,player2Pos,score,playerChasing,tagTimerCountdown = player1Wins(playerChasing,tagTimerCountdown)
                state = "got tagged"
                deathMessage = "PLAYER 1 TAGGED PLAYER 2"
                roundsUntillSwitch -= 1
                numberOfRoundsLeft -= 1
                
        
        #Player Two is chasing
        if playerChasing == 2 :
            #Check for collisions
            player1_player2Offset = (player1Pos[0] - player2Pos[0],player1Pos[1] - player2Pos[1])
            player1_player2Collide = player1SpriteMask.overlap(player2SpriteMask,player1_player2Offset)
            if player1_player2Collide:
                #Player two wins this round
                playerTotalTimeLeft[0] += tagTimerCountdown #Must be called before tag timer countdown is reset
                player1Pos,player2Pos,score,playerChasing,tagTimerCountdown = player2Wins(playerChasing,tagTimerCountdown)
                state = "got tagged"
                deathMessage = "PLAYER 2 TAGGED PLAYER 1"
                roundsUntillSwitch -= 1
                numberOfRoundsLeft -= 1
                


        #Timer stuff
        tagTimerCountdown -= 1
        if tagTimerCountdown == 0:
            if playerChasing == 2:
                #player 1 wins this round
                player1Pos,player2Pos,score,playerChasing,tagTimerCountdown = player1Wins(playerChasing,tagTimerCountdown)
                state = "got tagged"
                deathMessage = "PLAYER 1 EVADED PLAYER 2"
                roundsUntillSwitch -= 1
                numberOfRoundsLeft -= 1
                playerTotalDistanceApart[1] += distanceApart


            else:
                if playerChasing == 1:
                    #Player two wins this round
                    player1Pos,player2Pos,score,playerChasing,tagTimerCountdown = player2Wins(playerChasing,tagTimerCountdown)
                    state = "got tagged"
                    deathMessage = "PLAYER 2 EVADED PLAYER 1"
                    numberOfRoundsLeft -= 1
                    roundsUntillSwitch -= 1
                    

        
        #----------------------------------------------------STEP FIVE, BLIT TO SCREEN, ANIMATE-----------------------------------------------------------------------------
        #ANIMATE PLAYERS
        
        
        player1IntSpriteIndex = int(player1SpriteIndex)
        if player1SpriteIndex > player1SpriteListLength - 1:
            player1SpriteIndex = 0
        player1SpriteIndex += player1SpriteFPSAdd
            
        
        player2IntSpriteIndex = int(player2SpriteIndex)
        if player2SpriteIndex > player2SpriteListLength - 1:
            player2SpriteIndex = 0
        player2SpriteIndex += player2SpriteFPSAdd
            
            
        
        

        #DRAW PLAYERS
        gameDisplay.blit(player1Sprite[player1IntSpriteIndex],(player1Pos[0] - player1SpriteHalfWidth, player1Pos[1] - player1SpriteHalfHeight))
        gameDisplay.blit(player2Sprite[player2IntSpriteIndex],(player2Pos[0] - player2SpriteHalfWidth, player2Pos[1] - player2SpriteHalfHeight))
        

        #Draw HUD
        #Draw Distance
        distanceApartX = abs(player1Pos[0] - player2Pos[0])
        distanceApartY = abs(player1Pos[1] - player2Pos[1])
        distanceApart = int(math.sqrt(distanceApartX**2 + distanceApartY**2))
        distanceApartMeters = intRoundUp(distanceApart/pixelsToMeters)
        drawText(roomWidth - blockSize * 5,blockSize * 2,white,basic,22,str(distanceApartMeters) + " Meters")
        
        
        #Draw score
        if playerChasing == 1:
            player1Colour = blue
            player2Colour = white
        if playerChasing == 2:
            player2Colour = blue
            player1Colour = white
            
        drawText(roomWidth/2 - 10,blockSize * 2,player1Colour,basic,22,str(score[0]))
        drawText(roomWidth/2 + 10,blockSize * 2,player2Colour,basic,22,str(score[1]))

        #Draw time remaning
        
        a = tagTimerCountdown 
        while(a % FPS) != 0:
            a-=1        
        tagTimerCountdownDisplay = int(a/FPS + 1)
        drawText(blockSize * 3,blockSize * 2,white,basic,22,str(tagTimerCountdownDisplay))

        
        
        #----------------------------------------------------------STEP SIX, UPDATE----------------------------------------------------------------------
        #UPDATE DISPLAY
        pygame.display.update()
        #WAIT 
        clock.tick(FPS)

