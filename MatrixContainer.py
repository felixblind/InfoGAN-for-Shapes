import idx2numpy
import os
import numpy as np
import pickle

class Container:
    def __init__(self):
        self.rectangles = []
        self.ellipses = []
        self.triangles = []

    def put(self, matrix, matrixType):
        if matrixType == 'rectangle':
            self.rectangles.append(matrix)
        if matrixType == 'triangle':
            self.triangles.append(matrix)
        if matrixType == 'ellipse':
            self.ellipses.append(matrix)

    def getIdx(self, sampleSize, idxPath):

        # this method is a little bit lenghty. First we get ourselves the paths
        # to store the idx files. then we draw training and testing matrices
        # from the previously filled containers and store them with labels in
        # lists. this lists are then shuffled and the labels and the matrices
        # are separated into four lists. This lists are stored in idx files.

        trainLabelsPath = os.path.join(idxPath, 'train-labels-idx1-ubyte')
        trainImagePath = os.path.join(idxPath, 'train-images-idx3-ubyte')
        testLabelsPath = os.path.join(idxPath, 't10k-labels-idx1-ubyte')
        testImagePath = os.path.join(idxPath, 't10k-images-idx3-ubyte')

        trainMatrixAndLabelsSample = []
        testMatrixAndLabelsSample = []
        testMatrixSample = []
        trainMatrixSample = []
        testLabelsSample = []
        trainLabelsSample = []

        for _ in range(int((sampleSize * .9) / 3)):
            trainMatrixAndLabelsSample.append([0,
                self.ellipses[np.random.randint(len(self.ellipses))]])
            # trainMatrixAndLabelsSample.append([1,
            #     self.rectangles[np.random.randint(len(self.rectangles))]])
            # trainMatrixAndLabelsSample.append([2,
            #     self.triangles[np.random.randint(len(self.triangles))]])
        for _ in range(int((sampleSize * .1) / 3)):
            testMatrixAndLabelsSample.append([0,
                self.ellipses[np.random.randint(len(self.ellipses))]])
            # testMatrixAndLabelsSample.append([1,
            #     self.rectangles[np.random.randint(len(self.rectangles))]])
            # testMatrixAndLabelsSample.append([2,
            #     self.triangles[np.random.randint(len(self.triangles))]])

        # the lists have to be shuffled

        for matrixLabelTupel in trainMatrixAndLabelsSample:
            trainMatrixSample.append(matrixLabelTupel[1])
            trainLabelsSample.append(matrixLabelTupel[0])
        for matrixLabelTupel in testMatrixAndLabelsSample:
            testMatrixSample.append(matrixLabelTupel[1])
            testLabelsSample.append(matrixLabelTupel[0])

        pickle.dump([trainMatrixSample, trainLabelsSample, testMatrixSample,
            testLabelsSample], open('images.pkl', 'wb'), protocol=2)



        # idx2numpy.convert_to_file(trainImagePath, np.array(trainMatrixSample))
        # idx2numpy.convert_to_file(trainLabelsPath, np.array(trainLabelsSample))
        # idx2numpy.convert_to_file(testImagePath, np.array(trainMatrixSample))
        # idx2numpy.convert_to_file(testLabelsPath, np.array(testLabelsSample))
