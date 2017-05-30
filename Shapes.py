import pygame
import os

def getPath(shape, code):
    return os.path.join('images', shape + 's', shape +
            str(code) + '.png')

class Ellipse:

    def __init__(self, area, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth
        self.area = area
        # self.imageName = os.path.join('images', 'ellipses', 'ellipse-' + str(area) + '.jpeg')
        self.imageName = getPath('ellipse', self.area)

    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.ellipse(screen, self.color, self.area, self.borderWidth)
        pygame.image.save(screen, self.imageName)

class Triangle:

    def __init__(self, pointlist, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth

        self.pointlist = pointlist
        # self.imageName = os.path.join('images', 'triangles', 'triangle' +
        #         str(pointlist) + '.jpeg')
        self.imageName = getPath('triangle', self.pointlist)

    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.polygon(screen, self.color, self.pointlist, self.borderWidth)
        pygame.image.save(screen, self.imageName)

class Rectangle:

    def __init__(self, area, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth
        self.area = area
        # self.imageName = os.path.join('images', 'rectangles', 'rectangle-' + str(area) + '.jpeg')
        self.imageName = getPath('rectangle', self.area)

    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.rect(screen, self.color, self.area, self.borderWidth)
        pygame.image.save(screen, self.imageName)

class Circle:
    def __init__(self, imageSize, color, borderWidth, margin):
        self.color = color
        self.borderWidth = borderWidth
        # radius 0 would lead to no shape. The circle has to fit on the smaller
        # side of the image, therefor 'min'. Twice the radius should not be
        # bigger than the size of the smaller side of the image without the
        # margins on both sites.
        smallerSide = min(imageSize[0], imageSize[1])
        self.radius = np.random.randint(1,  int(smallerSide - 2 * margin) / 2))
        # The y-Coordinate of the middle point should be at least as far from
        # each border as the radius + margin
        yCoordinate = np.random.randint(margin + radius, imageSize[0] - margin
                - radius)
        xCoordinate = np.random.randint(margin + radius, imageSize[1] - margin
                - radius)
        self.position = [xCoordinate, yCoordinate]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.borderWidth)
