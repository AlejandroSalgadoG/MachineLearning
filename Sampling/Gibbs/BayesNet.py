import random

from Distribution import *

def rand():
    return random.randint(0,100) / 100

def probC():
    gen = rand()
    return selectElem(cloudy, gen)

def probR(probC):
    gen = rand()

    desc, prob = probC
    table = rain[desc]

    return selectElem(table, gen)

def probS(probC):
    gen = rand()

    desc, prob = probC
    table = sprinkler[desc]

    return selectElem(table, gen)

def probW(probS, probR):
    gen = rand()

    descS, probS = probS
    descR, probR = probR
    table = wetgrass[descS][descR]

    return selectElem(table, gen)

def selectElem(table, gen):
    for desc, prob in table:
        gen -= prob
        if gen <= 0:
            return (desc, prob)

def getRandVar(query):
    querySz = len(query)

    idx = random.randint(0,querySz-1)

    return query[idx]
