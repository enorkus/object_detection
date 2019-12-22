import os
from os import listdir
from os.path import isfile, join
import shutil

TRAIN_DIR = "train/"
TEST_DIR = "test/"

allTrainFiles = [f for f in listdir(TRAIN_DIR) if isfile(join(TRAIN_DIR, f))]
print("All train files:")
print(len(allTrainFiles))

count = 0
numberOfTestFiles = len(allTrainFiles) * 0.2
os.mkdir(TEST_DIR)
for fileName in allTrainFiles:
    if allTrainFiles.index(fileName) < numberOfTestFiles:
        shutil.move(TRAIN_DIR + fileName, TEST_DIR + fileName)
        count += 1
    else:
        break

trainFiles = [f for f in listdir(TRAIN_DIR) if isfile(join(TRAIN_DIR, f))]
print("Train files:")
print(len(trainFiles))

testFiles = [f for f in listdir(TEST_DIR) if isfile(join(TEST_DIR, f))]
print("Test files:")
print(len(testFiles))
