import pygame
import sys
import os
import numpy as np
from Shapes import Ellipse, Rectangle, Triangle
from MatrixContainer import Container


def createArea(margin, imageSize):
    areas = []
    # height or width 0 would lead to no shape. The ellipse should not be
    # higher than the height of the image without the margin on both sides.
    # The same is true for the width of the image and the width of the
    # ellipse.
    # The addition of 1 at the end is because of the range function.
    for yCoordinate in range(margin, imageSize[0] - 2 * margin + 1):
        for xCoordinate in range(margin, imageSize[1] - 2 * margin + 1):
            # for height in range(minHeight + margin, imageSize[0] - yCoordinate + 1):
            for height in range(margin, imageSize[0] - yCoordinate + 1):
                # for width in range(minWidth + margin, imageSize[1] - xCoordinate + 1):
                for width in range(margin, imageSize[1] - xCoordinate + 1):
                    areas.append([xCoordinate, yCoordinate, width, height])
    return areas

def createEllipses(imageSize, margin, color, borderWidth, matrixContainer):

    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.exists(os.path.join('images', 'ellipses')):
        os.makedirs(os.path.join('images', 'ellipses'))
    areas = createArea(margin, imageSize)
    for area in areas:
        ellipse = Ellipse(area, color, borderWidth, matrixContainer)
        ellipse.draw(imageSize)

def createRectangles(imageSize, margin, color,
        borderWidth, matrixContainer):
    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.exists(os.path.join('images', 'rectangles')):
        os.makedirs(os.path.join('images', 'rectangles'))
    areas = createArea(margin, imageSize)
    for area in areas:
        rectangle = Rectangle(area, color, borderWidth, matrixContainer)
        rectangle.draw(imageSize)

def createTriangles(imageSize, margin, color, borderWidth, matrixContainer):
    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.exists(os.path.join('images', 'triangles')):
        os.makedirs(os.path.join('images', 'triangles'))
    # # All three points just have to be somewhere within the margin
    # for y1Coordinate in range(margin, imageSize[0] - margin + 1):
    #     for x1Coordinate in range(margin, imageSize[1] - margin + 1):
    #         for y2Coordinate in range(margin, imageSize[0] - margin + 1):
    #             for x2Coordinate in range(margin, imageSize[1] - margin + 1):
    #                 for y3Coordinate in range(margin, imageSize[0] - margin + 1):
    #                     for x3Coordinate in range(margin, imageSize[1] - margin + 1):

    #                         # if three x- or y-coordinates are on a line, the 
    #                         # triangle would be empty.
    #                         inLine = abs(x1Coordinate - x2Coordinate) == abs(x2Coordinate - x3Coordinate)
    #                         inLine = inLine or (abs(y1Coordinate -
    #                             y2Coordinate) ==abs(y2Coordinate -                                     y3Coordinate))
    #                         if not inLine:
    #                             position1 = [x1Coordinate, y1Coordinate]
    #                             position2 = [x2Coordinate, y2Coordinate]
    #                             position3 = [x3Coordinate, y3Coordinate]
    #                             pointlist = [position1, position2, position3]

    #                             triangle = Triangle(pointlist,
    #                                 color,borderWidth)
    #                             triangle.draw(imageSize)

                            # if three x- or y-coordinates are on a line, the 
                            # triangle would be empty.

    # there are more then 40 million possible triangles. We choose randomly
    # 200000 of them:
    for _ in range(200000):
        # Note that every coordinate is bound by the x coordinate of the first
        # point and the y variable of the second point.
        # Every third corner point is further right than the first point and
        # further down as the second.
        # Draw a diagram.
        x1Coordinate = np.random.randint(margin, imageSize[1] - margin)
        y2Coordinate = np.random.randint(margin, imageSize[0] - margin)
        x2Coordinate = np.random.randint(x1Coordinate, imageSize[1] - margin)
        y1Coordinate = np.random.randint(y2Coordinate, imageSize[0] - margin)
        x3Coordinate = np.random.randint(x1Coordinate, imageSize[1] - margin)
        y3Coordinate = np.random.randint(y2Coordinate, imageSize[0] - margin)

        # if three x- or y-coordinates are on a line, the 
        # triangle would be empty.
        inLine = abs(x1Coordinate - x2Coordinate) == abs(x2Coordinate - x3Coordinate)
        inLine = inLine or (abs(y1Coordinate - y2Coordinate) == abs(y2Coordinate - y3Coordinate))
        if not inLine:
            position1 = [x1Coordinate, y1Coordinate]
            position2 = [x2Coordinate, y2Coordinate]
            position3 = [x3Coordinate, y3Coordinate]
            pointlist = [position1, position2, position3]
            if not os.path.exists(os.path.join('images', 'triangles', 'triangle' +
                str(pointlist) + '.png')):

                    triangle = Triangle(pointlist,
                        color,borderWidth, matrixContainer)
                    triangle.draw(imageSize)

def __main__():
    imageSize = [28,28]
    margin = 1
    minWidth = 3
    minHeight = 3
    borderWidth = sys.argv[1]
    black = [0,0,0]
    rotationAngles = [45]
    matrixContainer = Container()

    createEllipses(imageSize, margin, black, 0, matrixContainer, rotationAngles)
    createRectangles(imageSize, margin, black, 0, matrixContainer, rotationAngles)
    createTriangles(imageSize, margin, black, 0, matrixContainer)
    idxPath = os.path.join('MNIST')
    if not os.path.exists(idxPath):
        os.makedirs(idxPath)
    matrixContainer.getIdx(30000, idxPath)

    pygame.quit()

if __name__ == '__main__':
    __main__()
