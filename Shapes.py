import pygame
import os
class Ellipse:

    def __init__(self, area, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth
        self.area = area
        self.imageName = os.path.join('images', 'ellipses', 'ellipse-' + str(area) + '.jpeg')

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
        self.imageName = os.path.join('images', 'triangles', 'triangle' +
                str(pointlist) + '.jpeg')

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
        self.imageName = os.path.join('images', 'rectangles', 'rectangle-' + str(area) + '.jpeg')

    def draw(self, imageSize):
        screen = pygame.display.set_mode(imageSize)
        white = [255,255,255]
        screen.fill(white)
        pygame.draw.rect(screen, self.color, self.area, self.borderWidth)
        pygame.image.save(screen, self.imageName)
