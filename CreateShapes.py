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

def createEllipses(imageSize, margin, color, borderWidth, matrixContainer, angles):

    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.exists(os.path.join('images', 'ellipses')):
        os.makedirs(os.path.join('images', 'ellipses'))
    areas = createArea(margin, imageSize)
    for area in areas:
        ellipse = Ellipse(area, color, borderWidth, matrixContainer)
        ellipse.draw(imageSize, angles)

def createRectangles(imageSize, margin, color,
        borderWidth, matrixContainer, angles):
    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.exists(os.path.join('images', 'rectangles')):
        os.makedirs(os.path.join('images', 'rectangles'))
    areas = createArea(margin, imageSize)
    for area in areas:
        rectangle = Rectangle(area, color, borderWidth, matrixContainer)
        rectangle.draw(imageSize, angles)

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


def createRightTriangles(imageSize, margin, color, borderWidth, matrixContainer):
    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.exists(os.path.join('images', 'triangles')):
        os.makedirs(os.path.join('images', 'triangles'))


    # there are more then 40 million possible triangles. We choose randomly
    # 15000 of them:
    for _ in range(40000):
        # Draw a diagram.


        x1Coordinate = np.random.randint(margin, imageSize[1] - margin)
        y1Coordinate = np.random.randint(margin, imageSize[0] - margin)

        # Right angle in left upper corner
        lUy2Coordinate = np.random.randint(y1Coordinate, imageSize[0] - margin)
        lUx2Coordinate = x1Coordinate
        lUx3Coordinate = np.random.randint(x1Coordinate, imageSize[1] - margin)
        lUy3Coordinate = y1Coordinate

        # Right angle in left down corner
        lDx2Coordinate = x1Coordinate
        lDy2Coordinate = np.random.randint(y1Coordinate, imageSize[0] - margin)
        lDx3Coordinate = np.random.randint(lDx2Coordinate, imageSize[1] - margin)
        lDy3Coordinate = lDy2Coordinate

        # Right angle in right down corner
        rDx2Coordinate = np.random.randint(x1Coordinate, imageSize[1] - margin)
        rDy2Coordinate = y1Coordinate
        rDx3Coordinate = rDx2Coordinate
        if margin == rDy2Coordinate:
            rDy3Coordinate = margin
        else:
            rDy3Coordinate = np.random.randint(margin, rDy2Coordinate)

        # Right angle in right upper corner
        rUx2Coordinate = np.random.randint(x1Coordinate, imageSize[1] - margin)
        rUy2Coordinate = y1Coordinate
        rUx3Coordinate = rUx2Coordinate
        rUy3Coordinate = np.random.randint(rUy2Coordinate, imageSize[0] - margin)

        # if three x- or y-coordinates are on a line, the 
        # triangle would be empty.
        lUinLine = lUx3Coordinate == x1Coordinate or lUy3Coordinate == lUy2Coordinate
        lDinLine = lDx3Coordinate == x1Coordinate or lDy3Coordinate == y1Coordinate
        rDinLine = rDx3Coordinate == x1Coordinate or rDy2Coordinate == rDy3Coordinate
        rUinLine = rUx3Coordinate == x1Coordinate or rUy2Coordinate == rUy3Coordinate

        if not lUinLine:
            position1 = [x1Coordinate, y1Coordinate]
            position2 = [lUx2Coordinate, lUy2Coordinate]
            position3 = [lUx3Coordinate, lUy3Coordinate]
            pointlist = [position1, position2, position3]
            if not os.path.exists(os.path.join('images', 'triangles', 'triangle' +
                str(pointlist) + '.png')):

                    triangle = Triangle(pointlist,
                        color,borderWidth, matrixContainer)
                    triangle.draw(imageSize)

        if not lDinLine:
            position1 = [x1Coordinate, y1Coordinate]
            position2 = [lDx2Coordinate, lDy2Coordinate]
            position3 = [lDx3Coordinate, lDy3Coordinate]
            pointlist = [position1, position2, position3]
            if not os.path.exists(os.path.join('images', 'triangles', 'triangle' +
                str(pointlist) + '.png')):

                    triangle = Triangle(pointlist,
                        color,borderWidth, matrixContainer)
                    triangle.draw(imageSize)

        if not rUinLine:
            position1 = [x1Coordinate, y1Coordinate]
            position2 = [rUx2Coordinate, rUy2Coordinate]
            position3 = [rUx3Coordinate, rUy3Coordinate]
            pointlist = [position1, position2, position3]
            if not os.path.exists(os.path.join('images', 'triangles', 'triangle' +
                str(pointlist) + '.png')):

                    triangle = Triangle(pointlist,
                        color,borderWidth, matrixContainer)
                    triangle.draw(imageSize)

        if not rDinLine:
            position1 = [x1Coordinate, y1Coordinate]
            position2 = [rDx2Coordinate, rDy2Coordinate]
            position3 = [rDx3Coordinate, rDy3Coordinate]
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
    #borderWidth = sys.argv[1]
    black = [0,0,0]
    rotationAngles = []
    matrixContainer = Container()

    createEllipses(imageSize, margin, black, 0, matrixContainer, rotationAngles)
    createRectangles(imageSize, margin, black, 0, matrixContainer, rotationAngles)
    createRightTriangles(imageSize, margin, black, 0, matrixContainer)
    # createTriangles(imageSize, margin, black, 0, matrixContainer)
    idxPath = os.path.join('MNIST')
    if not os.path.exists(idxPath):
        os.makedirs(idxPath)
    matrixContainer.getIdx(30000, idxPath)

    pygame.quit()

if __name__ == '__main__':
    __main__()
