import pygame
import os
import numpy as np
from scipy import misc

def getPath(shape, code):
    return os.path.join('images', shape + 's', shape +
            str(code) + '.png')

def subMatrix(matrix):
     # white is 255, black is 0, the matrices are 8 bit encoded, so modulo 255,
     # so 255 + 1 = 0, 0 + 1 = 1
     return matrix + 1

def getMatrix(imageName):

    imageMatrix = misc.imread(imageName, flatten=True)

    return imageMatrix

def checkMatrix(matrix, imageSize):
    # for a 28x28 image we want shapes which are bigger than 9 pixels. 28x28/80
    # = 9
    matrixok = False
    # check if big enough
    if np.sum(matrix) < ((imageSize[0] * imageSize[1] * 255) - ((imageSize[0] * imageSize[1]) / 80)*255):
        # check if ratio of height to length ok, to rule out super lengthy objects
        shaperow = []
        shapecol = []
        for i in range(imageSize[0]):
            for j in range(imageSize[1]):
                if matrix[i,j] != 255:
                    shaperow.append(i)
                    shapecol.append(j)
        length = max(shaperow) - min(shaperow)
        height = max(shapecol) - min(shapecol)
        if height > 0 and length > 0:
            ratio = length/height
            if ratio < 4 and ratio > 0.25:
                matrixok = True
    return matrixok

def rotate(matrix, angle, imageSize):

    # get middle point of matrix around which we want to rotate the matrix
    print("I rotate right now")

    shaperow = []
    shapecol = []
    shape = []

    for i in range(imageSize[0]):
        for j in range(imageSize[1]):
            if matrix[i,j] != 255:
                shaperow.append(i)
                shapecol.append(j)
                shape.append([i,j,matrix[i,j]])
    middlepointrow = max(shaperow) - min(shaperow)
    middlepointcol = max(shapecol) - min(shapecol)

    s = np.sin(angle);
    c = np.cos(angle);

    rotatetmatrix = np.full((imageSize[0],imageSize[1]), 255)

    for point in shape:
        # translate point back to origin:
        point[0] -= middlepointrow;
        point[1] -= middlepointcol;

        #rotate point
        xnew = point[0] * c - (point[1] * s);
        ynew = point[0] * s + (point[1] * c);

        #translate point back:
        point[0] = int(xnew + middlepointrow);
        point[1] = int(ynew + middlepointcol);

        if point[0] < 28 and point[0] >= 0 and point[1] < 28 and point[1] >= 0:
            rotatetmatrix[point[0],point[1]] = point[2]

    return rotatetmatrix;

class Ellipse:

    def __init__(self, area, color, borderWidth, matrixContainer, count):
        self.color = color
        self.borderWidth = borderWidth
        self.area = area
        self.imageName = getPath('ellipse', self.area)
        self.matrixContainer = matrixContainer
        self.count = count

    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.ellipse(screen, self.color, self.area, self.borderWidth)
        pygame.image.save(screen, self.imageName)
        imageMatrix = getMatrix(self.imageName)
        if checkMatrix(imageMatrix, imageSize):
            print("I am right!")
            if self.count % 3 == 1:
                imageMatrix = rotate(imageMatrix, 15, imageSize)
            elif self.count % 3 == 2:
                imageMatrix = rotate(imageMatrix, 30, imageSize)
            else:
                print("I don't rotate")
            self.matrixContainer.put(imageMatrix, 'ellipse')
        else:
            print("I am to small")

class Triangle:

    def __init__(self, pointlist, color, borderWidth, matrixContainer):
        self.color = color
        self.borderWidth = borderWidth
        self.pointlist = pointlist
        self.imageName = getPath('triangle', self.pointlist)
        self.matrixContainer = matrixContainer

    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.polygon(screen, self.color, self.pointlist, self.borderWidth)
        pygame.image.save(screen, self.imageName)
        imageMatrix = getMatrix(self.imageName)
        if checkMatrix(imageMatrix, imageSize):
            print("I am right!")
            self.matrixContainer.put(imageMatrix, 'triangle')
        else:
            print("I am to small")
            

class Rectangle:

    def __init__(self, area, color, borderWidth, matrixContainer, count):
        self.color = color
        self.borderWidth = borderWidth
        self.area = area
        self.imageName = getPath('rectangle', self.area)
        self.matrixContainer = matrixContainer
        self.count = count

    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.rect(screen, self.color, self.area, self.borderWidth)
        pygame.image.save(screen, self.imageName)
        imageMatrix = getMatrix(self.imageName)
        if checkMatrix(imageMatrix, imageSize):
            print("I am right!")
            if self.count % 3 == 1:
                imageMatrix = rotate(imageMatrix, 15, imageSize)
            elif self.count % 3 == 2:
                imageMatrix = rotate(imageMatrix, 30, imageSize)
            else:
                print("I don't rotate")
            self.matrixContainer.put(imageMatrix, 'rectangle')
        else:
            print("I am to small")

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
