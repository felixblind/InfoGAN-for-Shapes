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

    imageMatrix = misc.imread(imageName)
    imageMatrix = (subMatrix(imageMatrix[:,:,0])/3 +
            subMatrix(imageMatrix[:,:,1])/3 +
            subMatrix(imageMatrix[:,:,2])/3)
    return imageMatrix

def checkMatrix(matrix, imageSize):
    # for a 28x28 image we want shapes which are bigger than 9 pixels. 28x28/80
    # = 9
    return np.sum(matrix) > (imageSize[0] * imageSize[1]) / 80

class Ellipse:

    def __init__(self, area, color, borderWidth, matrixContainer):
        self.color = color
        self.borderWidth = borderWidth
        self.area = area
        self.imageName = getPath('ellipse', self.area)
        self.matrixContainer = matrixContainer

    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.ellipse(screen, self.color, self.area, self.borderWidth)
        pygame.image.save(screen, self.imageName)
        imageMatrix = getMatrix(self.imageName)
        if checkMatrix(imageMatrix, imageSize):
            self.matrixContainer.put(imageMatrix, 'ellipse')

class Triangle:

    def __init__(self, area, color, borderWidth, matrixContainer):
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
            self.matrixContainer.put(imageMatrix, 'triangle')

class Rectangle:

    def __init__(self, area, color, borderWidth, matrixContainer):
        self.color = color
        self.borderWidth = borderWidth
        self.area = area
        self.imageName = getPath('rectangle', self.area)
        self.matrixContainer = matrixContainer

    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.rect(screen, self.color, self.area, self.borderWidth)
        pygame.image.save(screen, self.imageName)
        imageMatrix = getMatrix(self.imageName)
        if checkMatrix(imageMatrix, imageSize):
            self.matrixContainer.put(imageMatrix, 'rectangle')

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
