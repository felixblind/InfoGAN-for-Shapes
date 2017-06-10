import pickle
import numpy as np

__liste__ = pickle.load(open('images.pkl', 'rb'))

trainMatrixSample = np.array(__liste__[0])
trainLabelsSample = np.array(__liste__[1])
testMatrixSample = np.array(__liste__[2])
testLabelsSample = np.array(__liste__[3])
