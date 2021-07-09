import numpy as np
import cv2

FILENAME = "Gaussian-Image-of-the-point-cloud-represented-in-Fig-3.png"

img = cv2.imread(FILENAME)
grayImg = 255 - cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

subdiv = cv2.Subdiv2D((0, 0, grayImg.shape[0]-1, grayImg.shape[1]-1))

vertexArray = []
vertexArrayIndexHash = dict()

for x in range(0, grayImg.shape[0]-1):
    for y in range(0, grayImg.shape[1]-1):
        if grayImg[x, y] > 0:
            vertexArray.append((x, y, grayImg[x,y]))
            vertexArrayIndexHash[(x, y)] = len(vertexArray)-1
            subdiv.insert((x, y))

facesList = subdiv.getTriangleList()
facesArray = []

checklistArray = [0]*len(vertexArray)

for face in facesList:
    newFaceTuple = []
    for i in range(0, 6, 2):
        x = face[i]
        y = face[i+1]
        newFaceTuple.append(vertexArrayIndexHash[(x, y)])
        checklistArray[vertexArrayIndexHash[(x, y)]] = 1

    facesArray.append(tuple(newFaceTuple))

# validate that there is no vertex that is not being used in 2
for idx, vertex in enumerate(checklistArray):
    if vertex == 0:
        print("Error "+str(idx))
