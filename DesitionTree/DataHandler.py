import random

from Parameters import *
from Standars import *

def rand(lower, upper):
    return random.randint(lower, upper) 

def readDataset(path):
    dataFile = open(path, "r")
    data = dataFile.read()
    dataFile.close()

    return data

def parseData(rawData):
    linedData = rawData.split("\n")
    del linedData[-1]

    parsedData = []

    for line in linedData:
        tmpData = line.split(",")
        classification = tmpData[-1] # get classification
        del tmpData[-1]

        data = [] 
        for element in tmpData:
            data.append(float(element)) # get features values

        data.append(classes[classification]) # get code of the classification

        parsedData.append(data) # store the sample

    return parsedData

def divideData(data):
    size = len(data)

    testSz = int(size * testRate)
    heldSz = int(size * heldoutRate)
    trainSz = size - (testSz + heldSz)

    train = []
    heldout = []
    test = []

    for i in range(size-1, -1, -1):
        pos = rand(0, i)
        sample = data[pos]

        if size-i <= trainSz:
            train.append(sample)
        elif size-i <= heldSz+trainSz:
            heldout.append(sample)
        else:
            test.append(sample)

        del data[pos]

    return train, heldout, test

def getConsistentData(query, dataset):
    consistentData = []
    for data in dataset:
        if data[-1] == query:
            consistentData.append(data)

    return consistentData

def removeLabel(dataset):
    for data in dataset:
        del data[-1]
    return dataset

def getPureData(dataset):
    data = []
    for dat in dataset:
        del dat[-1]
        data.append(dat)
    return data

def buildTable(dataset):
    size = len(dataset[0])
    table = [ [] for i in range(size) ]

    for data in dataset:
        for idx, dat in enumerate(data):
            table[idx].append(dat)

    return table
