import pickle

liste = pickle.load(open('images.pkl', 'rb'))

trainMatrixSample = liste[0]
trainLabelsSample = liste[1]
testMatrixSample = liste[2]
testLabelsSample = liste[3]
