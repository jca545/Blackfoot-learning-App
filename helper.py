# Drawing functions
# Winnie Chan
# Nov. 16. 2022

import cmpt120image
import random

#Notes:
    #Width = Col = Horizontal = x = len(img[0])
    #Height = Row = Vertical = y = len(img)


def decide():
    decision = random.choice([True, False])
    return decision



def randcolor():
    '''
    Returns a random color in [r, g, b]  
    '''
    color = []
    for i in range(3):
        rgb = random.randint(10, 175)
        color = color + [rgb]
    return color


def isBlack(pixel):
    """ 
    Returns True if the RGB values of pixel combine to black.
    Input: pixel: [r, g, b]
    Output: True if black, False otherwise
    """
    if pixel[0] < 200:
        return True
    return False


def randposit(y, x):
    '''
    Input: canvas = the size of the canvas y, x (int)
    Output: random location
    '''
    y = random.randint(0, y - 80)
    x = random.randint(0, x - 80)
    return y, x


def recolorImage(img,color):
    '''
    Input:
    img = picture = [1:hei [2:wid [3:pixalRGB] 2:th] 1:ght]
    color = random color = [r, g, b]

    Outpupt: newIMG = image in a new color
    
    '''
    height = len(img)
    width = len(img[0])

    newIMG = cmpt120image.getWhiteImage(width, height)
    
    for x in range(width):
        for y in range(height):
            if isBlack(img[y][x]):
                newIMG[y][x] = color
            else:
                pass
                       
    return newIMG
                


def minify(img):
    '''
    Input: img
    Output: newIMG = 1/2 of the original size image
    '''
    height = len(img)
    width = len(img[0])
    
    newIMG = cmpt120image.getWhiteImage(width//2, height//2)
    
    for x in range(width//2):
        for y in range(height//2):
            wid = x*2
            heigh = y*2

            a = img[heigh+1][wid]
            b = img[heigh][wid+1]
            c = img[heigh+1][wid+1]
                
            newRGB = []
            for i in range(3):
                avg = ((img[heigh][wid][i] + a[i] + b[i] + c[i])//4)
                newRGB.append(avg)
            
            newIMG[y][x] = newRGB
                               
    return newIMG 


def mirror(img):
    '''
    Input: img
    Output: newIMG = flipped left/right
    '''
    
    height = len(img)
    width = len(img[0])
    
    newIMG = cmpt120image.getWhiteImage(width, height)
    
    for x in range(width):
        for y in range(height):
            newIMG[y][x] = img[y][width-x-1]

    return newIMG



def drawItem(img,item,row,col):
    '''
    Input:
    img = canvas image object 
    item = the image we want to draw
    row / col = row / col position of where to draw the image item 
    Output: Draw: canvas with a drawn image item
    '''
    
    #For the image
    height = len(item)
    width = len(item[0])

    for x in range(width):
        for y in range(height):
            if isBlack(item[y][x]):
                img[row + y][col + x] = item[y][x]

    cmpt120image.showImage(img)

    return img

    

def distributeItems(img,item,n):
    '''
    Input:
        img = canvas image object
        item = the image
        n = n times
    Output: Draw: canvas with a drawn image item n times
    '''
    height = len(img)
    width = len(img[0])
    
    item = recolorImage(item, randcolor())
    if decide():
        item = mirror(item)

    if decide():
        item = minify(item)
    

    for i in range(n):
        position = randposit(height, width) #y, x
        row = position[0]
        col = position[1]
        
        final = drawItem(img, item, row, col)
    return final
    

#For Testing

'''
img = cmpt120image.getImage("images/child.png")

canvas_size = [300, 400] #[h, w]
canvas = cmpt120image.getWhiteImage(canvas_size[1], canvas_size[0])


#drawItem(canvas,res,100,120)

can = distributeItems(canvas, img, 4)
distributeItems(can, img, 4)
'''






