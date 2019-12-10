import os
from os import listdir
from os.path import isfile, join

WORKING_DIR = "train/"

allFilesInTrain = [f for f in listdir(WORKING_DIR) if isfile(join(WORKING_DIR, f))]
allFilesInTrain.sort()
print('Initial number of files: ' + str(len(allFilesInTrain)))

orphans = []

for idx, elem in enumerate(allFilesInTrain):
    thiselem = elem
    nextelem = allFilesInTrain[(idx + 1) % len(allFilesInTrain)]
    if thiselem.endswith(".jpg"):
        if not nextelem.endswith(".xml"):
            orphans.append(thiselem)
    else:
        continue
print('Found images without labels: ' + str(len(orphans)))
print('Deleting...')
for orphan in orphans:
    os.remove(WORKING_DIR + orphan)

print('Final number of labeled images: ' + str(len([f for f in listdir(WORKING_DIR) if isfile(join(WORKING_DIR, f))])))
