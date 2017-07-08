'''
In this file is everything that is needed to set up the Creation of shapes
'''

import pygame
import os
import numpy as np
from scipy import misc


# get the path to our shape image
def getPath(shape, code):
    return os.path.join('images', shape + 's', shape +
            str(code) + '.png')

# Convert our matrices with values of 255 (white) and 0 (black) to a matrix with 0 and 1 to use in our neural network
def convertMatrix(matrix):
     # white is 255, black is 0, the matrices are 8 bit encoded, so modulo 255,
     # so 255 + 1 = 0, 0 + 1 = 1
    return (matrix + 1) % 256 

# get a Matrix from our generated pictures
def getMatrix(imageName):

    imageMatrix = misc.imread(imageName, flatten=True)
    matrix = convertMatrix(imageMatrix)

    return matrix

# check if our shape is big enough and not to lengthy to be distinguishable from the other shapes
def checkMatrix(matrix, imageSize):
    # for a 28x28 image we want shapes which are bigger than 9 pixels. 28x28/80
    # = 9
    matrixok = False
    # check if big enough and not entirely full of the shape (every pixel is 1)
    if np.sum(matrix) > ((imageSize[0] * imageSize[1]) / 80) and np.sum(matrix) < (imageSize[0] * imageSize[1]):
       
        # check if ratio of height to length ok, to rule out super lengthy objects
        shaperow = []
        shapecol = []
        for i in range(imageSize[0]):
            for j in range(imageSize[1]):
                if matrix[i,j] != 0:
                    shaperow.append(i)
                    shapecol.append(j)
        length = max(shaperow) - min(shaperow)
        height = max(shapecol) - min(shapecol)

        # heigth or length that only consist of only 1 pixel are definitly to small, 
        # and this would also give problems in Division so rule this out
        if height > 0 and length > 0:
            ratio = length/height
            # arbitrary ratio
            if ratio < 4 and ratio > 0.25:
                matrixok = True
    return matrixok

# check if our shape is big enough and not to lengthy to be distingusihable from the other shapes
# and check if our shape is in the middle of the picture
def checkMatrixAndMiddle(matrix, imageSize):
    # for a 28x28 image we want shapes which are bigger than 9 pixels. 28x28/80
    # = 9
    matrixok = False
    # check if big enough and not entirely full of the shape (every pixel is 1)
    if np.sum(matrix) > ((imageSize[0] * imageSize[1]) / 80) and np.sum(matrix) < (imageSize[0] * imageSize[1]):
       
        # check if ratio of height to length ok, to rule out super lengthy objects
        shaperow = []
        shapecol = []
        shape = []

        for i in range(imageSize[0]):
            for j in range(imageSize[1]):
                if matrix[i,j] != 0:
                    shaperow.append(i)
                    shapecol.append(j)
                    shape.append([i,j,matrix[i,j]])
        middlepointrow = min(shaperow) + ((max(shaperow) - min(shaperow))/2.)
        middlepointcol = min(shapecol) + ((max(shapecol) - min(shapecol))/2.)
        length = max(shaperow) - min(shaperow)
        height = max(shapecol) - min(shapecol)

        # Define a Area in the middle of the picture in which the middle point of the shape should lie
        middleAreaRowLow = (imageSize[0]/2.) - (imageSize[0]/14.)
        middleAreaRowHigh = (imageSize[0]/2.) + (imageSize[0]/14.)
        middleAreaColLow = (imageSize[1]/2.) - (imageSize[1]/14.)
        middleAreaColHigh = (imageSize[1]/2.) + (imageSize[1]/14.)

        # heigth or length that only consist of only 1 pixel are definitly to small, 
        # and this would also give problems in Division so rule this out
        if height > 0 and length > 0 and middlepointrow >= middleAreaRowLow and middlepointrow <= middleAreaRowHigh and middlepointcol >= middleAreaColLow and middlepointcol <= middleAreaRowHigh:
            ratio = length/height
            # arbitrary ratio
            if ratio < 4 and ratio > 0.25:
                matrixok = True


    return matrixok

# rotate the shapes, this is not possible in pygame, so we need our own function
# we do this by rotating every ("colored") point of our matrix aroung the middle
# point of our shape in a certain angle
def rotate(matrix, angle, imageSize):

    # get middle point of matrix around which we want to rotate the matrix
    # and every point that has a value different from 0 and needs to be rotated
    shaperow = []
    shapecol = []
    shape = []

    for i in range(imageSize[0]):
        for j in range(imageSize[1]):
            if matrix[i,j] != 0:
                shaperow.append(i)
                shapecol.append(j)
                shape.append([i,j,matrix[i,j]])
    middlepointrow = min(shaperow) + ((max(shaperow) - min(shaperow))/2.)
    middlepointcol = min(shapecol) + ((max(shapecol) - min(shapecol))/2.)

    # get our sinus and cosinus values for the degree in which we want to rotate
    s = np.sin(angle);
    c = np.cos(angle);

    # create a new matrix full of zeros, in which we want to fill in our new rotated shape
    rotatetmatrix = np.full((imageSize[0],imageSize[1]), 0)

    for point in shape:
        # translate point to origin:
        point[0] -= middlepointrow;
        point[1] -= middlepointcol;

        #rotate point (trigonometry, peope!)
        xnew = point[0] * c - (point[1] * s);
        ynew = point[0] * s + (point[1] * c);

        # translate point back: (The 0.5 is to round the number and not only cut the decimals off)
        # To prevent pixel-holes in our rotated shape, we "color" four pixels around our rotation-point
        # (Rotation tells us we would need to put our pixel at [3.4,5.6], that is not possible, so instead
        #  we put pixels at [3,5],[5,6],[4,5] and [4,6])
        x1 = int(xnew + middlepointrow - 0.5);
        y1 = int(ynew + middlepointcol - 0.5);
        x2 = int(xnew + middlepointrow + 0.5);
        y2 = int(ynew + middlepointcol + 0.5);
        # Confirm that the new pixel is realy in the picture and than "color it"
        if x1 < imageSize[0] and x1 >= 0 and y1 < imageSize[1] and y1 >= 0 : 
            rotatetmatrix[x1,y1] = point[2]
        if x2 < imageSize[0] and x2 >= 0 and y2 < imageSize[1] and y2 >= 0:
            rotatetmatrix[x2,y2] = point[2]
        if x2 < imageSize[0] and x2 >= 0 and y1 < imageSize[1] and y1 >= 0 :
            rotatetmatrix[x2,y1] = point[2]
        if x1 < imageSize[0] and x1 >= 0 and y2 < imageSize[1] and y2 >= 0:
            rotatetmatrix[x1,y2] = point[2]

    return rotatetmatrix;

class Ellipse:

    def __init__(self, area, color, borderWidth, matrixContainer):
        self.color = color
        self.borderWidth = borderWidth
        self.area = area
        self.imageName = getPath('ellipse', self.area)
        self.matrixContainer = matrixContainer

    # draw an ellipse in pygame, store it as a file (thats because of pygame), we want actually a matrix
    # so read the picture back in as a matrix, rotate it in the specified angles if wanted and store the original
    # as well as every rotated one in our matrixContainer
    def draw(self, imageSize, angles):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.ellipse(screen, self.color, self.area, self.borderWidth)
        pygame.image.save(screen, self.imageName)
        imageMatrix = getMatrix(self.imageName)
        if checkMatrixAndMiddle(imageMatrix, imageSize):

            self.matrixContainer.put(imageMatrix, 'ellipse')

            for angle in angles:
                rotation = rotate(imageMatrix, angle, imageSize)
                if checkMatrixAndMiddle(rotation, imageSize):
                    self.matrixContainer.put(rotation, 'ellipse')


class Triangle:

    def __init__(self, pointlist, color, borderWidth, matrixContainer):
        self.color = color
        self.borderWidth = borderWidth
        self.pointlist = pointlist
        self.imageName = getPath('triangle', self.pointlist)
        self.matrixContainer = matrixContainer

    # draw a triangle (or rather a polygon, because there are no triangles) in pygame, store it as a file (thats because of pygame), we want actually a matrix
    # so read the picture back in as a matrix and store it in our matrixContainer
    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.polygon(screen, self.color, self.pointlist, self.borderWidth)
        pygame.image.save(screen, self.imageName)
        imageMatrix = getMatrix(self.imageName)
        if checkMatrixAndMiddle(imageMatrix, imageSize):

            self.matrixContainer.put(imageMatrix, 'triangle')

            

class Rectangle:

    def __init__(self, area, color, borderWidth, matrixContainer):
        self.color = color
        self.borderWidth = borderWidth
        self.area = area
        self.imageName = getPath('rectangle', self.area)
        self.matrixContainer = matrixContainer

    # draw a rectangle in pygame, store it as a file (thats because of pygame), we want actually a matrix
    # so read the picture back in as a matrix, rotate it in the specified angles if wanted and store the original
    # as well as every rotated one in our matrixContainer
    def draw(self, imageSize, angles):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.rect(screen, self.color, self.area, self.borderWidth)
        pygame.image.save(screen, self.imageName)
        imageMatrix = getMatrix(self.imageName)
        if checkMatrixAndMiddle(imageMatrix, imageSize):

            self.matrixContainer.put(imageMatrix, 'rectangle')

            for angle in angles:
                rotation = rotate(imageMatrix, angle, imageSize)
                if checkMatrixAndMiddle(rotation, imageSize):
                    self.matrixContainer.put(rotation, 'rectangle')


# class Circle:

#     def __init__(self, imageSize, color, borderWidth, margin):
#         self.color = color
#         self.borderWidth = borderWidth
#         # radius 0 would lead to no shape. The circle has to fit on the smaller
#         # side of the image, therefor 'min'. Twice the radius should not be
#         # bigger than the size of the smaller side of the image without the
#         # margins on both sites.
#         smallerSide = min(imageSize[0], imageSize[1])
#         self.radius = np.random.randint(1,  int(smallerSide - 2 * margin) / 2)
#         # The y-Coordinate of the middle point should be at least as far from
#         # each border as the radius + margin
#         yCoordinate = np.random.randint(margin + radius, imageSize[0] - margin
#                 - radius)
#         xCoordinate = np.random.randint(margin + radius, imageSize[1] - margin
#                 - radius)
#         self.position = [xCoordinate, yCoordinate]

#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color, self.position, self.radius, self.borderWidth)
