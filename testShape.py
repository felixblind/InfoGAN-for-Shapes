import pygame
from scipy import misc
from Shapes import Container, Ellipse

def subMatrix(matrix):
     matrix = matrix + 1
     return matrix

white = [255,255,255]
black = [0,0,0]
screen = pygame.display.set_mode([28,28])
screen.fill(white)
area = [1,4,8,9]
rect = pygame.Rect(area)
pygame.draw.rect(screen, black, rect)
pygame.image.save(screen, 'test.png')
imageMatrix = misc.imread('test.png')

tmpMatrix0 = subMatrix(imageMatrix[:,:,0]) / 3
tmpMatrix1 = subMatrix(imageMatrix[:,:,1]) / 3
tmpMatrix2 = subMatrix(imageMatrix[:,:,2]) / 3
imageMatrix = (tmpMatrix0 + tmpMatrix1 + tmpMatrix2)

container = Container()
container.put(imageMatrix, 'ellipse')
container.getIdx(5, 'test.idx')

pygame.quit()
