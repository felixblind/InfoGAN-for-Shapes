import pygame
import sys
import os
import numpy as np
from Shapes import Ellipse, Rectangle, Triangle

def createArea(margin, imageSize, minWidth, minHeight):
    areas = []
    for yCoordinate in range(margin, imageSize[0] - 2 * margin + 1):
        for xCoordinate in range(margin, imageSize[1] - 2 * margin + 1):
            for height in range(minHeight + margin, imageSize[0] - yCoordinate + 1):
                for width in range(minWidth + margin, imageSize[1] - xCoordinate + 1):
                    areas.append([xCoordinate, yCoordinate, width, height])
    return areas

def createEllipses(imageSize, margin, minWidth, minHeight, color, borderWidth):
    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.exists(os.path.join('images', 'ellipses')):
        os.makedirs(os.path.join('images', 'ellipses'))
    # height or width 0 would lead to no shape. The ellipse should not be
    # higher than the height of the image without the margin on both sides.
    # The same is true for the width of the image and the width of the
    # ellipse.
    # The addition of 1 at the end is because of the range function.
    # for yCoordinate in range(margin, imageSize[0] - 2 * margin + 1):
    #     for xCoordinate in range(margin, imageSize[1] - 2 * margin + 1):
    #         for height in range(1 + margin, imageSize[0] - yCoordinate + 1):
    #             for width in range(1 + margin, imageSize[1] - xCoordinate + 1):
    #                 area = [xCoordinate, yCoordinate, width, height]
    areas = createArea(margin, imageSize, minWidth, minHeight)
    for area in areas:
        ellipse = Ellipse(area, color, borderWidth)
        ellipse.draw(imageSize)
        print('ellipe. area = ', area)

def createRectangles(imageSize, margin, color, borderWidth):
    if not os.path.exists('images'):
        os.makedirs('images')
    if not os.path.exists(os.path.join('images', 'rectangles')):
        os.makedirs(os.path.join('images', 'rectangles'))
    # height or width 0 would lead to no shape. The rectangle should not be
    # higher than the height of the image without the margin on both sides.
    # The same is true for the width of the image and the width of the
    # rectangle.
    # The addition of 1 at the end is because of the range function.
    # for yCoordinate in range(margin, imageSize[0] - 2 * margin + 1):
    #     for xCoordinate in range(margin, imageSize[1] - 2 * margin + 1):
    #         for height in range(1 + margin, imageSize[0] - yCoordinate + 1):
    #             for width in range(1 + margin, imageSize[1] - xCoordinate + 1):
    #                 area = [xCoordinate, yCoordinate, width, height]
    areas = createArea(margin, imageSize, minWidth, minHeight)
    for area in areas:
        rectangle = Rectangle(area, color, borderWidth)
        rectangle.draw(imageSize)
        print('rectangle. area = ', area)

def createTriangles(imageSize, margin, color, borderWidth):
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

    i = 0
    # there are more then 40 million possible triangles. We choose randomly
    # 200000 of them:
    while i < 200000:

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
        inLine = inLine or (abs(y1Coordinate - y2Coordinate) ==abs(y2Coordinate - y3Coordinate))
        if not inLine:
            position1 = [x1Coordinate, y1Coordinate]
            position2 = [x2Coordinate, y2Coordinate]
            position3 = [x3Coordinate, y3Coordinate]
            pointlist = [position1, position2, position3]
            if not os.path.exists(os.path.join('images', 'triangles', 'triangle' +
                str(pointlist) + '.png')):

                    triangle = Triangle(pointlist,
                        color,borderWidth)
                    triangle.draw(imageSize)
                    i = i + 1
                    print('triangle. area = ', pointlist)


def __main__():
    imageSize = [28,28]
    margin = 1
    minWidth = 3
    minHeight = 3
    borderWidth = sys.argv[1]
    black = [0,0,0]

    createEllipses(imageSize, margin, minWidth, minHeight, black, 0)
    # createRectangles(imageSize, margin, black, 0)
    # createTriangles(imageSize, margin, black, 0)

    pygame.quit()

if __name__ == '__main__':
    __main__()
